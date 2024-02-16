from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator


# product views
def index(request):
    featured_products = Product.objects.order_by('title')[:4]
    latest_products = Product.objects.order_by('-id')[:4]
    kv_pair = {
        'featured_product':featured_products,
        'latest_product':latest_products
    }
    return render(request, 'index.html', kv_pair)

def products(request):
    items = Product.objects.all()
    page = 1
    if request.method == 'GET':
        page = request.GET.get('page', 1)

    page_list = Paginator(items, 2)
    items = page_list.page(page)

    print(f"{page_list.count} items")

    item_list = {'item':items}
    return render(request, 'products.html',item_list)

def item(request, p_id):
    item_id = Product.objects.get(pk=p_id)
    kv_pair = {'item':item_id}
    print(item_id.title)
    return render(request, 'item.html', kv_pair)