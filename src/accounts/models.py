from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Account(models.Model):
    balance = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Account: {self.user.email}"
