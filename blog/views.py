from django.shortcuts import render, redirect
from .models import Post, Category
from .forms import PostForm
# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-pk')
    categories = Category.objects.all()
    return render(request, template_name='blog/index.html', context={'posts':posts,
                                                                     'categories':categories})

def category(request, slug):
    categories = Category.objects.all()
    if slug =='no_category':
        # 미분류인 경우
        posts = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        posts = Post.objects.filter(category=category)
    return render(request, template_name='blog/index.html',context={'posts':posts,
                                                                    'categories':categories})

def detail(request, pk):
    post = Post.objects.get(pk=pk)
    categories = Category.objects.all()
    return render(request, template_name='blog/detail.html', context={'post':post
                                                                      ,'categories':categories})

def create(request):
    categories = Category.objects.all()
    if request.method == "POST":
        # 제출 버튼을 누른경우
        postform = PostForm(request.POST, request.FILES)
        if postform.is_valid():
            # 정상값인 경우
            post1 = postform.save(commit=False)
            post1.title = post1.title
            postform.save()
            return redirect('/blog/')
    else: # get
        postform = PostForm()
    return render(request, template_name='blog/postform.html',
                  context={'postform':postform,
                           'categories':categories})

def createfake(request):
    post = Post()
    post.title = "새싹 용산구"
    post.content = "나진상가 3층"
    post.save()
    return redirect('/blog/')