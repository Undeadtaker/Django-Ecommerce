from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from .basket import Basket
from store.models import Product, Category

# Create your views here.
def basket_summary(req):
    categories = Category.objects.all()
    basket = Basket(req)
    context = {'store': basket, 'categories': categories}
    return render(req, 'cart/summary.html', context)


def basket_add(req):
    basket = Basket(req)
    if req.POST.get('action') == 'post':
        product_id = int(req.POST.get('productid'))
        product_quantity = int(req.POST.get('productquantity'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, quantity=product_quantity)
        return JsonResponse({'quantity': len(basket),})

def basket_delete(req):
    basket = Basket(req)
    if req.POST.get('action') == 'delete':
        product_id = int(req.POST.get('productid'))
        basket.delete(product_id)
        return JsonResponse({'quantity': len(basket), 'subtotal': basket.get_total_price() })


def basket_update(req):
    basket = Basket(req)
    if req.POST.get('action') == 'update':
        product_id = int(req.POST.get('productid'))
        product_quantity = int(req.POST.get('productquantity'))

        basket.update(product=product_id, quantity=product_quantity)
        return JsonResponse({'quantity': len(basket), 'subtotal': basket.get_total_price() })

