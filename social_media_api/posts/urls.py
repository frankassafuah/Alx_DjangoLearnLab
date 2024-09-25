from django.urls import path
from .views import PostListCreateView, PostDetailView
from .views import FeedView  # Import your feed view
from .views import LikeViewSet

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('feed/', FeedView.as_view(), name='feed'),  # Add the feed endpoint
    path('posts/<int:pk>/like/', LikeViewSet.as_view({'post': 'like_post'}), name='like-post'),
    path('posts/<int:pk>/unlike/', LikeViewSet.as_view({'post': 'unlike_post'}), name='unlike-post'),

]
