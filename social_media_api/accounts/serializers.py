from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

class RegisterSerializer(serializers.ModelSerializer):
    # Explicitly define 'username' and 'password' fields using CharField
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'email')

    def create(self, validated_data):
        # Create user with validated data
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        # Create a token for the new user
        Token.objects.create(user=user)
        return user
