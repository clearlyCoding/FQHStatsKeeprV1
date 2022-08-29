from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Game (models.Model):
	teamRed_score = models.IntegerField()
	teamBlue_score = models.IntegerField()
	teamRed_players = models.JSONField()
	teamBlue_players = models.JSONField()
	teamRed_indexPlayerGoalsandAssist = models.JSONField()
	teamBlue_indexPlayerGoalsandAssist = models.JSONField()
	game_Complete = models.BooleanField(default = False)
	game_Date = models.DateField ('date Played')
	game_code = models.CharField(max_length = 100, default = '')

	def __str__(self):
		return str(self.game_Date)

class Players(models.Model):
	player_name = models.CharField (max_length = 200)
	player_lifeTimeGoals = models.IntegerField()
	player_lifeTimeAssists = models.IntegerField()
	player_lifeTimeScore = models.IntegerField()
	

	def __str__(self):
		return self.player_name

# class Games(models.Model):
# 	game_Date = models.ForiegnKey(Game, default = 1, verbose_name = "Date", on_delete = models.SET_DEFAULT)
