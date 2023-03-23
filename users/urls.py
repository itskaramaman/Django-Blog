from django.urls import path
from .views import register
from django.contrib.auth import views

urlpatterns = [
    path("register/", register, name="users-register"),
    path("login/", views.LoginView.as_view(), name="users-login"),
    path("logout/", views.LogoutView.as_view(), name="users-logout")
]