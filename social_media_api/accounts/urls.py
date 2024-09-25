from django.urls import path
from .views import RegisterView, LoginView
from .views import UserFeedView
from .views import follow_user, unfollow_user  # Import your follow and unfollow views


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('follow/<int:user_id>/', follow_user, name='follow-user'),
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow-user'),
    path('feed/', UserFeedView.as_view(), name='user-feed'),
]
