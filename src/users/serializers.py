from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'password',
        ]
    
    def create(self, validated_data):
        return User.objects.create_user(email=validated_data["email"],
                                            username=validated_data["username"],
                                            password=validated_data["password"])


class UserTokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(max_length=125)

    def is_valid(self):
        if not super().is_valid():
            return False
        
        username = self.validated_data["username"]
        user_password = self.validated_data["password"]

        user = authenticate(username=username, password=user_password)
        if not user:
            raise serializers.ValidationError("Email or password is not correct")
        
        return True

    def create_access_token(self):
        # imaginary access token for development
        token = "generated token"
        return token
