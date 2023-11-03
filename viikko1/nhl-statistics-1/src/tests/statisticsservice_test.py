import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89),
            Player('Smith', 'NJD', 0, 5),
            Player('Tatar', 'NJD', 20, 28),
            Player('Haula', 'NJD', 14, 27),
            Player('Palat', 'NJD', 8, 15),
            Player('Hamilton', 'NJD', 22, 52),
            Player('Severson', 'NJD', 7, 26),
            Player('Wood', 'NJD', 13, 14),
            Player('Graves', 'NJD', 8, 18),
            Player('Siegenthaler', 'NJD', 4, 17),
            Player('Marino', 'NJD', 4, 14),
            Player('Bratt', 'NJD', 32, 41),
            Player('Bastian', 'NJD', 6, 9),
            Player('McLeod', 'NJD', 4, 22),
            Player('Hischier', 'NJD', 31, 49),
            Player('Boqvist', 'NJD', 10, 11),
            Player('Bahl', 'NJD', 2, 6),
            Player('Sharangovich', 'NJD', 13, 17),
            Player('Foote', 'NJD', 1, 0),
            Player('Okhotiuk', 'NJD', 1, 0),
            Player('Hughes', 'NJD', 43, 56),
            Player('Thompson', 'NJD', 0, 0),
            Player('Mercer', 'NJD', 27, 29),
            Player('Holtz', 'NJD', 3, 1),
            Player('Hughes', 'NJD', 1, 1),
            Player('Vanecek', 'NJD', 0, 0),
            Player('Blackwood', 'NJD', 0, 0),
            Player('Schmid', 'NJD', 0, 0),
            Player("McDavid", "EDM", 64, 89),
            Player("Draisaitl", "EDM", 52, 76),
            Player("Pastrnak", "BOS", 61, 52)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_existing_player(self):
        existing_player = self.stats.search("Kurri")
        self.assertEqual(existing_player.name, "Kurri", f"Right player name: 'Kurri', Given player name: '{existing_player.name}'")

    def test_search_nonexisting_player(self):
        nonexisting_player = self.stats.search("Batman")
        self.assertIsNone(nonexisting_player, None)

    def test_search_teamplayers(self):
        teamplayers = self.stats.team("NJD")
    
        NJD_teamplayers = [
            {'name': 'Smith', 'team': 'NJD', 'goals': 0, 'assists': 5},
            {'name': 'Tatar', 'team': 'NJD', 'goals': 20, 'assists': 28},
            {'name': 'Haula', 'team': 'NJD', 'goals': 14, 'assists': 27},
            {'name': 'Palat', 'team': 'NJD', 'goals': 8, 'assists': 15},
            {'name': 'Hamilton', 'team': 'NJD', 'goals': 22, 'assists': 52},
            {'name': 'Severson', 'team': 'NJD', 'goals': 7, 'assists': 26},
            {'name': 'Wood', 'team': 'NJD', 'goals': 13, 'assists': 14},
            {'name': 'Graves', 'team': 'NJD', 'goals': 8, 'assists': 18},
            {'name': 'Siegenthaler', 'team': 'NJD', 'goals': 4, 'assists': 17},
            {'name': 'Marino', 'team': 'NJD', 'goals': 4, 'assists': 14},
            {'name': 'Bratt', 'team': 'NJD', 'goals': 32, 'assists': 41},
            {'name': 'Bastian', 'team': 'NJD', 'goals': 6, 'assists': 9},
            {'name': 'McLeod', 'team': 'NJD', 'goals': 4, 'assists': 22},
            {'name': 'Hischier', 'team': 'NJD', 'goals': 31, 'assists': 49},
            {'name': 'Boqvist', 'team': 'NJD', 'goals': 10, 'assists': 11},
            {'name': 'Bahl', 'team': 'NJD', 'goals': 2, 'assists': 6},
            {'name': 'Sharangovich', 'team': 'NJD', 'goals': 13, 'assists': 17},
            {'name': 'Foote', 'team': 'NJD', 'goals': 1, 'assists': 0},
            {'name': 'Okhotiuk', 'team': 'NJD', 'goals': 1, 'assists': 0},
            {'name': 'Hughes', 'team': 'NJD', 'goals': 43, 'assists': 56},
            {'name': 'Thompson', 'team': 'NJD', 'goals': 0, 'assists': 0},
            {'name': 'Mercer', 'team': 'NJD', 'goals': 27, 'assists': 29},
            {'name': 'Holtz', 'team': 'NJD', 'goals': 3, 'assists': 1},
            {'name': 'Hughes', 'team': 'NJD', 'goals': 1, 'assists': 1},
            {'name': 'Vanecek', 'team': 'NJD', 'goals': 0, 'assists': 0},
            {'name': 'Blackwood', 'team': 'NJD', 'goals': 0, 'assists': 0},
            {'name': 'Schmid', 'team': 'NJD', 'goals': 0, 'assists': 0}
        ]
        
        teamplayers_info = [{'name': player.name, 'team': player.team, 'goals': player.goals, 'assists': player.assists} for player in teamplayers]

        self.assertListEqual(teamplayers_info, NJD_teamplayers)

    def test_search_top(self):
        top3player = self.stats.top(3)

        correct_top3player = [
            {'name': 'McDavid', 'score': 153, 'goal': 64, 'assist': 89, 'team': 'EDM'},
            {'name': 'Draisaitl', 'score': 128, 'goal': 52, 'assist': 76, 'team': 'EDM'},
            {'name': 'Gretzky', 'score': 124, 'goal': 35, 'assist': 89, 'team': 'EDM'},
            {'name': 'Pastrnak', 'score': 113, 'goal': 61, 'assist': 52, 'team': 'BOS'}
        ]

        top3player_info = [{'name': player.name, 'score': player.points, 'goal': player.goals, 'assist': player.assists, 'team': player.team} for player in top3player]

        self.assertListEqual(top3player_info, correct_top3player)