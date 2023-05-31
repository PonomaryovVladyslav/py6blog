from django.urls import path
from .views import blogs, about, oneblog, comment, create, update, delete, index
urlpatterns = [
    path('', index, name='index'),

    path('blogs/', index, name='index'),
    # path('blogs/', blogs),
    path('about/', about),
    path('oneblog/', oneblog, name='oneblog'),
    path('comment/<slug:txt>/', comment),
    path('create/', create, name='create'),
    path('update/<slug:txt>/', update),
    path('delete/<slug:txt>/', delete),
]

