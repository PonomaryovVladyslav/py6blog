from django.urls import path
from .views import searching

urlpatterns = [
    path('searching/', searching, name='searching')
]