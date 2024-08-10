from django.contrib.auth import get_user_model
from rest_framework import authentication, generics, status, views, permissions
from rest_framework.response import Response

from .serializers import UserCreateSerializer, UserTokenSerializer

User = get_user_model()


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()


class UserLoginView(views.APIView):
    def post(self, request):
        serializer = UserTokenSerializer(data=request.data)
        if serializer.is_valid():
            token = serializer.create_access_token()
            return Response({"token": token}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDestroyView(generics.DestroyAPIView):
    queryset = User
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [authentication.TokenAuthentication]
    lookup_field = 'username'
