from django.http import HttpResponse
from django.shortcuts import render


def username(request, username):
    return HttpResponse(f"here will be username {username}")


def change_password(request):
    return HttpResponse("here will be change_password")


def register(request):
    return render(request, 'registration.html')


def login(request):
    return render(request, 'login.html')


def logout(request):
    return HttpResponse("here will be logout")


