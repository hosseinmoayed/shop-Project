from django import template


register = template.Library()



@register.filter(name="splitletter")
def Splitletter(value: int):
    return "{:,}".format(value) +" "+ 'تومان'