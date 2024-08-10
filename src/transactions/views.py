from rest_framework import generics

from transactions.models import Transaction
from transactions.serializers import TransactionSerializer


class TransactionListView(generics.ListAPIView):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
