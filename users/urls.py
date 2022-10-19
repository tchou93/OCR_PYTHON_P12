from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from users.views import UserView

user_list = UserView.as_view({'get': 'list'})
user_detail = UserView.as_view({'get': 'retrieve'})

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/',TokenRefreshView.as_view(), name='token-refresh'),
    path('users/',user_list, name='users-list'),
    path('users/<int:pk>/',user_detail, name='user-detail'),
]
