from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Game, Players
from .forms import newGameForm
from django.views.decorators.csrf import csrf_exempt,csrf_protect 
import json,random, string


def homepage(request):
    return render (request = request,
                   template_name = 'main/home.html',
                   context = {"Games":Game.objects.all,
                              "Players": Players.objects.all})

def newGame (request):
 # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = newGameForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            newGameInstance = Game()
            # playersInstance = Players() ##gotta do something about this...
            redPlayers = {}
            redPlayers_GoalsAssists = {}
            bluePlayers = {}
            bluePlayers_GoalsAssists = {}
            game_Date = form.cleaned_data.get("game_Date")
            for k, v in form.data.items():
                if k.find("red") > -1:
                    if v:
                        redPlayers[k] = v
                        redPlayers_GoalsAssists[v]={"goals": 0,
                                        "assists": 0}
                if k.find("blue") > -1:
                    if v:
                        bluePlayers[k] = v
                        bluePlayers_GoalsAssists[v]={"goals": 0,
                                        "assists": 0}

            newGameInstance.teamRed_players = redPlayers
            newGameInstance.teamBlue_players = bluePlayers
            newGameInstance.game_Date = game_Date
            newGameInstance.teamRed_indexPlayerGoalsandAssist = redPlayers_GoalsAssists
            newGameInstance.teamBlue_indexPlayerGoalsandAssist = bluePlayers_GoalsAssists
            newGameInstance.teamBlue_score = 0
            newGameInstance.teamRed_score = 0 
            newGameInstance.game_Complete = False
            newGameInstance.game_code = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(20))
            newGameInstance.save()
            return render(request = request,
                            template_name = 'main/gamePlay.html',
                            context = {"Game":newGameInstance}
                            )

    # if a GET (or any other method) we'll create a blank form
    else:
        form = newGameForm()

        return render(request = request, template_name = 'main/newGame.html', context = {'form': form})


@csrf_exempt
def gamePlay (request):
    if request.method == 'POST':
        data = json.loads (request.body)
        redTeam = data['redTeam']
        blueTeam = data['blueTeam']
        gameInstance = Game.objects.get(game_code__exact= data['gameCode'])
        
        for i, players in enumerate(redTeam):
            gameInstance.teamRed_score += int(players['Goals'])
            gameInstance.teamRed_indexPlayerGoalsandAssist[i] = {'Goals': players['Goals'], 'Assists': players ['Assists']}
            

            #players individual stats...
            # playersInstance = Players.objects.get(player_name__exact = redTeam['player_name'])
            # playersInstance.player_lifeTimeGoals += int(players['Goals'])
            # playersInstance.player_lifeTimeAssists += int(players['Assists'])
            # playersInstance.player_lifeTimeScore = playersInstance.player_lifeTimeGoals + playersInstance.player_lifeTimeAssists



        for i, players in enumerate(blueTeam):
            gameInstance.teamBlue_score += int(players['Goals'])
            gameInstance.teamBlue_indexPlayerGoalsandAssist[i] = {'Goals': players['Goals'], 'Assists': players ['Assists']}
            

            #players individual stats...
            # playersInstance = Players.objects.get(player_name__exact = blueTeam['player_name'])
            # playersInstance.player_lifeTimeGoals += int(players['Goals'])
            # playersInstance.player_lifeTimeAssists += int(players['Assists'])
            # playersInstance.player_lifeTimeScore = playersInstance.player_lifeTimeGoals + playersInstance.player_lifeTimeAssists

        
        gameInstance.game_Complete = True
        gameInstance.save()

        

        return render(request, 'main/endgame.html', context = {Game: gameInstance})
    else:
        return render(request = request,
                        template_name = 'main/gamePlay.html',
                        context = gameInstance)

def endgame(request):
    return render(HttpResponse('what'))