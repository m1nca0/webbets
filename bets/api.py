from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from bets.models import Sport
from bets.models import Outcome
from bets.models import Bet
from bets.models import Event
from bets.models import Team
from bets.models import Tournamet

from bets.serializers import SportSerializer
from bets.serializers import OutcomeSerializer
from bets.serializers import BetSerializer
from bets.serializers import EventSerializer
from bets.serializers import TeamSerializer
from bets.serializers import TournametSerializer

class SportsViewset(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer

class OutcomeViewset(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet):
    queryset = Outcome.objects.all()
    serializer_class = OutcomeSerializer

class BetViewset(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet):
    queryset = Bet.objects.all()
    serializer_class = BetSerializer

class EventViewset(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class TeamViewset(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TournametViewset(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet):
    queryset = Tournamet.objects.all()
    serializer_class = TournametSerializer