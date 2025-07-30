from django.shortcuts import render
from .models import Post
# Create your views here.

def landing(request):
    posts = Post.objects.all()
    return render(request, template_name='single_pages/landing.html', context={'posts':posts})