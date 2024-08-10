from django.urls import path
from transactions.views import TransactionListCreateView, TransactionRetreiveDestroyUpdateView

urlpatterns = [
    path('transactions', TransactionListCreateView.as_view()),
    path('transactions/<int:id>', TransactionRetreiveDestroyUpdateView.as_view()),
]