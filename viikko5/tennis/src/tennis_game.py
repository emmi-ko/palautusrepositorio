class TennisGame:
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
        current_score = ""
        winning_points = 4

        if self.player1_score == self.player2_score:
            current_score = self.get_draw_score()

        elif self.player1_score >= winning_points or self.player2_score >= winning_points:
            current_score = self.check_if_winner(self.player1_score - self. player2_score)
 
        else:
            current_score += self.get_player_score(self.player1_score) + "-" + self.get_player_score(self.player2_score)

        return current_score

    def get_draw_score(self):
        if self.player1_score == 0:
            return "Love-All"
        elif self.player1_score == 1:
            return "Fifteen-All"
        elif self.player1_score == 2:
            return "Thirty-All"
        else:
            return "Deuce"

    def check_if_winner(self, difference):
        if difference == 1:
            return "Advantage player1"
        elif difference == -1:
            return "Advantage player2"
        elif difference >= 2:
            return "Win for player1"
        else:
            return "Win for player2"


    def get_player_score(self, player_score):
        if player_score == 0:
            return "Love"
        elif player_score == 1:
            return "Fifteen"
        elif player_score == 2:
            return "Thirty"
        elif player_score == 3:
            return "Forty"
