from django.urls import path

from adminapp.views import IndexTemplateView, UserListView, \
    UserCreateView, UserUpdateView, UserDeleteView, ProductListView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView, CategoryListView, CategoryCreateView, \
    CategoryUpdateView, CategoryDeleteView

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
    path('product_update/<int:pk>/', ProductUpdateView.as_view(),
         name='admin_product_update'),
    path('product_delete/<int:pk>/', ProductDeleteView.as_view(),
         name='admin_product_delete'),
    # category
    path('categories/', CategoryListView.as_view(), name='admin_categories'),
    path('category_create/', CategoryCreateView.as_view(),
         name='admin_category_create'),
    path('category_update/<int:pk>/', CategoryUpdateView.as_view(),
         name='admin_category_update'),
    path('category_delete/<int:pk>/', CategoryDeleteView.as_view(),
         name='admin_category_delete'),
]
