from django.db import models
from django.utils import timezone


class Post(models.Model):
    post_type = models.BooleanField(default=False)
    message = models.CharField(max_length=280)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    submit_time = models.DateTimeField(default=timezone.now)
    
    
class Sort(models.Model):
    sort_by =models.CharField(
        max_length=3)

    def __str__(self):
        return self.message
