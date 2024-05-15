from rest_framework import routers

from django.urls import include, path
from rest_framework.authtoken import views

from api.views import CommentViewSet, GroupViewSet, PostViewSet


router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('posts/<int:post_id>/comments/', CommentViewSet.as_view(
        {
            'get': 'list',
            'post': 'create'
        }
    )),
    path(
        'posts/<int:post_id>/comments/<int:comment_id>/',
        CommentViewSet.as_view(
            {
                'get': 'retrieve',
                'put': 'update',
                'patch': 'partial_update',
                'delete': 'destroy'
            }
        )
    ),
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
]
