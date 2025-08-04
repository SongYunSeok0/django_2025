from django.shortcuts import render, redirect
from .models import Post, Category, Comment
from .forms import PostForm, CommentForm
# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-pk')
    categories = Category.objects.all()
    return render(request, template_name='blog/index.html', 
                  context={'posts':posts, 'categories':categories}
                  )

def category(request, slug):
    categories = Category.objects.all()
    if slug =='no_category':
        # 미분류인 경우
        posts = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        posts = Post.objects.filter(category=category)
    return render(request, template_name='blog/index.html',
                  context={'posts':posts, 'categories':categories}
                  )

def detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    commentform = CommentForm() 
    categories = Category.objects.all()
    return render(request, template_name='blog/detail.html',
                  context={'post':post,'commentform':commentform, 'comments':comments, 'categories':categories, }
                  )

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
                           'categories':categories}
                           )

#/blog/<int:pk>/delete
def delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('/blog/')

#/blog/<int:pk>/update
def update(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        postform = PostForm(request.POST, request.FILES, instance=post)
        if postform.is_valid():
            postform.save()
            return redirect('/blog/')
    else:
        postform = PostForm(instance=post)

    return render(request, template_name="blog/postupdateform.html",
                  context={'postform':postform}
                  )

def createComment(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        # 제출 버튼을 누른경우
        commentform = CommentForm(request.POST)
        if commentform.is_valid():
            # 정상값인 경우
            comment = commentform.save(commit=False)
            comment.post = post
            commentform.save()
            return redirect(f'/blog/{post.pk}')
    else:
        commentform = CommentForm()

def updateComment(request, pk):
    comment = Comment.objects.get(pk=pk)
    post = comment.post
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect(f'/blog/{post.pk}/')
    else:
        form = CommentForm(instance=comment)

    return render(request, "blog/updatecommentform.html", {
        'commentform': form,
        'post': post
    })

def deleteComment(request, pk):
    comment = Comment.objects.get(pk=pk)
    comment.delete()
    return redirect(f'/blog/{comment.post.pk}/') 