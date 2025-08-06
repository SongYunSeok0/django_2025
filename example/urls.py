from django.urls import path
from . import views

urlpatterns = [
    path('',views.example, name='example'),
    path('helloAPI/', views.helloAPI, name='helloAPI'),
    path('hiAPI/', views.hiAPI, name='hiAPI'),
    path('postAPI/<int:pk>/', views.postAPI, name='postAPI'),
    path('blogAPI/', views.blogAPI, name='blogAPI'),
    path('commentAPI/<int:post_id>/', views.commentAPI, name='commentAPI'),
    path('commentAPI/', views.comment_html_page, name='commentAPI'),         # HTML 페이지 보여주는 뷰
    path('commentAPI/data/', views.commentAPI_data, name='commentAPI_data'),
]
