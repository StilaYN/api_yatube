from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter
from api.views import GroupViewSet, PostViewSet, CommentViewSet

group_router = SimpleRouter()
group_router.register('groups', GroupViewSet)

post_router = SimpleRouter()
post_router.register('posts', PostViewSet)
# Create your views here.
urlpatterns = [
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('api/v1/', include(post_router.urls)),
    path('api/v1/', include(group_router.urls)),
    path(
        'api/v1/posts/<int:post_id>/comments/',
        CommentViewSet.as_view({
            'get': 'list',
            'post': 'create'
        }),
        name='comment-list'
    ),
    path(
        'api/v1/posts/<int:post_id>/comments/<int:pk>/',
        CommentViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        }),
        name='comment-detail'
    ),
]
