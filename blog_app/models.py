from django.db import models

class Post(models.Model):
    post_title = models.CharField(max_length=300)
    post_body = models.TextField(blank=True, null=True)
    post_author = models.CharField(max_length=30)
    post_date = models.DateField(auto_now=True)