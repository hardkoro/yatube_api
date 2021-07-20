from django.shortcuts import get_object_or_404
from posts.models import Group, Post, User
from rest_framework import filters, permissions, status, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from .permissions import IsOwnerOrReadOnly, IsReadOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)


class PostViewSet(viewsets.ModelViewSet):
    """Получить список всех публикаций."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsOwnerOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """Получение всех комментариев к публикации."""
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments.all()

    def perform_create(self, serializer):
        get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action == 'retrieve':
            return (IsReadOnly(), )

        return super().get_permissions()


class GroupViewSet(viewsets.ModelViewSet):
    """Получение списка доступных сообществ."""
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = Group.objects.all()

    def create(self, request):
        response = {'message': 'Method not allowed.'}
        return Response(response, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class FollowViewSet(viewsets.ModelViewSet):
    """Возвращает все подписки пользователя, сделавшего запрос."""
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('following__username', 'user__username')

    def get_queryset(self):
        user = get_object_or_404(User, id=self.request.user.id)
        return user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
