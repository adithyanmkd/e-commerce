from django.shortcuts import render

# product views
def index(request):
    return render(request, 'index.html')

def products(request):
    return render(request, 'products.html')

def item(request):
    return render(request, 'item.html')