from django.urls import path
from .views import username, change_password, register, user_login, logout_view

urlpatterns = [
    path('profile/<str:username>/', username),
    path('change_password/', change_password),
    path('register/', register, name='register'),
    path('login/', user_login, name='user_login'),
    path('logout_view/', logout_view, name='logout_view'),
]

