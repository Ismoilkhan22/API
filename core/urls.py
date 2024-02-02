from django.urls import path

from core.v1.auth import LoginView, RegisView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('regis/', RegisView.as_view()),
]







