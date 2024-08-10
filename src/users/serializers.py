from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from rest_framework.authtoken.models import Token

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

    def get_authenticated_user(self):
        return User.objects.filter(username=self.validated_data["username"]).first() if self.is_valid() else None

    def create_access_token(self):
        user = self.get_authenticated_user()
        token, _is_created = Token.objects.get_or_create(user=user)
        return token.key
