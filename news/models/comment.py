from django.db import models
from .post import Post


class Comment(models.Model):
    author_name = models.CharField(max_length=255, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=255)
