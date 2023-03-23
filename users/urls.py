from django.urls import path
from .views import register, profile
from django.contrib.auth import views

urlpatterns = [
    path("register/", register, name="users-register"),
    path("login/", views.LoginView.as_view(template_name='users/login.html'), name="users-login"),
    path("logout/", views.LogoutView.as_view(template_name='users/logout.html'), name="users-logout"),
    path("profile/", profile, name="users-profile")
]