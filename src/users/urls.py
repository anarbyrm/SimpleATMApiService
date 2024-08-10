from django.urls import path
from .views import (UserCreateView,
                    UserLoginView,
                    UserDestroyView)

urlpatterns = [
    path("users", UserCreateView.as_view()),
    path("users/token", UserLoginView.as_view()),
    path('users/<str:username>', UserDestroyView.as_view()),
]