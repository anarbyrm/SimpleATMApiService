from rest_framework import authentication, generics, permissions
from transactions.models import Transaction
from transactions.serializers import TransactionSerializer


class TransactionListCreateView(generics.ListCreateAPIView):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [authentication.TokenAuthentication]


class TransactionRetreiveDestroyUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [authentication.TokenAuthentication]
