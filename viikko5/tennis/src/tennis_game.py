class TennisGame:
    WIN = 4
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self._get_scoresequal()
        elif self.player1_score >= self.WIN or self.player2_score >= self.WIN:
            return self._check_win_or_advantage()
        else:
            return self._get_regular_scores()

    def _get_scoresequal(self):
        if self.player1_score == 0:
            return "Love-All"
        elif self.player1_score == 1:
            return "Fifteen-All"
        elif self.player1_score == 2:
            return "Thirty-All"
        else:
            return "Deuce"

    def _check_win_or_advantage(self):
        delta_result = self.player1_score - self.player2_score

        if delta_result == 1:
            return "Advantage player1"
        elif delta_result == -1:
            return "Advantage player2"
        elif delta_result >= 2:
            return "Win for player1"
        else:
            return "Win for player2"

    def _get_regular_scores(self):
        score = ""

        for i in range(1, 3):
            if i == 1:
                current_score = self.player1_score
            else:
                score += "-"
                current_score = self.player2_score

            score += self._get_score_description(current_score)

        return score

    def _get_score_description(self, current_score):
        if current_score == 0:
            return "Love"
        elif current_score == 1:
            return "Fifteen"
        elif current_score == 2:
            return "Thirty"
        elif current_score == 3:
            return "Forty"
