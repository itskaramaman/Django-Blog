from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)
from .models import Post, Like, Comment

class Home(View):
    def post(self, request, pk=None):   
        if not request.user.is_authenticated:
            return redirect("users-login")

        # Save Comment
        post = Post.objects.get(id=pk)
        message = request.POST.get('comment')
        if message:
            comment = Comment(post=post, author=request.user, message=message)
            comment.save()
            return redirect("/")

        # Like and unlike a post 
        already_liked = Like.objects.filter(post=post, user=request.user)
        if already_liked:
            already_liked.delete()
        else:
            like = Like(post=post, user=request.user)
            like.save()
        return redirect("/")

    def get(self, request):
        page = request.GET.get('page', 1)
        posts = Post.objects.select_related('author').all().order_by("-date_posted")
        for post in posts:
            post.liked_by_cur_user = post.liked_by_user(request.user.id)
            post.comments = post.get_comments()

        paginator = Paginator(posts, 5)
        context = {'posts': paginator.page(page)}
        return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ['-date_posted']
    paginate_by = 2
    
class UserPostListView(ListView):
    model = Post
    template_name = "blog/user_posts.html"
    context_object_name = "posts"
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


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

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
