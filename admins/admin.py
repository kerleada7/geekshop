from django.contrib import admin

# Register your models here.
from basket.models import Basket


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product')
    extra = 0