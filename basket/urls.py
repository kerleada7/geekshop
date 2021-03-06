from django.urls import path

from .views import basket_add, basket_remove, basket_edit

app_name = 'basket'

urlpatterns = (
    path('add/<int:product_id>', basket_add, name='add'),
    path('remove/<int:product_id>', basket_remove, name='remove'),
    path('edit/<int:id>/<int:quantity>/', basket_edit, name='basket_edit')
)