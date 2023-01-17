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
    ]
