from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from bets.models import Sport
from bets.serializers import SportSerializer
class BetsViewset(mixins.ListModelMixin, GenericViewSet):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer