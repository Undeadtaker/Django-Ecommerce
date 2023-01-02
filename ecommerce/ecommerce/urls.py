from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = \
    [
        path('admin/', admin.site.urls),
        path('checkout/', include('checkout.urls', namespace = 'checkout')),
        path('account/', include('account.urls', namespace='account')),
        path('basket/', include('cart.urls', namespace='basket')),
        path('', include('store.urls', namespace='store')),
        path('__debug__/', include('debug_toolbar.urls'))
    ]

# If debug mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
