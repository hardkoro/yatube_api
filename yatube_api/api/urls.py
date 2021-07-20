from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet, PostViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('v1/', include(router.urls))
]
