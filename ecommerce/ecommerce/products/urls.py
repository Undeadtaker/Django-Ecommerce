from django.urls import include, path

from . import views

app_name = 'products'
urlpatterns = \
    [
        # POST method only, has to have CSRF token
        path('add_product_to_basket/', views.add_product_to_basket, name='add_product_to_basket'),

        path('<slug:slug>/', views.render_single_product, name='render_single_product'),
        path('', views.render_all_products, name='render_all_products'),
    ]
