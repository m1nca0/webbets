from django.db import models
from django.conf import settings

class Outcome(models.Model):
    type = models.TextField()
    result = models.BooleanField()
    status = models.BooleanField()
    event = models.ForeignKey("Event", on_delete=models.CASCADE, null = True)

    class Meta:
        verbose_name = "Исход"
        verbose_name_plural = "Исходы"

    def __str__(self) -> str:
        return self.type + " " + str(self.result) + " " + str(self.status) + " " + self.event.tournamet.name

class Bet(models.Model):
    coef = models.FloatField()
    sum = models.FloatField()
    outcome = models.ForeignKey("Outcome", on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
    )

class Event(models.Model):
    status = models.BooleanField()
    score_home = models.IntegerField()
    score_away = models.IntegerField()
    tournamet = models.ForeignKey("Tournamet", on_delete=models.CASCADE, null=True)
    home_team = models.ForeignKey(
        "Team",
        on_delete=models.CASCADE,
        null=True,
        related_name="home_events",
    )
    away_team = models.ForeignKey(
        "Team",
        on_delete=models.CASCADE,
        null=True,
        related_name="away_events",
    )

    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"

    def __str__(self) -> str:
        return self.tournamet.name + " " + self.home_team.name + " vs " + self.away_team.name

class Team(models.Model):
    name = models.TextField()
    sport = models.ForeignKey("Sport", on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"

    def __str__(self) -> str:
        return self.name
    
class Sport(models.Model):
    class Type(models.TextChoices):
        TEAM = "team", "Командный"
        INDIVIDUAL = "individual", "Индивидуальный"
        PAIR = "pair", "Парный"

    name = models.TextField()
    type = models.CharField(
        max_length=20,
        choices=Type.choices,
        default=Type.TEAM,
    )

    class Meta:
        verbose_name = "Спорт"
        verbose_name_plural = "Вид спорта"

    def __str__(self) -> str:
        return self.name

class Tournamet(models.Model):
    name = models.TextField()
    sport = models.ForeignKey("Sport", on_delete=models.CASCADE, null=True)
    country = models.TextField()
    
    class Meta:
        verbose_name = "Турнир"
        verbose_name_plural = "Турниры"

    def __str__(self) -> str:
        return self.name

