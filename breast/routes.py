from django.urls import include, path
from django.views.generic import TemplateView, RedirectView
from .controllers import BreastDetector

urlpatterns = [
    path('', TemplateView.as_view(template_name='breast/index.html')),
    path('predict/', BreastDetector.predict),
]
