from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-pk')
    return render(request, template_name='blog/index.html', context={'posts':posts})

def detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, template_name='blog/detail.html', context={'post':post})

def create(request):
    if request.method == "POST":
        # 제출 버튼을 누른경우
        postform = PostForm(request.POST, request.FILES)
        if postform.is_valid():
            # 정상값인 경우
            post1 = postform.save(commit=False)
            post1.title = post1.title + "홍길동 만세"
            postform.save()
            return redirect('/blog/')
    else: # get
        postform = PostForm()
    return render(request, template_name='blog/postform.html',
                  context={'postform':postform})

def createfake(request):
    post = Post()
    post.title = "새싹 용산구"
    post.content = "나진상가 3층"
    post.save()
    return redirect('/blog/')