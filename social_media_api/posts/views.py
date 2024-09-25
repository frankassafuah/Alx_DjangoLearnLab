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
