from rest_framework import routers
from .api_views import TopicViewSet, BlogpostViewSet, CommentViewSet, GroupViewSet, AuthorViewSet
# from .filters import AuthorFilterBackend

router = routers.SimpleRouter()
router.register(r'topic', TopicViewSet)
router.register(r'blogpost', BlogpostViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'group', GroupViewSet)
router.register(r'author', AuthorViewSet)
urlpatterns = router.urls

