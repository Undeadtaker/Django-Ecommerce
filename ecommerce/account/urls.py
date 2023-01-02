from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from . import views
from .forms import UserLoginForm, MyPasswordResetForm, MyPasswordConfirmForm


app_name = 'account'
urlpatterns = \
    [
        path('activate/<slug:uidb64>/<slug:token>', views.account_activate, name='activate'),
        path('dashboard', views.dashboard, name='dashboard'),

        # include login/logout/register
        path('login/', auth_views.LoginView.as_view(template_name='account/login.html', form_class=UserLoginForm), name='login'),
        path('logout/', auth_views.LogoutView.as_view(next_page='/account/login/'), name='logout'),
        path('register/', views.account_register, name='register'),

        # user dashboard
        path('profile/edit/', views.edit_details, name='edit_details'),
        path('profile/delete/', views.delete_user, name='delete_user'),
        path('profile/delete_confirm/', TemplateView.as_view(template_name="account/delete_confirmation.html"), name='delete_confirmation'),

        # user password reset
        path('password_reset/',
             auth_views.PasswordResetView.as_view(template_name = 'account/password_reset_form.html',
                                                  success_url = 'password_reset_email_confirm',
                                                  email_template_name = 'account/password_reset_email.html',
                                                  form_class = MyPasswordResetForm),
                                                  name = 'password_reset'),

        path('password_reset/password_reset_email_confirm', TemplateView.as_view(template_name='account/reset_status.html')),

        path('password_reset_confirm/<uidb64>/<token>',
                    auth_views.PasswordResetConfirmView.as_view(template_name = 'account/password_reset_confirm.html',
                                                                success_url='/account/password_reset_complete/',
                                                                form_class = MyPasswordConfirmForm),
                                                                name = 'password_reset_confirm'),

        path('password_reset_complete/',
             TemplateView.as_view(template_name="account/reset_status.html"), name='password_reset_complete'),

        path("user_orders/", views.user_orders, name="user_orders"),

        # user adresses
        path('addresses/', views.view_addresses, name='addresses'),
        path('add_address/', views.view_add_address, name='add_addresses'),
        path('address/edit/<slug:id>/', views.edit_address, name='edit_address'),
        path('address/delete/<slug:id>/', views.delete_address, name='delete_address'),
        path('address/set_default/<slug:id>/', views.set_default, name='set_default'),

        # wishlist
        path('wishlist', views.view_wishlist, name='wishlist'),
        path('wishlists/add_to_wishlist/<int:id>', views.add_to_wishlist, name='add_to_wishlist')

    ]



















