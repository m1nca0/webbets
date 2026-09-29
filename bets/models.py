from django.db import models

class Outcome(models.Model):
    type = models.TextField()
    result = models.TextField()
    status = models.TextField()
    event = models.ForeignKey("Event", on_delete=models.CASCADE, null = True)

    class Meta:
        verbose_name = "Исход"
        verbose_name_plural = "Исходы"

    def __str__(self) -> str:
        return self.name

class Bet(models.Model):
    coef = models.TextField()
    sum = models.TextField()
    outcome = models.ForeignKey("Outcome", on_delete=models.CASCADE, null = True)
    # user = models.ForeignKey("User", on_delete=models.CASCADE, null = True)

class Event(models.Model):
    status = models.TextField()
    score_home = models.TextField()
    score_away = models.TextField()
    tournamet = models.ForeignKey("Tournamet", on_delete=models.CASCADE, null = True)
    home_team = models.ForeignKey("Team", on_delete=models.CASCADE, null=True)
    # away_team = models.ForeignKey("Team", on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"

    def __str__(self) -> str:
        return self.name

class Team(models.Model):
    name = models.TextField()
    sport = models.ForeignKey("Sport", on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"

    def __str__(self) -> str:
        return self.name
    
class Sport(models.Model):
    name = models.TextField()
    type = models.TextField()
    
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

