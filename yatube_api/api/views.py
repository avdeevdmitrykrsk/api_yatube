# Thirdparty imports
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Projects imports
from api.permissions import AuthorOrNot, UserAuth
from api.serializers import (CommentSerializer, GroupSerializer,
                             PostSerializer, UserSerializer)
from posts.models import Comment, Group, Post, User


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AuthorOrNot, IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        self.get_queryset


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AuthorOrNot, IsAuthenticated]

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        queryset = post.comments.all()
        return queryset

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        serializer.save(author=self.request.user, post=post)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserAuth]

    def get_queryset(self):
        queryset = User.objects.all()
        user = self.request.user
        self.check_object_permissions(self.request, user)
        return queryset
