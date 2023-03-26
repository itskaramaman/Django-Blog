from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def get_comments(self):
        return Comment.objects.filter(author=self.author, post=self)

    def get_likes(self):
        return Like.objects.filter(user=self.author, post=self)

    def liked_by_user(self):
        return Like.objects.filter(user=self.author, post=self).first() != None


class Comment(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return f'{self.post} liked by {self.author}'


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.post} liked by {self.user}'
