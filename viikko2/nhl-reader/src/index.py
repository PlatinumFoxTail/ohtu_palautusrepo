import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    response = requests.get(url).json()

    #file template
    #print("JSON-muotoinen vastaus:")
    #print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    #v2t11: sorting players according to total points
    sorted_players = sorted(players, key=lambda x: x.points, reverse=True)

    #file template
    #print("Oliot:")

    #file template
    #for player in players:
        #print(player)

    #v2t10: print FIN players
    for player in sorted_players:
        if player.nationality == "FIN":
            print(player)

if __name__ == "__main__":
    main()
