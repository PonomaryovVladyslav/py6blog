from django import forms
from .models import Blogpost, Topic, Author, Comment

class BlogpostModelForm(forms.ModelForm):
    class Meta:
        model = Blogpost
        fields = ['slug', 'title', 'text',  'topics']


class TopicModelForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['slug', 'title', 'text']


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        # тільки тест коментаря
        fields = ['text', 'blogpost']