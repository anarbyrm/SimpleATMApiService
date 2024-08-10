from enum import Enum
from django.db import models

from accounts.models import Account

class TransactionType(Enum):
    TOPPED_UP = "topped up"
    WITHDRAWN = "withdrawn"


class Transaction(models.Model):
    amount = models.IntegerField()
    additional_info = models.TextField()
    transaction_type = models.CharField(
        max_length=10,
        choices=[(transaction_type.value, transaction_type.name) for transaction_type in TransactionType]
    )
    account = models.ForeignKey(
        Account,
        on_delete=models.SET_NULL, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction for {self.account.user.email} account with amount of {self.amount}"
