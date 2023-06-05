from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=120)
    date_of_registration = models.DateTimeField()


class Topic(models.Model):
    titleTopic = models.CharField(max_length=128)
    text = models.TextField(null=True, blank=True)
    date_of_publicTopic = models.DateTimeField()
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.titleTopic


class Blogpost(models.Model):
    titleBlogpost = models.CharField(max_length=120)
    text = models.TextField(null=True, blank=True)
    date_of_publicBlogpost = models.DateTimeField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='blogpost')
    topics = models.ManyToManyField(Topic)

    def __str__(self):
        return self.titleBlogpost


class Comment(models.Model):
    text = models.TextField(null=True, blank=True)
    date_of_publicComment = models.DateTimeField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author')
    blogpost = models.ForeignKey(Blogpost, on_delete=models.CASCADE, related_name='blogpost')




# Create your models here.
