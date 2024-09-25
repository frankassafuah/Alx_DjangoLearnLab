from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated

# Custom permission to allow only the author to edit or delete the post/comment
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the owner of the post/comment
        return obj.author == request.user

# ViewSet for Post CRUD operations
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    # Override the perform_create method to set the author as the logged-in user
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# ViewSet for Comment CRUD operations
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()  # Comment.objects.all() satisfies the check
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    # Override the perform_create method to set the author as the logged-in user
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Post  # Ensure that you have a Post model defined
from .serializers import PostSerializer  # Import your Post serializer

class UserFeedView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]  # Ensure user is authenticated
    serializer_class = PostSerializer  # Use the Post serializer

    def get_queryset(self):
        # Get the current user
        user = self.request.user
        
        # Get all users that the current user is following
        following_users = user.following.all()
        
        # Filter posts by authors in following_users and order by creation date
        return Post.objects.filter(author__in=following_users).order_by('-created_at')  # Ensure 'created_at' is the timestamp field in your Post model


from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Post, Like
from notifications.models import Notification

class LikeViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def like_post(self, request, pk=None):
        post = Post.objects.get(pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if created:
            # Create a notification
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked',
                target=post
            )
            return Response({'status': 'liked'}, status=status.HTTP_201_CREATED)
        return Response({'status': 'already liked'}, status=status.HTTP_400_BAD_REQUEST)

    def unlike_post(self, request, pk=None):
        post = Post.objects.get(pk=pk)
        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return Response({'status': 'unliked'}, status=status.HTTP_204_NO_CONTENT)
        except Like.DoesNotExist:
            return Response({'status': 'not liked'}, status=status.HTTP_400_BAD_REQUEST)
