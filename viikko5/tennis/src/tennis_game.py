class TennisGame:
    REGULAR_WIN_THRESHOLD = 4
    DEUCE_PHASE_START_THRESHOLD = 3
    DEUCE_ADVANTAGE = 1
    DEUCE_WIN_THRESHOLD = 2

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.tennis_notation = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        if self.__is_deuce_phase():
            return self.__get_deuce_phase_score()
        else:
            return self.__get_regular_phase_score()

    def __is_deuce_phase(self):
        return self.player1_score >= TennisGame.DEUCE_PHASE_START_THRESHOLD and self.player2_score >= TennisGame.DEUCE_PHASE_START_THRESHOLD

    def __get_deuce_phase_score(self):
        difference = self.player1_score - self.player2_score
        leading_player = self.player1_name if difference > 0 else self.player2_name

        if difference == 0:
            return "Deuce"

        if abs(difference) == TennisGame.DEUCE_ADVANTAGE:
            return f"Advantage {leading_player}"
        if abs(difference) >= TennisGame.DEUCE_WIN_THRESHOLD:
            return f"Win for {leading_player}"

    def __get_regular_phase_score(self):
        if self.player1_score >= TennisGame.REGULAR_WIN_THRESHOLD:
            return f"Win for {self.player1_name}"
        if self.player2_score >= TennisGame.REGULAR_WIN_THRESHOLD:
            return f"Win for {self.player2_name}"

        if self.player1_score == self.player2_score:
            return f"{self.tennis_notation[self.player1_score]}-All"

        return f"{self.tennis_notation[self.player1_score]}-{self.tennis_notation[self.player2_score]}"
