from django.urls import path
from .views import home, about, user

urlpatterns = [
    path('', home, name="blog-home"),
    path('about/', about, name="blog-about"),
    path('user<str:name>/', user, name="blog-user"),
]