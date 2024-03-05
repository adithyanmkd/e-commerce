from django import template
 
register = template.Library()

@register.simple_tag(name="code")
def order_status(arg):
    if arg == 1:
        status = 'order confirmed'
    else:
        arg -= 2
        status = ['order processed', 'order deliverd', 'order rejected']
        status = status[arg]
    return status