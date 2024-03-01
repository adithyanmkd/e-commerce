from django.shortcuts import render, redirect
from . models import Order, OrderedItem
from products.models import Product

# cart page
def cart(request):
    user = request.user
    customer = user.customer_profile
    cart_obj, created = Order.objects.get_or_create(
        owner = customer,
        order_status = Order.CART_STAGE
    )
    item_dict = {'cart':cart_obj}
    return render(request, 'cart.html', item_dict)

def add_to_cart(request):
    method = request.POST
    if method:
        print(f"{method}============")
        user = request.user
        customer = user.customer_profile
        quantity = method.get('quantity')
        product_id = method.get('item_id')
        print(f"{product_id}========>>>>>>>>>")
        cart_obj, created = Order.objects.get_or_create(
            owner = customer,
            order_status = Order.CART_STAGE
        )
        product = Product.objects.get(pk=product_id)
        print(f">>>>>>>>>>============")
        orderd_item = OrderedItem.objects.create(
            product = product,
            quantity = int(quantity),
            owner = cart_obj,
        )
        return redirect('cart')