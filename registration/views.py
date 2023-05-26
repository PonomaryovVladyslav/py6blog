from django.http import HttpResponse


def username(request, username):
    return HttpResponse(f"here will be username {username}")


def change_password(request):
    return HttpResponse("here will be change_password")


def register(request):
    return HttpResponse("here will be register")


def login(request):
    return HttpResponse("here will be login")


def logout(request):
    return HttpResponse("here will be logout")


