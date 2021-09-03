from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,UserPostListView
from . import views


app_name = 'posts'


urlpatterns=[
    path('',PostListView.as_view(), name="index"),
    path('user/<str:username>',UserPostListView.as_view(), name="user-posts"),
    path('detail/<int:pk>/',PostDetailView.as_view(), name="detail"),
    path('create/',PostCreateView.as_view(), name="create"),
    path('edit/<int:pk>/',PostUpdateView.as_view(), name="edit"),
    path('delete/<int:pk>/',PostDeleteView.as_view(), name="delete"),
]