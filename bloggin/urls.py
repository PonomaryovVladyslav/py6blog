from django.urls import path
from .views import blogs, about, get_blog, comment, create, update, delete, index
urlpatterns = [
    path('', blogs, name='blogs'),
    path('blogs/', blogs, name='blogs'),
    # path('blogs/', blogs),
    path('about/', about),
    path('get_blog/<slug:slug>/', get_blog, name='get_blog'),
    path('comment/<slug:txt>/', comment),
    path('create/', create, name='create'),
    path('update/<slug:txt>/', update),
    path('delete/<slug:txt>/', delete),
]

