from django.urls import include, path

from . import views

app_name = 'products'
urlpatterns = \
    [
        path('', views.render_all_products, name='render_all_products')
    ]
