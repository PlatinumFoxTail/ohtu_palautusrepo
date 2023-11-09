class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.penalties = dict['assists']
        self.team = dict['team']
        self.games = dict['games']

        self.points = self.goals + self.assists

    
    def __str__(self):
        
        #v2t10
        #return f"{self.name} team {self.team} goals {self.goals} assists {self.assists}"
        
        #v2t11
        return f"{self.name:<20} {self.team}  {self.goals:2} + {self.assists:2} = {self.points}"
