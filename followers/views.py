from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from followers.serializers import RelationshipUserSerializer
from followers.utils import get_following


class FollowingViewSet(GenericViewSet):

    serializer_class = RelationshipUserSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        following = get_following(request.user)
        serializer = RelationshipUserSerializer(following, many=True)
        return Response(serializer.data)
