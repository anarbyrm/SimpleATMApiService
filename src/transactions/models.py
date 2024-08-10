from django.db import models

from accounts.models import Account


class Transaction(models.Model):
    amount = models.IntegerField()
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction for {self.account.user.email} account with amount of {self.amount}"
