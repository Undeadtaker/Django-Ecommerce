import json

from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import DeliveryOptions
from cart.basket import Basket
from account.models import Address

@login_required
def delivery_choices(req):
    deliverychoices = DeliveryOptions.objects.filter(is_active=True)
    return render(req, 'checkout/delivery_choices.html', {'deliveryoptions': deliverychoices})


@login_required
def basket_update_delivery(req):
    basket = Basket(req)
    if req.POST.get('action') == 'post':
        delivery_option = int(req.POST.get('deliveryoption'))
        delivery_type = DeliveryOptions.objects.get(id=delivery_option)
        updated_total_price = basket.basket_update_delivery(delivery_type.delivery_price)

        session = req.session
        if 'purchase' not in session:
            session['purchase'] = {'delivery_id': delivery_type.id}
        else:
            session['purchase']['delivery_id'] = delivery_type.id
            session.modified = True

        context = \
            {
                'total': updated_total_price,
                'delivery_price': delivery_type.delivery_price
            }

        return JsonResponse(context)


@login_required
def delivery_address(req):
    session = req.session
    if 'purchase' not in session:
        messages.success(req, 'Please select a delivery option before proceeding.')
        return HttpResponseRedirect(req.META['HTTP_REFERER'])

    else:
        delivery_price = DeliveryOptions.objects.get(id = session['purchase']['delivery_id']).delivery_price
        addresses = Address.objects.filter(custom_user=req.user).order_by('-default')
        price_with_delivery = Basket(req).basket_update_delivery(delivery_price)


        if 'address' not in session and not addresses:
            addresses = None
        elif 'address' not in session:
            session['address'] = {'address': str(addresses[0].id)}
        else:
            session['address']['address'] = str(addresses[0].id)
            session.modified = True

        context = \
            {
                'addresses': addresses,
                'delivery_price': delivery_price,
                'price_with_delivery': price_with_delivery
            }

        return render(req, 'checkout/delivery_address.html', context)



@login_required()
def payment_selection(req):
    session = req.session
    if 'purchase' not in session and 'address' not in session:

        messages.success(req, 'Make sure you have selected a delivery method and a purchase address')
        return HttpResponseRedirect(req.META['HTTP_REFERER'])

    else:

        delivery_price = DeliveryOptions.objects.get(id=session['purchase']['delivery_id']).delivery_price
        price_with_delivery = Basket(req).basket_update_delivery(delivery_price)

        context = \
            {
                'delivery_price': delivery_price,
                'price_with_delivery': price_with_delivery
            }

        return render(req, 'checkout/payment_selection.html', context)









