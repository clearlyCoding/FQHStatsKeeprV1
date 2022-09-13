#FQH Stats Beta App


# goalie pts --> 5 = +5 pts, 1 goalie game played,; more than 5 = +x pts, 1 goalie game played, 1 goalie game won

# goals, assists, goalie pts, games played, goalie games played, goalie games won, pts (sum of goals, assists, goalie pts)

import glob
import os 
from datetime import datetime

fqh_peeps = {}

path = "C:/Users/Home/Desktop/FQH_python/Test Data/"

os.chdir(path)

for each_file in glob.glob('*.txt'):
    with open(each_file) as f:
        print(f)
        team_colours = f.readline().split(',')[1].split() 
                
        for line in f.readlines():
            info = line.strip().split(',')
            if (info[0].strip() in team_colours):
                name                = info[1].strip()
                goals               = int(info[2].strip())
                assists             = int(info[3].strip())
                goalie_pts          = 0
                games_played        = 1
                goalie_games_played = 0
                goalie_game_win     = 0

                if (len(info) == 5):
                    goalie_pts = int(info[4].strip())
                    goalie_games_played = 1
                    if (goalie_pts > 5):
                        goalie_game_win = 1
                    
                if (name in fqh_peeps):
                    fqh_peeps[name]["GAMES_PLAYED"]        += 1
                    fqh_peeps[name]["GOALS"]               += goals
                    fqh_peeps[name]["ASSISTS"]             += assists
                    fqh_peeps[name]["GOALIE_GAMES_PLAYED"] += goalie_games_played
                    fqh_peeps[name]["GOALIE_GAMES_WON"]    += goalie_game_win
                    fqh_peeps[name]["GOALIE_PTS"]          += goalie_pts
                    fqh_peeps[name]["TOT_PTS"]             += goals + assists + goalie_pts
                    
                else:
                    fqh_peeps[name] = {"GAMES_PLAYED": 1, "GOALS": goals, "ASSISTS": assists,   
                                       "GOALIE_GAMES_PLAYED": goalie_games_played, "GOALIE_GAMES_WON": goalie_game_win,  
                                       "GOALIE_PTS": goalie_pts, "TOT_PTS": goals+assists+goalie_pts}

for guy in fqh_peeps:
    ppg = fqh_peeps[guy]["TOT_PTS"] / fqh_peeps[guy]["GAMES_PLAYED"]
    fqh_peeps[guy]["PPG"] = ppg

now = datetime.now()
dt_string = now.strftime("%Y-%m-%d_%H%M%S")
file_name = str(dt_string)+".txt"

final_file = open(file_name, "w")
str1 = ("%-20s GAMES_PLAYED | GOALS | ASSISTS | GOALIE_GAMES_PLAYED | GOALIE_GAMES_WON | GOALIE_PTS | TOT_PTS | PPG\n" %("NAME"))
str2 = "NAME, GAMES_PLAYED, GOALS, ASSISTS, GOALIE_GAMES_PLAYED, GOALIE_GAMES_WON, GOALIE_PTS, TOT_PTS, PPG\n"
# final_file.write(str1)
final_file.write(str2)
for guy in fqh_peeps:
    str1 = ("%-27s %-8d %-11d %-8d %-20d %-17d %-11d %-8d %-5.2f\n" %(guy, fqh_peeps[guy]["GAMES_PLAYED"],
                                                                  fqh_peeps[guy]["GOALS"],
                                                                  fqh_peeps[guy]["ASSISTS"],
                                                                  fqh_peeps[guy]["GOALIE_GAMES_PLAYED"],
                                                                  fqh_peeps[guy]["GOALIE_GAMES_WON"],
                                                                  fqh_peeps[guy]["GOALIE_PTS"],
                                                                  fqh_peeps[guy]["TOT_PTS"],
                                                                  fqh_peeps[guy]["PPG"]                 ))

    str2 = ("%s, %d, %d, %d, %d, %d, %d, %d, %.2f\n" %(guy, fqh_peeps[guy]["GAMES_PLAYED"],
                                                                  fqh_peeps[guy]["GOALS"],
                                                                  fqh_peeps[guy]["ASSISTS"],
                                                                  fqh_peeps[guy]["GOALIE_GAMES_PLAYED"],
                                                                  fqh_peeps[guy]["GOALIE_GAMES_WON"],
                                                                  fqh_peeps[guy]["GOALIE_PTS"],
                                                                  fqh_peeps[guy]["TOT_PTS"],
                                                                  fqh_peeps[guy]["PPG"]                 ))
    final_file.write( str2 )

final_file.close()

'''
fqh_peeps = {}

my_file = open("Test Data/2010-01-02.txt", encoding='utf-8')
team_colours = my_file.readline().split(',')[1].split() 
# print(team_colours)

for line in my_file.readlines():
    info = line.strip().split(',')
    if (info[0] in team_colours):
        name    = info[1]
        pts     = info[2]
        assists = info[3]
        
        if (name in fqh_peeps):
            fqp_peeps[name][0] += pts
            fqp_peeps[name][1] += assists
        else:
            fqh_peeps[name] = [pts, assists]

print(fqh_peeps)
for guy in fqh_peeps:
    print(guy)
    print(fqh_peeps[guy])
            
my_file.close()

'''

