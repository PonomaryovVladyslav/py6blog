from django.urls import path
from .views import blogs, about, oneblog, comment, create, update, delete
urlpatterns = [
    path('', blogs),
    path('blogs/', blogs),
    path('about/', about),
    path('oneblog/<slug:txt>/', oneblog),
    path('comment/<slug:txt>/', comment),
    path('create/', create),
    path('update/<slug:txt>/', update),
    path('delete/<slug:txt>/', delete),
]

