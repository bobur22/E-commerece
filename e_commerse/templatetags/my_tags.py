from django import template

register = template.Library()

@register.simple_tag()
def count_cart(request):
    cart = request.session.get('cart', [])
    return len(cart)
