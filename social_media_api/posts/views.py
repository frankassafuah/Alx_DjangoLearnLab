from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from .models import Post, Like
from notifications.models import Notification

class LikeViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def like_post(self, request, pk=None):
        # Fetch the post object safely using get_object_or_404
        post = get_object_or_404(Post, pk=pk)

        # Create or retrieve the Like object
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if created:
            # Create a notification if the post is liked for the first time
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked',
                target=post
            )
            return Response({'status': 'liked'}, status=status.HTTP_201_CREATED)
        
        return Response({'status': 'already liked'}, status=status.HTTP_400_BAD_REQUEST)

    def unlike_post(self, request, pk=None):
        # Fetch the post object safely using get_object_or_404
        post = get_object_or_404(Post, pk=pk)

        try:
            # Attempt to retrieve the Like object
            like = Like.objects.get(user=request.user, post=post)
            like.delete()  # Remove the like if it exists
            return Response({'status': 'unliked'}, status=status.HTTP_204_NO_CONTENT)
        except Like.DoesNotExist:
            return Response({'status': 'not liked'}, status=status.HTTP_400_BAD_REQUEST)
