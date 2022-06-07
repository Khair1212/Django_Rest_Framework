from django.urls import path
# from .views import PostList, PostDetail, UserList, UserDetail
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, PostViewSet


router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')

urlpatterns = router.urls

