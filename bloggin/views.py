from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Blogpost, Comment, Topic


def username(request):
    return HttpResponse("here will be username")


def get_blog(request, slug):
    blogpost_one = get_object_or_404(Blogpost, slug=slug)
    comments = Comment.objects.filter(blogpost=blogpost_one)
    topic = Topic.objects.filter(blogpost=blogpost_one)[0]

    return render(request, "detailedBlog.html", {"blogpost_one": blogpost_one, "comments": comments,
                  'topic': topic})


def blogs(request):
    blogposts = Blogpost.objects.all()
    all_topics = Topic.objects.all()
    return render(request, "index.html", {"blogposts": blogposts, 'all_topics': all_topics})


def about(request):
    return HttpResponse("here will be about")


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





