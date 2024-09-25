from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import authenticate
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth import get_user_model

from django.shortcuts import get_object_or_404
from .models import CustomUser  # Assuming CustomUser is your user model
from .serializers import UserSerializer  # Assuming you have a serializer for CustomUser
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.create(user=user)
            return Response({
                'token': token.key,
                'user': UserSerializer(user).data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user': UserSerializer(user).data
            })
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


# View to follow a user
class FollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]  # User must be authenticated
    queryset = CustomUser.objects.all()  # Access to all users
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        user_to_follow = get_object_or_404(CustomUser, id=kwargs['pk'])  # Get the user to follow
        if user_to_follow == request.user:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        # Add user_to_follow to the authenticated user's following list
        request.user.following.add(user_to_follow)
        return Response({"detail": f"You are now following {user_to_follow.username}."}, status=status.HTTP_200_OK)

# View to unfollow a user
class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]  # User must be authenticated
    queryset = CustomUser.objects.all()  # Access to all users
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        user_to_unfollow = get_object_or_404(CustomUser, id=kwargs['pk'])  # Get the user to unfollow
        if user_to_unfollow == request.user:
            return Response({"detail": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        # Remove user_to_unfollow from the authenticated user's following list
        request.user.following.remove(user_to_unfollow)
        return Response({"detail": f"You have unfollowed {user_to_unfollow.username}."}, status=status.HTTP_200_OK)