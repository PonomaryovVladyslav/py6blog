from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Blogpost, Comment, Topic, Author
from .forms import BlogpostForm, TopicForm, BlogpostModelForm, TopicModelForm, CommentModelForm, CommentForm

def get_blog(request, slug):
    all_topics = Topic.objects.all()
    blogpost_one = get_object_or_404(Blogpost, slug=slug)
    comments = Comment.objects.filter(blogpost=blogpost_one)
    topic = Topic.objects.filter(blogpost=blogpost_one)[0]
    return render(request, "detailedBlog.html", {"blogpost_one": blogpost_one, "comments": comments,
                  'topic': topic,  'all_topics': all_topics})

def blogs(request):
    blogposts = Blogpost.objects.all()
    all_topics = Topic.objects.all()
    if 'search' in request.GET:
        searching_text = request.GET["search"]
        blogposts_search = Blogpost.objects.filter(title_blogpost__icontains =request.GET["search"])
        blogposts_search_text = Blogpost.objects.filter(text_blogpost__icontains=request.GET["search"])

        print('blogposts_search = ', blogposts_search)
        return render(request, "search.html",  context= {"blogposts_search": blogposts_search,
                "searching_text": searching_text, 'blogposts_search_text': blogposts_search_text})
    # return render(request, 'search.html')
    return render(request, "index.html",
                  {"blogposts": blogposts, "all_topics": all_topics})

def by_topics(request):
    all_topics = Topic.objects.all()
    return render(request, "by_topics.html", { "all_topics": all_topics})

def get_topic(request, slug):
    topic = get_object_or_404(Topic, slug=slug)
    all_blogposts = Blogpost.objects.all()

    print('topic', topic)
    return render(request, "post_in_topic.html", {"topic": topic, 'all_blogposts': all_blogposts })


def search(request):
    print('search', search)
    # print('hi')
    # if request.method == "POST":
    #     print('search = ', search)
    if 'search' in request.GET:
        print('hi')
        searching_text = request.GET["search"]
        print('searching_text = ', searching_text)
        blogposts_search = Blogpost.objects.filter(title__blogpost__iregex =request.GET["search"])
        print('blogposts_search = ', blogposts_search)
        return render(request, "search.html",  context= {"blogposts_search": blogposts_search,
                                                             "searching_text": searching_text})
    return render(request, 'search.html')

def create(request):
    if request.method == 'POST':
        form = BlogpostModelForm(request.POST)
        if form.is_valid():
            blog = form.save()
            # author, _ = Author.objects.get_or_create(name=form.cleaned_data['author_blogpost'])
            # topic, _ = Topic.objects.get_or_create(title_topic=form.cleaned_data['topics'])
            #
            # blog = Blogpost.objects.create(
            #     title_blogpost=form.cleaned_data['title_blogpost'],
            #     text_blogpost=form.cleaned_data['text_blogpost'],
            #     date_of_public_blogpost=form.cleaned_data['date_of_public_blogpost'],
            #     author_blogpost=author,
            #     )
            # blog.topics.add(topic)
            return HttpResponse(f"we are creating a new blog {blog}")
        return render(request, 'createBlog.html', context={'form': form})
    form = BlogpostForm()
    return render(request, 'createBlog.html', context={'form': form})

def topic_create(request):
    if request.method == 'POST':
        form_topic = TopicModelForm(request.POST)
        if form_topic.is_valid():
            topic = form_topic.save()
            return HttpResponse(f"we are creating a new blog {topic}")
        return render(request, 'createTopic.html', context={'form_topic': form_topic})
    form_topic = TopicForm()
    return render(request, 'createTopic.html', context={'form_topic': form_topic})

def create_comment(request):
    if request.method == 'POST':
        form_comment = CommentModelForm(request.POST)
        if form_comment.is_valid():
            comment = form_comment.save()
            return HttpResponse(f"we are creating a new blog {comment}")
        return render(request, 'create_comment.html', context={'form_comment': form_comment})
    form_comment = CommentForm()
    return render(request, 'create_comment.html', context={'form_comment': form_comment})


# def topic_for_topics(request):
#     all_topics = Topic.objects.all()
#     return render(request, "base.html", {'all_topics': all_topics})




def about(request):
    return HttpResponse("here will be about")


def comment(request, txt):
    return HttpResponse(f"here will be comment, address {txt}")

def update(request, txt):
    return HttpResponse(f"here will be update, address {txt}")


def delete(request,txt):
    return HttpResponse(f"here will be delete, address {txt}")


def index(request):
    return render(request, 'index.html')



def username(request):
    return HttpResponse("here will be username")
