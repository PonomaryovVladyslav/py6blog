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
    fields = ('title_topic', 'text_topic', 'date_of_public_topic', 'authors')

    def create_date(self, obj):
        return obj.created

    create_date.empty_value_display = '???'


@admin.register(Blogpost)
class BlogpostAdmin(admin.ModelAdmin):
    fields = ('slug', 'title_blogpost', 'text_blogpost', 'date_of_public_blogpost', 'author_blogpost', 'topics')
    prepopulated_fields = {"slug": ("title_blogpost",)}

    def create_date(self, obj):
        return obj.created

    create_date.empty_value_display = '???'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ('text_comment', 'date_of_public_comment', 'author_comment', 'blogpost')

    def create_date(self, obj):
        return obj.created

    create_date.empty_value_display = '???'



# Register your models here.
