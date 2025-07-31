from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-pk')
    return render(request, template_name='shop/index.html', context={'posts':posts})

def detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, template_name='shop/detail.html', context={'post':post})

def create(request):
    if request.method == "POST":
        # 제출 버튼을 누른경우
        postform = PostForm(request.POST, request.FILES)
        if postform.is_valid():
            # 정상값인 경우
            postform.save()
            return redirect('/shop/')
    else: # get
        postform = PostForm()
    return render(request, template_name='shop/postform.html',
                  context={'postform':postform})
