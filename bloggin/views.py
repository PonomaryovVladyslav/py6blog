from django.http import HttpResponse
from django.shortcuts import render



def username(request):
    return HttpResponse("here will be username")


def blogs(request):
    return render(request, 'index.html')


def about(request):
    return HttpResponse("here will be about")


def oneblog(request):
    return render(request, 'detailedBlog.html')


def comment(request, txt):
    return HttpResponse(f"here will be comment, address {txt}")


def create(request):
    return render(request, 'createBlog.html')


def update(request, txt):
    return HttpResponse(f"here will be update, address {txt}")


def delete(request,txt):
    return HttpResponse(f"here will be delete, address {txt}")


def index(request):
    return render(request, 'index.html')
