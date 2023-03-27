from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Post, Like, Comment

def home(request, pk=None):
    if request.method == "POST":
        message = request.POST['comment']
        post = Post.objects.get(id=pk)
        comment = Comment(post=post, author=request.user, message=message)
        comment.save()
        return redirect("/")


    posts = Post.objects.all().order_by("-date_posted")
    for post in posts:
        post.liked_by_cur_user = post.liked_by_user(request.user)
        post.comments = post.get_comments()
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


def like_post(request, pk):
    post = Post.objects.get(id=pk)
    already_liked = Like.objects.filter(post=post, user=request.user)
    if already_liked:
        already_liked.delete()
    else:
        like = Like(post=post, user=request.user)
        like.save()
    return redirect("/")

def add_comment(request, pk):
    if request.method == "POST":
        pass
    post = Post.objects.get(id=pk)
    
    return redirect("/")


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
