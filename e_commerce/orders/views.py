from django.shortcuts import render, redirect
from . models import Order, OrderedItem
from products.models import Product
from django.contrib import messages

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
        user = request.user
        customer = user.customer_profile
        quantity = method.get('quantity')
        product_id = method.get('item_id')
        cart_obj, created = Order.objects.get_or_create(
            owner = customer,
            order_status = Order.CART_STAGE
        )
        product = Product.objects.get(pk=product_id)
        orderd_item, created = OrderedItem.objects.get_or_create(
            product = product,
            owner = cart_obj
        )
        if created:
            orderd_item.quantity = quantity
            orderd_item.save()
        else:
            orderd_item.quantity += int(quantity)
            orderd_item.save()
        return redirect('cart')
    
def cart_item_remove(request, item_id):
    item = OrderedItem.objects.get(pk=item_id)
    if item:
        item.delete()
    return redirect('cart')

def checkout(request):
    if request.POST:
        try:
            user = request.user
            customer = user.customer_profile
            total = float(request.POST.get('total'))
            order_obj= Order.objects.get(
                owner = customer,
                order_status = Order.CART_STAGE
            )
            if order_obj:
                order_obj.order_status = Order.ORDER_CONFIRMED
                order_obj.total_price = total
                order_obj.save()
                status_msg = f"Your order confirmed {order_obj.total_price}"
                messages.success(request, status_msg)
            else:
                status_msg = "Unable to process your order try again"
                messages.error(request, status_msg)
        except Exception as e:
            status_msg = "exception msg occured"
            messages.error(request, status_msg)
    return redirect('cart')






