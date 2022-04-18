from authapp.forms import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import models

from authapp.models import User
from mainapp.models import Product, ProductCategories


class UserAdminRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'last_name', 'first_name', 'email', 'image', 'age')

    def __init__(self, *args, **kwargs):
        super(UserAdminRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['password1'].widget.attrs['placeholder'] = 'Введите пароль'
        self.fields['password2'].widget.attrs['placeholder'] = 'Подтвердите пароль'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Введите фамилию'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Введите имя'
        self.fields['email'].widget.attrs['placeholder'] = 'Введите email'
        self.fields['image'].widget.attrs['placeholder'] = 'Добавить фото'
        self.fields['age'].widget.attrs['placeholder'] = 'Возраст'

        for filed_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'


class UserAdminProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'last_name', 'first_name', 'email', 'image', 'age')

    def __init__(self, *args, **kwargs):
        super(UserAdminProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = True

        for filed_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'

        self.fields['image'].widget.attrs['class'] = 'custom-file-input'


# product
class AdminProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AdminProductForm, self).__init__(*args, **kwargs)

        for filed_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'

        self.fields['image'].widget.attrs['class'] = 'custom-file-input'


class AdminProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AdminProductUpdateForm, self).__init__(*args, **kwargs)

        for filed_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'

        self.fields['image'].widget.attrs['class'] = 'custom-file-input'


# category
class AdminCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategories
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AdminCategoryForm, self).__init__(*args, **kwargs)

        for filed_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'


class AdminCategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = ProductCategories
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AdminCategoryUpdateForm, self).__init__(*args, **kwargs)

        for filed_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'


