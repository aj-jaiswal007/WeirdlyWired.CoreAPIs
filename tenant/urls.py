from tenant.views import UserRegisterView, UserViewSet, ProfileView
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="user")

urlpatterns = [
    path("register/", UserRegisterView.as_view()),
    path("user/profile/", ProfileView.as_view()),
    path("", include(router.urls)),
]
