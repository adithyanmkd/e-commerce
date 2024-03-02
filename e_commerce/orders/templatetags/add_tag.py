from django import template
 
register = template.Library()

@register.simple_tag(name="add")
def addition(items):
    total = 0
    for item in items.added_item.all():
        total += item.product.price * item.quantity
    return total