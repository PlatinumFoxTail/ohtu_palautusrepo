from player_reader import PlayerReader
from enum import Enum

### v1t16 ###

def sort_by_points(player):
    return player.points


class StatisticsService:
    #def __init__(self):
        #reader = PlayerReader()
        #self._players = reader.get_players()
    def __init__(self, player_reader):
        self._players = player_reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    ### v1t16 ###
    #def top(self, how_many):
        #sorted_players = sorted(
            #self._players,
            #reverse=True,
            #key=sort_by_points
        #)

        #result = []
        #i = 0
        #while i <= how_many:
            #result.append(sorted_players[i])
            #i += 1

        #return result
    
    ### v1t17 ###
    def top(self, how_many, sort_by=None):
        if sort_by == SortBy.POINTS:
            key_function = lambda player: player.points
        elif sort_by == SortBy.GOALS:
            key_function = lambda player: player.goals
        elif sort_by == SortBy.ASSISTS:
            key_function = lambda player: player.assists
        else:
            key_function = lambda player: player.points  

        sorted_players = sorted(
            self._players,
            reverse=True,
            key=key_function
        )

        return sorted_players[:how_many]
    
### v1t17 ###

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3
