from django.urls import path
from .views import username, change_password, register, login, logout

urlpatterns = [
    path('profile/<str:username>/', username),
    path('change_password/', change_password),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout),
]

