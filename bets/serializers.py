from rest_framework import serializers
from bets.models import Sport
from bets.models import Outcome
from bets.models import Bet
from bets.models import Event
from bets.models import Team
from bets.models import Tournamet

class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = ['id', 'name']

class OutcomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outcome
        fields = ['id', 'type', 'result', 'status', 'event']

class BetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bet
        fields = ['id', 'coef', 'sum', 'outcome']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'status', 'score_home', 'score_away', 'tournamet', 'home_team']

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'sport']

class TournametSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournamet
        fields = ['id', 'name', 'sport', 'country']