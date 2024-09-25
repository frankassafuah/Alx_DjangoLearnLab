from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token  # For token management

class RegisterSerializer(serializers.ModelSerializer):
    # Ensure the password field is explicitly defined as a CharField
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'email')

    def create(self, validated_data):
        # Create user using the validated data
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        # Generate a token for the newly created user
        Token.objects.create(user=user)
        return user
