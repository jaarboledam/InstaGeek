from rest_framework.routers import SimpleRouter

from followers.views import FollowingViewSet, FollowViewSet

router = SimpleRouter()
router.register(r'following', FollowingViewSet, base_name='following')
router.register(r'follow', FollowViewSet)

urlpatterns = router.urls
