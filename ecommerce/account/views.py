from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.shortcuts import redirect

from store.models import Category, Product

from .forms import RegistrationForm, UserEditForm, UserAddressForm
from .models import CustomUser, Address
from .token import account_activation_token
from .tasks import celery_send_mail



def account_register(req):
    if req.user.is_authenticated:
        return redirect('/')

    if req.method == 'POST':
        registerForm = RegistrationForm(req.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            user.is_active = False  # because we still need the email confirmation
            user.save()
            # Setup email
            current_site = get_current_site(req)
            subject = 'Activate your Account'
            message = render_to_string('account/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            celery_send_mail.delay(user.id, subject, message)
            return HttpResponse('Congratulations. Your Account has been '
                                        'created. Check your email to activate your it.')
    else:
        registerForm = RegistrationForm()

    return render(req, 'account/register.html', {'form': registerForm})


def account_activate(req, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(req, user)
        return redirect('account:dashboard')
    else:
        return render(req, 'account/activation_invalid.html')


# ---------------------------------------------------------------- #
# From this point on the user needs to be logged in
# ---------------------------------------------------------------- #
@login_required
def dashboard(req):
    categories = Category.objects.filter(level=0)
    context = {'categories': categories}
    return render(req, 'account/dashboard.html', context)


@login_required
def edit_details(req):
    categories = Category.objects.filter(level=0)
    if req.method == 'POST':
        user_form = UserEditForm(instance=req.user, data=req.POST)

        if user_form.is_valid():
            user_form.save()

    else:
        user_form = UserEditForm(instance=req.user)

    return render(req, 'account/edit_details.html', {'user_form': user_form, 'categories': categories})


@login_required
def delete_user(req):
    user = CustomUser.objects.get(id = req.user.id)
    user.is_active = False  # The user won't be able to log in
    user.save()
    logout(req)
    return redirect('account:delete_confirmation')

# ------------------------- #
# User Address Management
# ------------------------- #

@login_required()
def view_addresses(req):
    categories = Category.objects.filter(level=0)
    addresses = Address.objects.filter(custom_user = req.user)
    return render(req, 'account/addresses.html', {'addresses': addresses, 'categories': categories})


@login_required()
def view_add_address(req):
    if req.method == 'POST':
        new_address_form = UserAddressForm(data=req.POST)
        if new_address_form.is_valid():
            new_address = new_address_form.save(commit=False)
            new_address.custom_user = req.user
            new_address_form.save()
            return HttpResponseRedirect(reverse('account:addresses'))
    else:
        new_address_form = UserAddressForm()

    return render(req, 'account/edit_address.html', {'form': new_address_form})


@login_required()
def edit_address(req, id):

    if req.method == 'POST':
        address = Address.objects.get(pk=id, custom_user=req.user)
        address_form = UserAddressForm(instance=address, data=req.POST)
        if address_form.is_valid():
            address_form.save()
            return HttpResponseRedirect(reverse('account:addresses'))
    else:
        address = Address.objects.get(pk=id, custom_user = req.user)
        address_form = UserAddressForm(instance=address)
    return render(req, 'account/edit_address.html', {'form': address_form})


@login_required()
def delete_address(req, id):
    Address.objects.get(pk=id, custom_user = req.user).delete()
    return HttpResponseRedirect(reverse('account:addresses'))


@login_required()
def set_default(req, id):
    Address.objects.filter(custom_user = req.user, default = True).update(default=False)
    Address.objects.filter(custom_user=req.user, pk=id).update(default=True)

    previous_url = req.META.get('HTTP_REFERER')
    if 'delivery_address' in previous_url:
        return redirect('checkout:delivery_address')

    return HttpResponseRedirect(reverse('account:addresses'))


# ------------------------- #
# User Wishlist
# ------------------------- #
@login_required()
def view_wishlist(req):
    wishlist = Product.objects.filter(users_wishlist=req.user)
    return render(req, 'account/wishlist.html', {'wishlist': wishlist})


@login_required()
def add_to_wishlist(req, id):
    product = get_object_or_404(Product, pk=id)
    if product.users_wishlist.filter(id=req.user.id).exists():
        product.users_wishlist.remove(req.user)
        messages.success(req, f'Product {product.title} removed from wishlist.')
    else:
        product.users_wishlist.add(req.user)
        messages.success(req, f'Product {product.title} added to wishlist.')
    return HttpResponseRedirect(req.META['HTTP_REFERER'])
