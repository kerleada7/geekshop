from django.shortcuts import render


# Create your views here.

def index(request):
    content = {'title': 'GeekShop'}
    return render(request, 'products/index.html', content)


def products(request):
    list_products = [
                    {'name': "Худи черного цвета с монограммами adidas Originals", 'price': '6 090,00', 'image': '', 'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'}
                    ,{'name': 'Синяя куртка The North Face', 'price': '23 725,00', 'image': '', 'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'}
                    ,{'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': '3 390,00', 'image': '', 'description': 'Материал с плюшевой текстурой. Удобный и мягкий.'}
                    ]

    links_menu_categories = [
        {'id': 0, 'name': 'Новинки'},
        {'id': 1, 'name': 'Одежда'},
        {'id': 2, 'name': 'Обувь'},
        {'id': 3, 'name': 'Аксессуары'},
        {'id': 4, 'name': 'Подарки'},
    ]

    content = {'title': 'GeekShop - Каталог',
               'list_products': list_products,
               'links_menu_categories': links_menu_categories
               }
    return render(request, 'products/products.html', content)
