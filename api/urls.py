from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from .users import views as userViews
urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', userViews.RegisterView.as_view(), name='register'),
    path('logout/', userViews.LogoutView.as_view(), name='logout'),
]
