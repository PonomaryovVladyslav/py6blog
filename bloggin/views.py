from urllib import request

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView
from .models import Blogpost, Comment, Topic, Author
from .forms import BlogpostModelForm, TopicModelForm, CommentModelForm


class BlogDetailView(DetailView):
    model = Blogpost
    template_name = 'detailed_blog.html'
    context_object_name = "blog"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(blogpost=self.object).order_by('updated_at')
        context['form'] = CommentModelForm
        return context

class PostsListView(ListView):
    model = Blogpost
    template_name = "index.html"
    context_object_name = 'blogs'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('updated_at')
        if "search" in self.request.GET:
            return queryset.filter(text__icontains=self.request.GET["search"])
        return queryset


class TopicListView(ListView):
    model = Topic
    template_name = "by_topics.html"
    context_object_name = 'topics'

    def get_queryset(self):
        return super().get_queryset().order_by('updated_at')


class PostsInTopicListView(DetailView):
    model = Topic
    template_name = "post_in_topic.html"
    context_object_name = 'topic'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Blogpost.objects.filter(topics = self.object).order_by('updated_at')
        context['posts'] = posts
        return context


class PostCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = BlogpostModelForm
    template_name =  'create_blog.html'
    success_url = reverse_lazy('blogs')
    login_url = '/login/'
    success_message = "Blogpost %(title)s is created"

    def form_valid(self, form):
        self.obj = form.save(commit=False)
        self.obj.author = self.request.user
        self.obj.save()
        return super().form_valid(form=form)


class TopicCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = TopicModelForm
    template_name = 'create_topic.html'
    success_url = reverse_lazy('by_topics')
    login_url = '/login/'
    success_message = "Topic %(title)s is created"

    def form_valid(self, form):
        self.obj = form.save(commit=False)
        self.obj.author = self.request.user
        self.obj.save()
        return super().form_valid(form=form)


class CommentCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = CommentModelForm
    success_url = reverse_lazy('blogs')
    login_url = '/login/'
    success_message = "Comment is created"

    def form_valid(self, form, **kwargs):
        self.obj = form.save(commit=False)
        self.obj.author = self.request.user
        self.obj.blogpost = get_object_or_404(Blogpost, slug= self.kwargs.get("slug"))
        self.obj.save()
        return super().form_valid(form=form)


class BlogUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Blogpost
    template_name = 'post_edit.html'
    fields = ['title', 'text', 'topics']
    success_url = reverse_lazy('blogs')
    login_url = '/login/'
    success_message = "Blog %(title)s is updated"

class TopicUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Topic
    template_name = 'topic_edit.html'
    fields = ['title', 'text']
    success_url = reverse_lazy('by_topics')
    login_url = '/login/'
    success_message = "Topic %(title)s is updated"

class BlogDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Blogpost
    context_object_name = 'post'
    template_name = 'post_delete.html'
    success_url = reverse_lazy('blogs')
    login_url = '/login/'
    success_message = "Blog is deleted"

class TopicDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Topic
    context_object_name = 'topic'
    template_name = 'topic_delete.html'
    success_url = reverse_lazy('by_topics')
    login_url = '/login/'
    success_message = "Topic is deleted"
class AddLike(LoginRequiredMixin, View):
    def post(self,  request,  pk, *args, **kwargs):
        author = request.user
        post = Blogpost.objects.get(id=pk)
        if author.likes.filter(id=pk).exists():
            author.likes.remove(post)
        else:
            author.likes.add(post)
            if author.dislikes.filter(id=pk).exists():
                author.dislikes.remove(post)

        next = request.POST.get('next', 'http://127.0.0.1:8000/get_blog/<id=pk>')
        return HttpResponseRedirect(next)



class AddDislike(LoginRequiredMixin, View):
    def post(self,  request,  pk, *args, **kwargs):
        author = request.user
        post = Blogpost.objects.get(id=pk)
        if author.dislikes.filter(id=pk).exists():
            author.dislikes.remove(post)
        else:
            author.dislikes.add(post)
            if author.likes.filter(id=pk).exists():
                author.likes.remove(post)
        next = request.POST.get('next', 'http://127.0.0.1:8000/get_blog/<id=pk>')
        return HttpResponseRedirect(next)


class AddFollower(LoginRequiredMixin, View):
    def post(self,  request,  topic_id, *args, **kwargs):
        author = request.user
        topic = Topic.objects.get(id=topic_id)
        if author.followers.filter(id=topic_id).exists():
            author.followers.remove(topic)
        else:
            author.followers.add(topic)
        next = request.POST.get('next', 'http://127.0.0.1:8000/by_topics/')
        return HttpResponseRedirect(next)


class About(TemplateView):
        template_name = "about.html"
