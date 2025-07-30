from django.shortcuts import render
from .models import Outer, Top, Bottom, Shoes, Main
# Create your views here.

def main(request):
    posts = Main.objects.all()
    return render(request, template_name='shop/main.html', context={'posts':posts})

def outer(request):
    posts = Outer.objects.all()
    return render(request, template_name='shop/outer.html', context={'posts':posts})

def top(request):
    posts = Top.objects.all()
    return render(request, template_name='shop/top.html', context={'posts':posts})

def bottom(request):
    posts = Bottom.objects.all()
    return render(request, template_name='shop/bottom.html', context={'posts':posts})

def shoes(request):
    posts = Shoes.objects.all()
    return render(request, template_name='shop/shoes.html', context={'posts':posts})