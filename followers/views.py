from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from followers.models import Relationship
from followers.serializers import RelationshipUserSerializer, RelationshipSerializer
from followers.utils import get_following


class FollowingViewSet(ListModelMixin, GenericViewSet):

    serializer_class = RelationshipUserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return get_following(self.request.user)


class FollowViewSet(CreateModelMixin, GenericViewSet):

    queryset = Relationship.objects.all()
    serializer_class = RelationshipSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        """
        Hacemos que el usuario autenticado sea el seguidor
        """
        serializer.save(origin=self.request.user)