from tenant.views import TempView
from django.urls import path


urlpatterns = [path("", TempView.as_view())]
