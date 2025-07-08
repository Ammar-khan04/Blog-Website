from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.
class PostListView(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_at')
    template_name = 'blogs.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog_detail.html'