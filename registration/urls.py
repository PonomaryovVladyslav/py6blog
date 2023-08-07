from django.urls import path
from .views import Logout, Login, Register, PasswordChange, ProfileView

urlpatterns = [
    path('profile/<str:username>/', ProfileView.as_view(), name = 'profile'),
    path('password_change/', PasswordChange.as_view(), name = 'password_change'),
    path('register/', Register.as_view(), name='register'),
    path('login/',  Login.as_view(), name='user_login'),
    path('logout/', Logout.as_view(), name='logout'),
]

