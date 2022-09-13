from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Game, Players
from .forms import newGameForm, gamePlayForm
from django.views.decorators.csrf import csrf_exempt,csrf_protect 
import json,random, string
from django.urls import reverse
from urllib.parse import urlencode

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
           
            base_url = "/gamePlay"
            gameCode_url = urlencode({'gameCode': newGameInstance.game_code})
            url_additive = '{}?{}'.format(base_url,gameCode_url)
            print (url_additive)
            return redirect(url_additive)
        print(form.errors)
        return redirect("/newGame")
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
            gameInstance.teamRed_indexPlayerGoalsandAssist[players['player_name']] = {'goals': players['Goals'], 'assists': players ['Assists']}




        for i, players in enumerate(blueTeam):
            gameInstance.teamBlue_score += int(players['Goals'])
            gameInstance.teamBlue_indexPlayerGoalsandAssist[players['player_name']] = {'goals': players['Goals'], 'assists': players ['Assists']}
            
        print(gameInstance.teamRed_indexPlayerGoalsandAssist)
        
        gameInstance.game_Complete = True
        gameInstance.save()

        base_url = "/endGame"
        gameCode_url = urlencode({'gameCode': gameInstance.game_code})
        url_additive = '{}?{}'.format(base_url, gameCode_url)

        return redirect(url_additive)

    else:

        gameCode  = request.GET.get('gameCode');
        gameInstance = Game.objects.get(game_code__exact = gameCode)

        if gameInstance.game_Complete == False:
            return render(request = request,
                            template_name = 'main/gamePlay.html',
                            context = {"Game": gameInstance})
        else:
            base_url = "/endGame"
            gameCode_url = urlencode({'gameCode': gameInstance.game_code})
            url_additive = '{}?{}'.format(base_url, gameCode_url)
            return redirect(url_additive)

@csrf_exempt
def endGame(request):
    gameCode  = request.GET.get('gameCode');
    gameInstance = Game.objects.get(game_code__exact = gameCode)
    redTeamPlayers = gameInstance.teamRed_players
    blueTeamPlayers = gameInstance.teamBlue_players

    wholeRed = reStructure(redTeamPlayers,gameInstance.teamRed_indexPlayerGoalsandAssist)
    wholeBlue = reStructure(blueTeamPlayers,gameInstance.teamBlue_indexPlayerGoalsandAssist)
    print(wholeRed)
    
    return render(request = request, 
                template_name='main/endGame.html', 
                context = {'Game': gameInstance,
                            'wholeRed':wholeRed, 'wholeBlue': wholeBlue})

def reStructure(colorTeamPlayers, IndexedGoalsandAssists):
    structuredDict={}
    # print(colorTeamPlayers)
    # print (IndexedGoalsandAssists)
    for k,v in colorTeamPlayers.items():
        structuredDict[k] = {'Name': v, 
                            'goals': IndexedGoalsandAssists[v]['goals'], 
                            'assists' : IndexedGoalsandAssists[v]['assists'],
                            'points': int(IndexedGoalsandAssists[v]['goals']) + int(IndexedGoalsandAssists[v]['assists'])}
    
    return structuredDict 

def playerStats(request):
    return render(request = request,
                        template_name = 'main/playerStats.html',
                        context = {})