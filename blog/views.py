from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, template_name='blog/index.html', context={'posts':posts})

def detail(request, pk):
    posts = Post.objects.get(pk=pk)
    return render(request, template_name='blog/detail.html', context={'posts':posts})