from django import template

register=template.Library()


def Swap(value):
    return value.swapcase()

register.filter('Swap',Swap)