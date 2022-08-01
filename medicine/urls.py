from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView


urlpatterns = [
    path('', RedirectView.as_view(url='/breast/')),
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('breast/', include('breast.routes')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
