from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse, reverse_lazy
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, \
    AdminProductForm, AdminProductUpdateForm, AdminCategoryForm, AdminCategoryUpdateForm
from authapp.models import User
from adminapp.mixin import BaseClassContextMixin, CustomDispatchMixin
from mainapp.models import Product, ProductCategories

from django.views.generic import TemplateView, ListView, UpdateView, DetailView, \
    DeleteView, CreateView


# @user_passes_test(lambda u: u.is_superuser)
# def index(request):
#     return render(request, 'adminapp/admin.html')

class IndexTemplateView(TemplateView, BaseClassContextMixin, CustomDispatchMixin):
    template_name = 'adminapp/admin.html'
    title: 'Главная страница'


class UserListView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-read.html'
    title: 'Админка | Пользователи'
    context_object_name = 'users'


# @user_passes_test(lambda u: u.is_superuser)
# def admin_users(request):
#     context = {
#         'title': 'Админка | Пользователи',
#         'users': User.objects.all()
#     }
#     return render(request, 'adminapp/admin-users-read.html', context)


# @user_passes_test(lambda u: u.is_superuser)
# def admin_user_create(request):
#     if request.method == 'POST':
#         form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('adminapp:admin_users'))
#         else:
#             print(form.errors)
#     else:
#         form = UserAdminRegisterForm()
#     context = {
#         'title': 'Админка | Регистрация',
#         'form': form
#     }
#     return render(request, 'adminapp/admin-users-create.html', context)


class UserCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-create.html'
    form_class = UserAdminRegisterForm
    title: 'Админка | Регистрация'
    success_url = reverse_lazy('adminapp:admin_users')


# @user_passes_test(lambda u: u.is_superuser)
# def admin_user_update(request, id):
#     user_select = User.objects.get(id=id)
#     if request.method == 'POST':
#         form = UserAdminProfileForm(data=request.POST, instance=user_select,
#                                     files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('adminapp:admin_users'))
#     else:
#         form = UserAdminProfileForm(instance=user_select)
#     context = {
#         'title': 'Админка | Обновление пользователя',
#         'form': form,
#         'user_select': user_select
#     }
#     return render(request, 'adminapp/admin-users-update-delete.html', context)


class UserUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    title: 'Админка | Обновление пользователя'
    success_url = reverse_lazy('adminapp:admin_users')


# @user_passes_test(lambda u: u.is_superuser)
# def admin_user_delete(request, id):
#     user = User.objects.get(id=id)
#     user.is_active = False
#     user.save()
#     return HttpResponseRedirect(reverse('adminapp:admin_users'))


class UserDeleteView(DeleteView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('adminapp:admin_users')


    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# product

class ProductListView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'adminapp/admin-product-read.html'
    title: 'Админка | Продукты'
    context_object_name = 'products'


# @user_passes_test(lambda u: u.is_superuser)
# def admin_products(request):
#     context = {
#         'title': 'Админка | Продукты',
#         'products': Product.objects.all()
#      }
#     return render(request, 'adminapp/admin-product-read.html', context)


# @user_passes_test(lambda u: u.is_superuser)
# def admin_product_create(request):
#     if request.method == 'POST':
#         form = AdminProductForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('adminapp:admin_products'))
#         else:
#             print(form.errors)
#
#     else:
#         form = AdminProductForm()
#     context = {
#         'title': 'Админка | Создать продукты',
#         'form': form
#     }
#     return render(request, 'adminapp/admin-product-create.html', context)


class ProductCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'adminapp/admin-product-create.html'
    form_class = AdminProductForm
    title: 'Админка | Создать продукты'
    success_url = reverse_lazy('adminapp:admin_products')


# @user_passes_test(lambda u: u.is_superuser)
# def admin_product_update(request, id):
#     product_select = Product.objects.get(id=id)
#     if request.method == 'POST':
#         form = AdminProductUpdateForm(data=request.POST, instance=product_select,
#                                           files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('adminapp:admin_products'))
#         else:
#             print(form.errors)
#     else:
#         form = AdminProductUpdateForm(instance=product_select)
#     context = {
#         'title': 'Админка | Обновление продуктов',
#         'form': form,
#         'product_select': product_select
#     }
#     return render(request, 'adminapp/admin-product-update-delete.html', context)

class ProductUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'adminapp/admin-product-update-delete.html'
    form_class = AdminProductUpdateForm
    title: 'Админка | Обновление продуктов'
    success_url = reverse_lazy('adminapp:admin_products')


# @user_passes_test(lambda u: u.is_superuser)
# def admin_product_delete(request, id):
#     product = Product.objects.get(id=id)
#     product.delete()
#     return HttpResponseRedirect(reverse('adminapp:admin_products'))

class ProductDeleteView(DeleteView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'adminapp/admin-product-update-delete.html'
    form_class = AdminProductUpdateForm
    success_url = reverse_lazy('adminapp:admin_products')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())

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
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_categories'))
        else:
            print(form.errors)
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
        form = AdminCategoryUpdateForm(data=request.POST, instance=category_select,
                                       files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_categories'))
        else:
            print(form.errors)
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
