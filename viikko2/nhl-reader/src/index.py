import requests
from player import Player

#v2t12: Refaktorinti

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)

class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        response = requests.get(self.url).json()
        
        players = []
        for player_dict in response:
            player = Player(player_dict)
            players.append(player)
        
        return players

class PlayerStats:
    def __init__(self, player_reader):
        self.players = player_reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        
        searched_players = []
        for player in self.players:
            if player.nationality == nationality:
                searched_players.append(player)


        sorted_players = sorted(searched_players, key=lambda x: x.points, reverse=True)
        
        return sorted_players

if __name__ == "__main__":
    main()

#v2t10-11 ilman refaktorointia
#def main():
    #url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    #response = requests.get(url).json()

    #file template
    #print("JSON-muotoinen vastaus:")
    #print(response)

    #players = []

    #for player_dict in response:
        #player = Player(player_dict)
        #players.append(player)

    #v2t11: sorting players according to total points
    #sorted_players = sorted(players, key=lambda x: x.points, reverse=True)

    #file template
    #print("Oliot:")

    #file template
    #for player in players:
        #print(player)

    #v2t10: print FIN players
    #for player in sorted_players:
        #if player.nationality == "FIN":
            #print(player)

#if __name__ == "__main__":
    #main()
