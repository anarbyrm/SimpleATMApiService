from rest_framework import generics, views, authentication
from accounts.models import Account
from .serializers import AccountSerializer


class AccountRetrieveCreateView(generics.RetrieveAPIView,
                                generics. CreateAPIView,
                                views.APIView):
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = AccountSerializer
    queryset = Account.objects.all()

    def get_object(self):
        current_user = self.request.user
        user_accounts = self.get_queryset().filter(user=current_user)
        return user_accounts.first() if user_accounts.exists() else None
