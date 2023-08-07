from rest_framework import serializers

from .models import Blogpost, Topic, Author, Comment
# from registration.serializers import UserModelSerializer


class BlogpostModelSerializer(serializers.ModelSerializer):
    # author = UserModelSerializer()
    topics = serializers.CharField(read_only=True, source='topics.slug')

    class Meta:
        model = Blogpost
        fields = ['id', 'slug', 'title', 'text',  'topics']

    def create(self, validated_data):
         return Blogpost.objects.create(**validated_data)


class TopicModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = ['id', 'slug', 'title', 'text']


class CommentModelSerializer(serializers.ModelSerializer):
    # blogpost = serializers.IntegerField(source='blogpost.id', read_only=True)
    # blogpost_id = serializers.IntegerField(source='blogpost.id', read_only=True)

    class Meta:
        model = Comment

        fields = ['id', 'text', 'blogpost', 'author']
