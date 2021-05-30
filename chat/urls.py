from django.urls import path
from chat.views import TestChatView

urlpatterns = [
    path("", TestChatView.as_view()),
]
