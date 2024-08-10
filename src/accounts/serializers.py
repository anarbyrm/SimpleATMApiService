from rest_framework import serializers
from accounts.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "balance",
            "user"
        ]
        read_only_fields = [
            "user"
        ]

    def create(self, validated_data):
        current_user = self.context["request"].user
        user_account = Account.objects.filter(user=current_user)

        if user_account.exists():
            return user_account.first()
        
        validated_data["user"] = current_user
        return super().create(validated_data)
