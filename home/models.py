from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.text import slugify


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True, null=True)




    def __str__(self):
        return self.description




class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    tweet = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reply', null=True, blank=True)

    def __str__(self):
        return self.tweet

