from django.shortcuts import get_object_or_404
from posts.models import Comment, Follow, Group, Post, User
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username', read_only=True)
    following = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all())

    def validate(self, data):
        """Проверяем, что подписки уже нет, и что она не на самого себя."""
        user = get_object_or_404(User, username=data['following'].username)
        follow = Follow.objects.filter(
            user=self.context['request'].user, following=user).exists()

        if follow:
            raise serializers.ValidationError('Подписка уже существует!')
        elif user == self.context['request'].user:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя!')

        return data

    class Meta:
        fields = ('user', 'following')
        model = Follow
