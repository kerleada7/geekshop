from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.generic import FormView

from .models import ProductCategory, Product

# Create your views here.

def index(request):
    content = {'title': 'GeekShop'}
    return render(request, 'products/index.html', content)


def products(request, id_category=None):
    if id_category is None:
        list_products = Product.objects.all()
    else:
        list_products = Product.objects.filter(category=id_category)

    links_menu_categories = ProductCategory.objects.all()

    content = {'title': 'GeekShop - Каталог',
               'list_products': list_products,
               'links_menu_categories': links_menu_categories
               }
    return render(request, 'products/products.html', content)


class IndexView(FormView):
    form_class = FormView
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Каталог'
        return context

