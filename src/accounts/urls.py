from django.urls import path
from .views import (AccountRetrieveCreateView,
                    AccountBalanceTopUpView,
                    AccountBalanceWithdrawView,
                    AccountDestroyView)

urlpatterns = [
    path("accounts", AccountRetrieveCreateView.as_view()),
    path("accounts/top-up", AccountBalanceTopUpView.as_view()),
    path("accounts/withdraw", AccountBalanceWithdrawView.as_view()),
    path("accounts/<str:username>", AccountDestroyView.as_view()),
]