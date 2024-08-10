from django.urls import path
from .views import (UserCreateView,
                    UserLoginView)

urlpatterns = [
    path("users/", UserCreateView.as_view()),
    path("users/token", UserLoginView.as_view()),
]