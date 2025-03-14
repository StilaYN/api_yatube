from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter
from api.views import PostViewSet

post_router = SimpleRouter()
post_router.register('posts', PostViewSet)
# Create your views here.
urlpatterns = [
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('api/v1/', include(post_router.urls))
]

