from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:pk>/', views.detail, name="detail"),
    path('create/', views.create, name="blogcreate"),
    path('createfake/', views.createfake, name="fakeblogcreate"),
]