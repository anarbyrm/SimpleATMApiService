from rest_framework import authentication, generics, permissions, status, views
from rest_framework.response import Response
from accounts.models import Account
from transactions.models import Transaction, TransactionType
from .serializers import (AccountSerializer,
                          AccountBalanceTopUpSerializer,
                          AccountBalanceWithdrawSerializer)
from .utils import divide_money_into_units


class AccountRetrieveCreateView(generics.RetrieveAPIView,
                                generics. CreateAPIView,
                                views.APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AccountSerializer
    queryset = Account.objects.all()

    def get_object(self):
        current_user = self.request.user
        user_accounts = self.get_queryset().filter(user=current_user)
        return user_accounts.first() if user_accounts.exists() else None


class AccountBalanceTopUpView(generics.UpdateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Account.objects.all()

    def patch(self, request):
        account = self.get_object()
        serializer = AccountBalanceTopUpSerializer(account, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response({
                "success": False,
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        
        updated_account = serializer.save()
        topped_up_amount = serializer.validated_data["top_up_amount"]

        Transaction.objects.create(amount=topped_up_amount,
                                   account=account,
                                   transaction_type=TransactionType.TOPPED_UP.value)
        return Response({
            "success": True,
            "data": {
                "topped_up_amount": topped_up_amount,
                "balance": updated_account.balance
            }
        }, status=status.HTTP_200_OK)

    def get_object(self):
        current_user = self.request.user
        accounts = Account.objects.filter(user=current_user)
        return accounts.first() if accounts.exists() else None


class AccountBalanceWithdrawView(generics.UpdateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Account.objects.all()

    def get_object(self):
        current_user = self.request.user
        accounts = Account.objects.filter(user=current_user)
        return accounts.first() if accounts.exists() else None

    def patch(self, request):
        account = self.get_object()
        serializer = AccountBalanceWithdrawSerializer(account, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response({
                "success": False,
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        updated_account = serializer.save()
        withdrawn_amount = serializer.validated_data["withdraw_amount"]
        unit_dict = divide_money_into_units(withdrawn_amount)
        
        Transaction.objects.create(amount=withdrawn_amount,
                                   account=account,
                                   transaction_type=TransactionType.WITHDRAWN.value)

        return Response({
            "success": True,
            "data": {
                "withdrawn_amount": {
                    "total": withdrawn_amount,
                    "in_pieces": unit_dict
                },
                "balance": updated_account.balance
            }
        })
