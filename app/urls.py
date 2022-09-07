from django.urls import path
from .views import prediction, register, dlogin ,login, get_predictions_per_user, get_predictions_for_doctor, create_comment

urlpatterns = [
    path('predict/', prediction),
    path('register/', register),
    path('login/', login),
    path('dlogin/', dlogin),
    path('user/', get_predictions_per_user),
    path('doctor/', get_predictions_for_doctor),
    path('comment/', create_comment)
]
