from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

# from .filters import AuthorFiltr
from .models import Topic, Blogpost, Comment
from .permissions import IsAuthorOrReadOnly, IsAdminOrReadOnly
from .serializers import TopicModelSerializer, CommentModelSerializer, BlogpostModelSerializer
from registration.serializers import UserModelSerializer


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicModelSerializer
    permission_classes = (IsAuthorOrReadOnly, IsAdminOrReadOnly)


class BlogpostViewSet(viewsets.ModelViewSet):
    queryset = Blogpost.objects.all()
    serializer_class = BlogpostModelSerializer
    permission_classes = (AllowAny, IsAuthorOrReadOnly, IsAdminOrReadOnly)
    # filter_backends = [SearchFilter, OrderingFilter]
    # search_fields = ['text', 'title']

    # def get_queryset(self, *args, **kwargs):
    #     queryset_list = Blogpost.objects.all()
    #     query = self.request.GET.get("search")
    #     if query:
    #         queryset_list = queryset_list.filter(
    #             Q(title__icontains=query) |
    #             Q(text__icontains=query)
    #         ).distinct()
    #     return queryset_list


class GroupViewSet(ModelViewSet):
    queryset = Blogpost.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    permission_classes = (AllowAny, IsAuthorOrReadOnly, IsAdminOrReadOnly)
    serializer_class = BlogpostModelSerializer
    search_fields = ['text', 'title']


class AuthorViewSet(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = (AllowAny, IsAuthorOrReadOnly, IsAdminOrReadOnly)
    serializer_class = UserModelSerializer
    filter_backends = [SearchFilter]
    search_fields = ['username']


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentModelSerializer
    permission_classes = (IsAuthorOrReadOnly, IsAdminOrReadOnly)
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['content', 'author__username']
    odering_fields = ['content', 'author']