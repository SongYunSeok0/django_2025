from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:pk>/', views.detail, name="detail"),
    path('create/', views.create, name="blogcreate"),
    path('category/<slug>/', views.category, name='category'),
    path('<int:pk>/delete/', views.delete, name="delete"),
    path('<int:pk>/update/', views.update, name="update"),
    path('<int:pk>/createcomment', views.createComment, name="createcomment"),
    path('<int:pk>/updatecomment', views.updateComment, name="updatecomment"),
    path('<int:pk>/deletecomment', views.deleteComment, name="deletecomment"),
]