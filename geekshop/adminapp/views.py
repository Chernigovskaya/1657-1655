from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
# Create your views here.
from django.urls import reverse

from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, \
    AdminProductForm, AdminProductUpdateForm, AdminCategoryForm, AdminCategoryUpdateForm
from authapp.models import User
from mainapp.models import Product, ProductCategories


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'adminapp/admin.html')


@user_passes_test(lambda u: u.is_superuser)
def admin_users(request):
    context = {
        'title': 'Админка | Пользователи',
        'users': User.objects.all()
    }
    return render(request, 'adminapp/admin-users-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_user_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_users'))
        else:
            print(form.errors)
    else:
        form = UserAdminRegisterForm()
    context = {
        'title': 'Админка | Регистрация',
        'form': form
    }
    return render(request, 'adminapp/admin-users-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_user_update(request, id):
    user_select = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST, instance=user_select,
                                    files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_users'))
    else:
        form = UserAdminProfileForm(instance=user_select)
    context = {
        'title': 'Админка | Обновление пользователя',
        'form': form,
        'user_select': user_select
    }
    return render(request, 'adminapp/admin-users-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_user_delete(request, id):
    user = User.objects.get(id=id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('adminapp:admin_users'))


# product
@user_passes_test(lambda u: u.is_superuser)
def admin_products(request):
    context = {
        'title': 'Админка | Продукты',
        'products': Product.objects.all()
     }
    return render(request, 'adminapp/admin-product-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_product_create(request):
    if request.method == 'POST':
        form = AdminProductForm(data=request.POST, files=request.FILES)
        form.save()
        return HttpResponseRedirect(reverse('adminapp:admin_products'))

    else:
        form = AdminProductForm()
    context = {
        'title': 'Админка | Создать продукты',
        'form': form
    }
    return render(request, 'adminapp/admin-product-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_product_update(request, id):
    product_select = Product.objects.get(id=id)
    if request.method == 'POST':
        form = AdminProductUpdateForm(data=request.POST, instance=product_select,
                                          files=request.FILES)
        form.save()
        return HttpResponseRedirect(reverse('adminapp:admin_products'))
    else:
        form = AdminProductUpdateForm(instance=product_select)
    context = {
        'title': 'Админка | Обновление продуктов',
        'form': form,
        'product_select': product_select
    }
    return render(request, 'adminapp/admin-product-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_product_delete(request, id):
    pass
    product = Product.objects.get(id=id)
    product.delete()
    return HttpResponseRedirect(reverse('adminapp:admin_products'))


# category
@user_passes_test(lambda u: u.is_superuser)
def admin_categories(request):
    context = {
        'title': 'Админка | Категории',
        'categories': ProductCategories.objects.all()
     }
    return render(request, 'adminapp/admin-category-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_category_create(request):
    if request.method == 'POST':
        form = AdminCategoryForm(data=request.POST, files=request.FILES)
        form.save()
        return HttpResponseRedirect(reverse('adminapp:admin_categories'))

    else:
        form = AdminCategoryForm()
    context = {
        'title': 'Админка | Создать категорию товаров',
        'form': form
    }
    return render(request, 'adminapp/admin-category-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_category_update(request, id):
    category_select = ProductCategories.objects.get(id=id)
    if request.method == 'POST':
        form = AdminCategoryUpdateForm(data=request.POST, instance=category_select, files=request.FILES)
        form.save()
        return HttpResponseRedirect(reverse('adminapp:admin_categories'))
    else:
        form = AdminCategoryUpdateForm(instance=category_select)
    context = {
        'title': 'Админка | Обновление категории продуктов',
        'form': form,
        'category_select': category_select
    }
    return render(request, 'adminapp/admin-category-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_category_delete(request, id):
    pass
    category = ProductCategories.objects.get(id=id)
    category.delete()
    return HttpResponseRedirect(reverse('adminapp:admin_categories'))
