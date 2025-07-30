from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('outer/', views.outer),
    path('top/', views.top),
    path('bottom/', views.bottom),
    path('shoes/', views.shoes),
]