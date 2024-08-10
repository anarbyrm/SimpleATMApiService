from django.urls import path
from .views import AccountRetrieveCreateView

urlpatterns = [
    path("accounts/", AccountRetrieveCreateView.as_view()),
]