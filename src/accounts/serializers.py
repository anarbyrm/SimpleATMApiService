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


class AccountBalanceTopUpSerializer(serializers.ModelSerializer):
    top_up_amount = serializers.IntegerField(min_value=1)

    class Meta:
        model = Account
        fields = [
            "balance",
            "top_up_amount"
        ]
        read_only_fields = ["balance"]

    def update(self, instance, validated_data):
        top_up_amount = validated_data.pop("top_up_amount", None)
        if top_up_amount:
            instance.balance += top_up_amount
            instance.save()
        return instance


class AccountBalanceWithdrawSerializer(serializers.ModelSerializer):
    withdraw_amount = serializers.IntegerField(min_value=1)

    class Meta:
        model = Account
        fields = [
            "balance",
            "withdraw_amount"
        ]
        read_only_fields = ["balance"]

    def validate(self, attrs):
        amount = attrs["withdraw_amount"]
        if amount > self.instance.balance:
            raise serializers.ValidationError("Withdraw amount can't be more than balance")
        return attrs

    def update(self, instance, validated_data):
        withdraw_amount = validated_data.pop("withdraw_amount", None)
        if withdraw_amount:
            instance.balance -= withdraw_amount
            instance.save()
        return instance