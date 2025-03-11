from django.db import models
from django.utils.text import slugify


# Create your models here.
# Item object with name and description
class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    

class Team(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    

class Game(models.Model):
    game_date = models.DateField()
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="home_games", null=True, blank=True)
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="away_games", null=True, blank=True)
    home_team_score = models.PositiveIntegerField(default=0)
    away_team_score = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.home_team.name} vs {self.away_team.name} on {self.game_date}"
    
    @property
    def winner(self):
        if self.home_team_score > self.away_team_score:
            return self.home_team.name
        elif self.away_team_score > self.home_team_score:
            return self.away_team.name
        return "Tie"


class Player(models.Model):
    name = models.CharField(max_length=30)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="players", null=True)

    def __str__(self):
        return self.name
    

class GameStat(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="gamestat")
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="gamestat")

    def __str__(self):
        return f"{self.player.name} stats for {self.game}"

class AtBat(models.Model):
    gamestat = models.ForeignKey(GameStat, on_delete=models.CASCADE, related_name="atbat")
    OUTCOMES = [
        ("OUT_3", "3 Strikes and Out"),
        ("OUT_2", "2 Strikes and Out"),
        ("OUT_1", "1 Strike and Out"),
        ("OUT_0", "0 Strikes and Out"),
        ("SINGLE", "Single (1 Base Hit)"),
        ("DOUBLE", "Double (2 Base Hits)"),
        ("TRIPLE", "Triple (3 Base Hits)"),
        ("HOMERUN", "Home Run"),
    ]
    outcome = models.CharField(max_length=10, choices=OUTCOMES)
    inning = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.gamestat.player.name} - {self.get_outcome_display()} in inning {self.inning}" 