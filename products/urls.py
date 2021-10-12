from django.urls import path

from .views import products

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('category/<int:id_category>/', products, name='product'),
    path('page/<int:page_id>', products, name='page'),
]