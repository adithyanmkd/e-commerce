from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator


# product views
def index(request):
    return render(request, 'index.html')

def products(request):
    items = Product.objects.all()
    page = 1
    if request.method == 'GET':
        page = request.GET.get('page', 1)

    page_list = Paginator(items, 3)
    items = page_list.page(page)

    print(f"{page_list.count} items")

    item_list = {'item':items}
    return render(request, 'products.html',item_list)

def item(request):
    return render(request, 'item.html')