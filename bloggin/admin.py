from django.contrib import admin
from .models import Author, Blogpost, Comment, Topic


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = ('name', 'date_of_registration')

    def create_date(self, obj):
        return obj.created

    create_date.empty_value_display = '???'


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    fields = ('titleTopic', 'text', 'date_of_public', 'authors')

    def create_date(self, obj):
        return obj.created

    create_date.empty_value_display = '???'


@admin.register(Blogpost)
class BlogpostAdmin(admin.ModelAdmin):
    fields = ('titleBlogpost', 'text', 'date_of_public', 'author', 'topics')

    def create_date(self, obj):
        return obj.created

    create_date.empty_value_display = '???'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ('text', 'date_of_public', 'author', 'blogpost')

    def create_date(self, obj):
        return obj.created

    create_date.empty_value_display = '???'



# Register your models here.
