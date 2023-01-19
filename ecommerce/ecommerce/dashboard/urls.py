from django.urls import include, path

from . import views

app_name = 'dashboard'
urlpatterns = \
    [
        path('', views.dashboard, name='dashboard'),
        path('addresses', views.view_addresses, name='view_addresses'),
        path('add_address', views.add_address, name='add_address'),
        path('edit/<slug:id>', views.edit_address, name='edit_address'),
        path('delete/<slug:id>', views.delete_address, name='delete_address'),
        path('set_default/<slug:id>', views.set_default_address, name='set_default'),

        # cart
        path('view_cart', views.view_cart, name='view_cart'),
        path('cart_delete_item', views.cart_delete_item, name='cart_delete_item'),
        path('cart_update_item', views.cart_update_item, name='cart_update_item')
    ]
