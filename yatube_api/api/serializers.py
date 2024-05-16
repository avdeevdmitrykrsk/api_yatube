# Thirdparty imports
from rest_framework import serializers

# Projects imports
from posts.models import Comment, Group, Post, User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = (
            'password', 'user_permissions',
            'is_superuser', 'is_staff',
            'is_active', 'groups'
        )
        read_only_fields = (
            'password', 'user_permissions',
            'is_superuser', 'is_staff',
            'is_active', 'groups',
            'date_joined', 'last_login'
        )


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Post
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post',)
