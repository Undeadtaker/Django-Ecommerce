from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Category, Product

def product_all(req):
    products = Product.objects.prefetch_related("product_image").filter(is_active=True)
    categories = Category.objects.filter(level=0)
    context = \
        {
            'products': products,
            'categories': categories
        }
    return render(req, 'store/home.html', context)

def product_single(req, slug):
    categories = Category.objects.filter(level=0)
    product = get_object_or_404(Product, slug=slug)
    context = \
        {
            'product': product,
            'categories': categories
        }
    return render(req, 'store/product.html', context)


def category_single(req, category_slug=None):
    categories = Category.objects.all()
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(
        category__in=Category.objects.get(slug=category_slug).get_descendants(include_self=True)
    )
    context = \
        {
            'category': category,
            'products': products,
            'categories': categories
        }

    return render(req, 'store/category.html', context)
