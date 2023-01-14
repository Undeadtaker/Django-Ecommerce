from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.http import JsonResponse

from dj_shop_cart.cart import get_cart_class
from .models import Product


Cart = get_cart_class()  # get the cart object


# Renders all products page
def render_all_products(req):
    products = Product.objects.all()
    context_dict = {'products': products}
    return render(req, 'products/all_products.html', context_dict)


# Renders single product page
def render_single_product(req, slug):
    product = get_object_or_404(Product, slug=slug)
    context_dict = {'product': product}
    return render(req,'products/single_product.html', context_dict)


# Will maybe be moved to basket app
@require_POST
def add_product_to_basket(req):
    if req.method == 'POST':
        cart = Cart.new(req)
        product_id = int(req.POST.get('product_id'))
        quantity = int(req.POST.get('quantity'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product, variant=None, quantity=quantity)
        return JsonResponse({'cart_quantity': cart.count})
