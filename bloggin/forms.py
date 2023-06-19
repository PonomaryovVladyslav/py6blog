from django import forms
from .models import Blogpost, Topic, Author, Comment
import datetime



class BlogpostForm(forms.Form):
    title_blogpost = forms.CharField(max_length=128, required=True)
    text_blogpost = forms.CharField(max_length=99999999, required=True, widget=forms.Textarea)
    date_of_public_blogpost = forms.DateTimeField(initial=datetime.datetime.now())
    author_blogpost = forms.ModelChoiceField(queryset=Author.objects.all())
    topics = forms.ModelChoiceField(queryset=Topic.objects.all())
    

class BlogpostModelForm(forms.ModelForm):
    class Meta:
        model = Blogpost
        fields = ['title_blogpost', 'text_blogpost', 'date_of_public_blogpost', 'author_blogpost', 'topics']


class TopicForm(forms.Form):
    title_topic = forms.CharField(max_length=128, required=True)
    text_topic = forms.CharField(max_length=250, required=True, widget=forms.Textarea)
    date_of_public_topic = forms.DateTimeField(initial=datetime.datetime.now())
    authors = forms.ModelChoiceField(queryset=Author.objects.all())


class TopicModelForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title_topic', 'text_topic', 'date_of_public_topic', 'authors']


class CommentForm(forms.Form):
    text_comment = forms.CharField(max_length=128, required=True, widget=forms.Textarea)
    blogpost = forms.ModelChoiceField(queryset=Blogpost.objects.all())
    date_of_public_comment = forms.DateTimeField(initial=datetime.datetime.now())
    author_comment = forms.ModelChoiceField(queryset=Author.objects.all())


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text_comment', 'blogpost', 'date_of_public_comment', 'author_comment']