from tenant.views import TempView, UserView
from django.urls import path


urlpatterns = [path("", TempView.as_view()), path("users/", UserView.as_view())]
