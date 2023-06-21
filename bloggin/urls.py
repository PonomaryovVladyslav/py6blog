from django.urls import path

from .views import blogs, about, get_blog, comment, create, update, delete, topic_create, \
    by_topics, index, create_comment, get_topic



urlpatterns = [
    path('', blogs, name='blogs'),
    path('blogs/', blogs, name='blogs'),
    path('about/', about),
    path('get_topic/<slug:slug>/', get_topic, name='get_topic'),
    path('by_topics/', by_topics, name = 'by_topics'),
    path('get_blog/<slug:slug>/', get_blog, name='get_blog'),
    path('comment/<slug:slug>/', comment),
    path('create/', create, name='create'),
    path('create_comment/', create_comment, name='create_comment'),

    path('topic_create/', topic_create, name = 'topic_create'),
    path('update/<slug:txt>/', update),
    path('delete/<slug:txt>/', delete),
]

