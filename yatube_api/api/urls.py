# Thirdparty imports
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

# Projects imports
from api.views import CommentViewSet, GroupViewSet, PostViewSet

# V1_router settings
v1_router = routers.DefaultRouter()
v1_router.register('groups', GroupViewSet, basename='groups')
v1_router.register('posts', PostViewSet, basename='posts')
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet, basename='comments'
)

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(v1_router.urls)),
]
