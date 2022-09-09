from django import forms
import datetime

class newGameForm (forms.Form):
	redPlayer1 = forms.CharField (label= 'Red Captain', max_length = 100, initial = "", required = False) #required
	redPlayer2 = forms.CharField (label= 'Red Goalie', max_length = 100, initial = "", required = False) #required
	redPlayer3 = forms.CharField (label= 'Red Player 3', max_length = 100, initial = "", required = False) #required
	redPlayer4 = forms.CharField (label= 'Red Player 4', max_length = 100, initial = "", required = False) #required
	redPlayer5 = forms.CharField (label= 'Red Player 5', max_length = 100, initial = "", required = False)
	redPlayer6 = forms.CharField (label= 'Red Player 6', max_length = 100, initial = "", required = False)
	redPlayer7 = forms.CharField (label= 'Red Player 7', max_length = 100, initial = "", required = False)
	redPlayer8 = forms.CharField (label= 'Red Player 8', max_length = 100, initial = "", required = False)
	redPlayer9 = forms.CharField (label= 'Red Player 9', max_length = 100, initial = "", required = False)
	redPlayer10 = forms.CharField (label= 'Red Player 10', max_length = 100, initial = "", required = False)

	bluePlayer1 = forms.CharField (label= 'Blue Captain', max_length = 100, initial = "", required = False) #required
	bluePlayer2 = forms.CharField (label= 'Blue Goalie', max_length = 100, initial = "", required = False) #required
	bluePlayer3 = forms.CharField (label= 'Blue Player 3', max_length = 100, initial = "", required = False) #required
	bluePlayer4 = forms.CharField (label= 'Blue Player 4', max_length = 100, initial = "", required = False) #required
	bluePlayer5 = forms.CharField (label= 'Blue Player 5', max_length = 100, initial = "", required = False)
	bluePlayer6 = forms.CharField (label= 'Blue Player 6', max_length = 100, initial = "", required = False)
	bluePlayer7 = forms.CharField (label= 'Blue Player 7', max_length = 100, initial = "", required = False)
	bluePlayer8 = forms.CharField (label= 'Blue Player 8', max_length = 100, initial = "", required = False)
	bluePlayer9 = forms.CharField (label= 'Blue Player 9', max_length = 100, initial = "", required = False)
	bluePlayer10 = forms.CharField (label= 'Blue Player 10', max_length = 100, initial = "", required = False)

	game_Date = forms.DateField(initial = datetime.date.today) 


class gamePlayForm(forms.Form):
	nothing= forms.CharField(label='',required = False)
	