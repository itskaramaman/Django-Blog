from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class JobPost(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class JobPostApplicant(models.Model):
    job = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    applied_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.job.title} applied by {self.applicant.username}'
