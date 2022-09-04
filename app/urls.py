from django.urls import path
from .views import prediction, register, login, get_predictions_per_user, get_predictions_for_doctor

urlpatterns = [
    path('predict/', prediction),
    path('register/', register),
    path('login/', login),
    path('user/', get_predictions_per_user),
    path('doctor/', get_predictions_for_doctor)
]
