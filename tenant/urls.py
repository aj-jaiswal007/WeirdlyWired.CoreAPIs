from tenant.views import UserRegisterView, UserView
from django.urls import path


urlpatterns = [
    path("register/", UserRegisterView.as_view()),
    path("users/", UserView.as_view()),
]
