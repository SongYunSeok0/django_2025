from django import forms
from blog.models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'category', 'title', 'content', 'uploaded_image', 'uploaded_file']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'comment']

