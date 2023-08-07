from django.contrib import admin
from .models import Author, Blogpost, Comment, Topic


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = ('name', 'created_at')

    def create_date(self, obj):
        return obj.created

    create_date.empty_value_display = '???'


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    fields = ('slug', 'title', 'text', 'followers')

    def create_date(self, obj):
        return obj.created


    create_date.empty_value_display = '???'


@admin.register(Blogpost)
class BlogpostAdmin(admin.ModelAdmin):
    fields = ('slug', 'title', 'text',  'topics', 'likes', 'dislikes')
    prepopulated_fields = {"slug": ("title",)}

    def create_date(self, obj):
        return obj.created

    create_date.empty_value_display = '???'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ('text_comment',  'blogpost')

    def create_date(self, obj):
        return obj.created

    create_date.empty_value_display = '???'



# Register your models here.
