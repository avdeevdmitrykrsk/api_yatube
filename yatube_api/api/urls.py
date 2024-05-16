# Thirdparty imports
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

# Projects imports
from api.views import CommentViewSet, GroupViewSet, PostViewSet, UserViewSet

# V1_router settings
v1_router = routers.DefaultRouter()
v1_router.register('v1/users', UserViewSet, basename='users')
v1_router.register('v1/groups', GroupViewSet, basename='groups')
v1_router.register('v1/posts', PostViewSet, basename='posts')
v1_router.register(
    r"v1/posts/(?P<post_id>\d+)/comments",
    CommentViewSet, basename="comments"
)

urlpatterns = [
    path("v1/api-token-auth/", views.obtain_auth_token),
    path("", include(v1_router.urls)),
]
