from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class League(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.country})"


class Team(models.Model):
    name = models.CharField(max_length=255, unique=True)
    rating = models.IntegerField(default=1)
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name="teams")

    class Meta:
        ordering = ["-rating", "name"]

    def __str__(self):
        return self.name


class Player(AbstractUser):
    points = models.IntegerField(default=0)     # currency
    score = models.IntegerField(default=0)

    class Meta:
        ordering = ["-score", "username"]
        verbose_name = "player"
        verbose_name_plural = "players"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("tournament:player-detail", kwargs={"pk": self.pk})


class GameSession(models.Model):
    date = models.DateField(auto_now_add=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="game_sessions")
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="game_sessions")
    score = models.IntegerField(default=0)
    last_stage = models.CharField(max_length=255)
    win = models.BooleanField(default=False)

    class Meta:
        ordering = ["-date"]

    def save(self, *args, **kwargs):
        super(GameSession, self).save(*args, **kwargs)

        self.player.score += self.score
        self.player.points += self.score
        self.player.save()

    def __str__(self):
        return f"{self.player.username} - {self.team.name} ({self.date})"
