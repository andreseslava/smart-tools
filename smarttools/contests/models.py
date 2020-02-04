from datetime import datetime

from django.conf import settings
from django.db import models


class Contest(models.Model):
    name = models.CharField(max_length=150, default='Non Name')
    startDate = models.DateTimeField(default=datetime.now())
    endDate = models.DateTimeField(default=datetime.now())
    path = models.CharField(max_length=8, default='Non Path')
    prize = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(auto_now_add=False)
    logo = models.FileField(upload_to='logos',null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, blank=False, default=1)


    def __str__(self):
        return self.name