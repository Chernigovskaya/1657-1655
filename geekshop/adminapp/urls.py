from django.urls import path

from adminapp.views import admin_categories, \
    admin_category_create, \
    admin_category_update, admin_category_delete, IndexTemplateView, UserListView, \
    UserCreateView, UserUpdateView, UserDeleteView, ProductListView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView

app_name = 'adminapp'
urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('user_create/', UserCreateView.as_view(), name='admin_user_create'),
    path('user_update/<int:pk>/', UserUpdateView.as_view(), name='admin_user_update'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='admin_user_delete'),
    # product
    path('products/', ProductListView.as_view(), name='admin_products'),
    path('product_create/', ProductCreateView.as_view(), name='admin_product_create'),
    path('product_update/<int:pk>/', ProductUpdateView.as_view(), name='admin_product_update'),
    path('product_delete/<int:pk>/', ProductDeleteView.as_view(), name='admin_product_delete'),
    # category
    path('categories/', admin_categories, name='admin_categories'),
    path('category_create/', admin_category_create, name='admin_category_create'),
    path('category_update/<int:id>/', admin_category_update,
         name='admin_category_update'),
    path('category_delete/<int:id>/', admin_category_delete,
         name='admin_category_delete'),
]
