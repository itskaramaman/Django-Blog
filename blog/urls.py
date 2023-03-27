from django.urls import path
from .views import (home,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    like_post,
    add_comment,
    about)

urlpatterns = [
    path('', home, name="blog-home"),
    path('<int:pk>', home, name="blog-home"),
    path('post/<int:pk>', PostDetailView.as_view(), name="post-detail"),
    path('post/new', PostCreateView.as_view(), name="post-create"),
    path('post/like/<int:pk>', like_post, name="post-like"),
    path('post/comment/<int:pk>', add_comment, name="post-comment"),
    path('post/update/<int:pk>', PostUpdateView.as_view(), name="post-update"),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name="post-delete"),
    path('about/', about, name="blog-about"),
]