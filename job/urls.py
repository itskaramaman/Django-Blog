from django.urls import path
from .views import jobs, job

urlpatterns = [
    path('', jobs, name="jobs"),
    path('job/<int:id>', job, name="job")
]