from django.urls import path

from .views import PostsListView, PostCreate, TopicCreate, TopicListView, BlogDetailView, CommentCreate, \
    PostsInTopicListView, BlogDeleteView, BlogUpdateView, AddLike, AddDislike, AddFollower, About, TopicDeleteView, \
    TopicUpdateView

urlpatterns = [
    path('', PostsListView.as_view(), name='blogs'),
    path('blogs/', PostsListView.as_view(), name='blogs'),
    path('about/', About.as_view(), name = 'about'),
    path('get_topic/<slug:slug>/', PostsInTopicListView.as_view(), name='get_topic'),
    path('by_topics/',  TopicListView.as_view(), name = 'by_topics'),
    path('get_blog/<slug:slug>/', BlogDetailView.as_view(), name='get_blog'),
    path('create/', PostCreate.as_view(), name='create'),
    path('<slug:slug>/comment/', CommentCreate.as_view(), name='create_comment'),
    path('topic_create/', TopicCreate.as_view(), name = 'topic_create'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('by_topics/<int:pk>/delete/', TopicDeleteView.as_view(), name='topic_delete'),
    path('by_topics/<int:pk>/edit/', TopicUpdateView.as_view(), name='topic_edit'),
    path('post/<int:pk>/like', AddLike.as_view(), name='like'),
    path('post/<int:pk>/dislike', AddDislike.as_view(), name='dislike'),
    path('by_topics/<int:topic_id>/followers/add', AddFollower.as_view(), name='add_follower'),
    # path('by_topics/<int:topic_id>/followers/remove', RemoveFollower.as_view(), name='remove_follower'),
]

