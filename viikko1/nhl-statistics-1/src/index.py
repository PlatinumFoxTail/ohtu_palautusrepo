from player_reader import PlayerReader #added
from statistics_service import StatisticsService, SortBy


def main():
    ### v1t15 ###
    #stats = StatisticsService()
    stats = StatisticsService(PlayerReader("https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"))
    
    ### v1t16 ###
    #philadelphia_flyers_players = stats.team("PHI")
    #top_scorers = stats.top(10)

    #print("Philadelphia Flyers:")
    #for player in philadelphia_flyers_players:
        #print(player)

    #print("Top point getters:")
    #for player in top_scorers:
        #print(player)

    ### v1t17 ###

    # järjestetään kaikkien tehopisteiden eli maalit+syötöt perusteella
    print("Top point getters:")
    for player in stats.top(10, SortBy.POINTS):
        print(player)

    # metodi toimii samalla tavalla kuin yo. kutsu myös ilman toista parametria
    for player in stats.top(10):
        print(player)

    # järjestetään maalien perusteella
    print("Top point goal scorers:")
    for player in stats.top(10, SortBy.GOALS):
        print(player)

    # järjestetään syöttöjen perusteella
    print("Top by assists:")
    for player in stats.top(10, SortBy.ASSISTS):
        print(player)

if __name__ == "__main__":
    main()
