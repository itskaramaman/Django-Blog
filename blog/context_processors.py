from .models import Comment, Like, Post
from django.db.models import Count

def sidebar(request):
    # Most Liked Post
    most_liked_post_id = Like.objects.all().values('post').annotate(Count('post')).order_by('-post__count')[0]['post']
    most_liked_post = Post.objects.get(id=most_liked_post_id)

    # Most Commented Post
    most_commented_post_id = Comment.objects.all().values('post').annotate(Count('message')).order_by('-message__count')[0]['post']
    most_commented_post = Post.objects.get(id=most_commented_post_id)

    return {
        'most_liked_post': most_liked_post,
        'most_commented_post': most_commented_post
    }