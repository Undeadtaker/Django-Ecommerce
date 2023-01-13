from django.shortcuts import render

from .models import Product

# Create your views here.
def render_all_products(req):
    products = Product.objects.all()
    context_dict = {'products': products}
    return render(req, 'products/all_products.html', context_dict)
