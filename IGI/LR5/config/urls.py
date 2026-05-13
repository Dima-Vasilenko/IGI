from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home),

    path('', include('accounts.urls')),
    path('', include('content.urls')),
    path('', include('catalog.urls')),
    path('', include('orders.urls')),
]


urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)