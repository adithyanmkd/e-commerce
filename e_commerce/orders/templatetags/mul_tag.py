from django import template

register = template.Library()

@register.simple_tag(name="mul")
def multiply(a, b):
    return a * b