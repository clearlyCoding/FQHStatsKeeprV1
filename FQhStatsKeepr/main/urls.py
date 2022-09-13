from django.urls import path
from . import views



app_name = 'main' #namespace



urlpatterns = [
	path ("", views.homepage, name = "homepage"),
	path ("newGame/", views.newGame, name = "newGame"),
	path ("gamePlay/", views.gamePlay, name = "gamePlay"),
	path ("endGame/", views.endGame, name = "endGame"),
	path ("playerStats/", views.playerStats, name = "playerStats"),
]