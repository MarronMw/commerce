
from django.contrib import admin  # type: ignore
from django.urls import path, include  # type: ignore
from crud import urls
from django.conf.urls.static import static  # type: ignore
from django.conf import settings  # type: ignore

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crud.urls')),
    path('paypal/', include("paypal.standard.ipn.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
