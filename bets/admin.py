from django.contrib import admin
from bets.models import Bet, Outcome, Sport, Team, Tournamet, Event
# Register your models here.

@admin.register(Bet)
class BetAdmin(admin.ModelAdmin):
    list_display = ["id", "coef", "sum", "outcome"]

@admin.register(Outcome)
class OutcomeAdmin(admin.ModelAdmin):
    list_display = ["id", "type", "result", "status", "event"]

@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "type"]

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ["id", "status", "score_home", "score_away", "tournamet", "home_team"]

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "sport"]

@admin.register(Tournamet)
class TournametAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "sport", "country"]
