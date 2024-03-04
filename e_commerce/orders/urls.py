from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/', views.add_to_cart, name='cart_page'),
    path('cart_item_remove/<item_id>', views.cart_item_remove, name='remove_item'),
    path('checkout', views.checkout, name='checkout'),
]