from django.shortcuts import render

from django.views import generic
from .models import Post

class PostView(generic.ListView):
    template_name = 'blog.html'
    model = Post
    context_object_name = "post"