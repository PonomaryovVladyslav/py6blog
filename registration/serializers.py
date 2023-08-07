from rest_framework import serializers
from django.contrib.auth.models import User

from bloggin.serializers import BlogpostModelSerializer


class UserModelSerializer(serializers.ModelSerializer):
    blogpost =  BlogpostModelSerializer(many=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'blogpost']