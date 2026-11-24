from django.urls import path
from . import views

urlpatterns = [
    # Register Login URLs
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    # Blog API URLs
    path('blog_list_create/', views.blog_list_create, name='blog_list_create'),
    path('blog_detail/', views.blog_detail, name='blog_detail'),
]