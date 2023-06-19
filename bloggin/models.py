from django.db import models
from django.utils.text import slugify


class Author(models.Model):
    name = models.CharField(max_length=120)
    date_of_registration = models.DateTimeField(null=True, blank=True)


class Topic(models.Model):
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    title_topic = models.CharField(max_length=128)
    text_topic = models.TextField(null=True, blank=True)
    date_of_public_topic = models.DateTimeField(null=True, blank=True)
    authors = models.ManyToManyField(Author)


    def __str__(self):
        return self.title_topic

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)


class Blogpost(models.Model):
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    title_blogpost = models.CharField(max_length=120)
    text_blogpost = models.TextField(null=True, blank=True)
    date_of_public_blogpost = models.DateTimeField(null=True, blank=True)
    author_blogpost = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='blogpost')
    topics = models.ManyToManyField(Topic)

    def __str__(self):
        return self.title_blogpost

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.id:
            self.slug = slugify(self.title_blogpost)
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)


class Comment(models.Model):
    text_comment = models.TextField(null=True, blank=True)
    date_of_public_comment = models.DateTimeField(null=True, blank=True)
    author_comment = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author')
    blogpost = models.ForeignKey(Blogpost, on_delete=models.CASCADE, related_name='blogpost')




# Create your models here.
