from django.urls import path

from .views import index, UserUpdateView, UserCreateView, UserListView, UserDeleteView, CategoryUpdateView, \
    CategoryCreateView, CategoryListView, CategoryDeleteView, ProductsListView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

app_name = 'admins'
urlpatterns = [

    path('', index, name='index'),
    path('users/', UserListView.as_view(), name='admins_user'),
    path('users-create/', UserCreateView.as_view(), name='admins_user_create'),
    path('users-update/<int:pk>/', UserUpdateView.as_view(), name='admins_user_update'),
    path('users-delete/<int:pk>/', UserDeleteView.as_view(), name='admins_user_delete'),

    path('categorias/', CategoryListView.as_view(), name='admins_category'),
    path('categorias-create/', CategoryCreateView.as_view(), name='admins_category_create'),
    path('categorias-update/<int:pk>/', CategoryUpdateView.as_view(), name='admins_category_update'),
    path('categorias-delete/<int:pk>/', CategoryDeleteView.as_view(), name='admins_category_delete'),

    path('products/', ProductsListView.as_view(), name='admins_products'),
    path('products-create/', ProductCreateView.as_view(), name='admins_product_create'),
    path('products-update/<int:pk>', ProductUpdateView.as_view(), name='admins_product_update'),
    path('products-delete/<int:pk>', ProductDeleteView.as_view(), name='admins_product_delete'),
]
