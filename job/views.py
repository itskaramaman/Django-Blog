from django.shortcuts import render
from .models import JobPost

def jobs(request):
    job_posts = JobPost.objects.all()
    return render(request, 'job/jobs.html', {'job_posts': job_posts})


def job(request, id):
    job_post = JobPost.objects.get(id=id)
    return render(request, 'job/job.html', {'job_post': job_post})

