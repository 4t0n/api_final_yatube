from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Follow, Group, Comment, Post
from .serializers import (CommentSerializer, GroupSerializer,
                          PostSerializer, FollowSerializer)


# class BaseViewset(viewsets.ModelViewSet):
#     def perform_update(self, serializer):
#         if serializer.instance.author != self.request.user:
#             raise PermissionDenied()
#         super().perform_update(serializer)

#     def perform_destroy(self, instance):
#         if instance.author != self.request.user:
#             raise PermissionDenied()
#         super().perform_destroy(instance)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        return post.comments.all()

    # def perform_create(self, serializer):
    #     serializer.save(
    #         author=self.request.user,
    #         post=get_object_or_404(Post, pk=self.kwargs['post_id'])
    #     )


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
