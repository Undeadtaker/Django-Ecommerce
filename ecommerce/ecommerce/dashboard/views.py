from django.http import JsonResponse
from django.shortcuts import render, HttpResponseRedirect, reverse

from .forms import AddressForm
from ecommerce.users.models import Address

from dj_shop_cart.cart import get_cart_class
Cart = get_cart_class()


# Create your views here.
def dashboard(req):
    return render(req, 'dashboard/dashboard.html')

# ----------------------------------------------------------------
# ADDRESS SECTION
# ----------------------------------------------------------------
def view_addresses(req):
    addresses = Address.objects.filter(user=req.user).order_by('-default')
    return render(req, 'dashboard/view_addresses.html', {'addresses': addresses})


def add_address(req):
    if req.method == 'POST':
        form = AddressForm(data=req.POST)
        if form.is_valid():
            new_address = form.save(commit=False)
            new_address.default = True if not Address.objects.filter(user=req.user) else False
            new_address.user = req.user
            form.save()
            return HttpResponseRedirect(reverse('dashboard:view_addresses'))
    else:
        form = AddressForm()

    return render(req, 'dashboard/add_address.html', {'form': form})


def edit_address(req, id):
    if req.method == 'POST':
        address = Address.objects.get(pk=id, user=req.user)
        address_form = AddressForm(instance=address, data=req.POST)
        if address_form.is_valid():
            address_form.save()
            return HttpResponseRedirect(reverse('dashboard:view_addresses'))
    else:
        address = Address.objects.get(pk=id, user = req.user)
        address_form = AddressForm(instance=address)
    return render(req, 'dashboard/add_address.html', {'form': address_form})


def delete_address(req, id):
    Address.objects.get(pk=id, user = req.user).delete()
    return HttpResponseRedirect(reverse('dashboard:view_addresses'))


def set_default_address(req, id):
    Address.objects.filter(user = req.user, default = True).update(default=False)
    Address.objects.filter(user=req.user, pk=id).update(default=True)

    # previous_url = req.META.get('HTTP_REFERER')
    # if 'delivery_address' in previous_url:
    #     return redirect('checkout:delivery_address')

    return HttpResponseRedirect(reverse('dashboard:view_addresses'))

# ----------------------------------------------------------------
# CART section
# ----------------------------------------------------------------
def view_cart(req):
    return render(req, 'dashboard/view_cart.html')


def cart_delete_item(req):
    if req.POST.get('action') == 'delete':
        cart = Cart.new(req)
        product_id = req.POST.get('product_id')
        for item in cart:
            if item.product_pk == product_id:
                cart.remove(item.id)
                req.session.modified = True
        return JsonResponse({'quantity': cart.count, 'subtotal': cart.total, 'removed_item_id': product_id})


def cart_update_item():
    return None
