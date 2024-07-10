from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

app_name = 'api'
v1_router = routers.DefaultRouter()
v1_router.register('posts', PostViewSet)
v1_router.register('groups', GroupViewSet)
v1_router.register('follow', FollowViewSet)
v1_router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet)
urlpatterns = [
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(v1_router.urls)),
]
