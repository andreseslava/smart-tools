from django.db import models

from contests.models import Contest


class Video(models.Model):
    title = models.CharField(max_length=100, default='Non-Title')
    description = models.CharField(max_length=500, null=True)
    name = models.CharField(max_length=150, default='Non-Name')
    sureName = models.CharField(max_length=150, null=True)
    email = models.EmailField(max_length=254, null=True)
    video = models.FileField(upload_to='videos')
    state = models.CharField(max_length=15, default="PENDING")
    created_At = models.DateTimeField(auto_now_add=True)
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE, null=False, blank=False, default=2)

    def __str__(self):
        return self.name + self.title
