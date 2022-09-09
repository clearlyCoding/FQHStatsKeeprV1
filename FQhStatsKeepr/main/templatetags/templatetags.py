from django import template

register = template.Library()

@register.filter(name='points')
def points(value1, value2):
    try:
        value1 += 1
        return value1-1
    except:
        value1 = 0
        return value1
    try:
        value2 += 1
        return value2-1
    except:
        value2 = 0
        return value2

    return value1+value2