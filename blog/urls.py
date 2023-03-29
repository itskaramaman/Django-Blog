from django.urls import path
from .views import (Home,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    about)

urlpatterns = [
    path('', Home.as_view(), name="blog-home"),
    path('<int:pk>/', Home.as_view(), name="blog-home"),
    path('post/<int:pk>', PostDetailView.as_view(), name="post-detail"),
    path('post/new', PostCreateView.as_view(), name="post-create"),
    path('post/update/<int:pk>', PostUpdateView.as_view(), name="post-update"),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name="post-delete"),
    path('about/', about, name="blog-about"),
]