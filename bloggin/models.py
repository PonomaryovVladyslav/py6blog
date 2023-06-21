from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Author(models.Model):
    name = models.CharField(max_length=120)
    created_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.name

class Topic(models.Model):
    slug = models.SlugField(unique=True, blank=True, null=True)
    title = models.CharField(max_length=128)
    text = models.TextField(null=True, blank=True)
    authors = models.ManyToManyField(User)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.id:
            self.slug = slugify(self.title)
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)



class Blogpost(models.Model):
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    title = models.CharField(max_length=120)
    text = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogpost')
    topics = models.ManyToManyField(Topic)

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.id:
            self.slug = slugify(self.title)
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)


class Comment(models.Model):
    text = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    blogpost = models.ForeignKey(Blogpost, on_delete=models.CASCADE, related_name='blogpost')




# Create your models here.
