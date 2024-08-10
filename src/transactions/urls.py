from django.urls import path
from transactions.views import TransactionListView

urlpatterns = [
    path('transactions/', TransactionListView.as_view()),
]