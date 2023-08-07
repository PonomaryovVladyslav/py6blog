from rest_framework import filters
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny

from .models import Blogpost
from .permissions import IsAuthorOrReadOnly, IsAdminOrReadOnly
from .serializers import BlogpostModelSerializer


# class AuthorFiltr(filters.SearchFilter):
#
#     def filter_queryset(self, request, queryset, view):
#         if request.query_params.get('mine') is not None:
#             return queryset.filter(**{self.field: request.user})
#         return queryset

    # search_fields = ['text', 'title']


    #
    # """
    # Filter that only allows users to see their own objects if the ?mine
    # query param is set.
    # """
    #
    # field = 'author'
    # query_param = 'mine'
    #
    # def filter_queryset(self, request, queryset, view):
    #     if request.query_params.get('mine') is not None:
    #         return queryset.filter(**{self.field: request.user})
    #     return queryset