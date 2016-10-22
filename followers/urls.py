from rest_framework.routers import SimpleRouter

from followers.views import FollowingViewSet

router = SimpleRouter()
router.register(r'following', FollowingViewSet, base_name='following')

urlpatterns = router.urls
