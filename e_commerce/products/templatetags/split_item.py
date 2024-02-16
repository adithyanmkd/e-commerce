from django import template

register = template.Library()

@register.filter(name='split')
def split_item(item, size):
    item_list = []
    x = 0
    for i in item:
        item_list.append(i)
        x += 1
        if x == size:
            yield item_list
            item_list = []
    yield item_list
