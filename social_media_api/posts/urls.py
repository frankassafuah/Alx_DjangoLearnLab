from django.urls import path
from .views import PostListCreateView, PostDetailView
from .views import FeedView  # Import your feed view

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('feed/', FeedView.as_view(), name='feed'),  # Add the feed endpoint

]
