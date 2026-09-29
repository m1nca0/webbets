from rest_framework.viewsets import GenericViewSet

from bets.models import Bet

class BetsViewset(GenericViewSet):
    queryset = Bet.objects.all()