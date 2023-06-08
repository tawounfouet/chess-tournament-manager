
class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.result = None

    def record_result(self, score_player1, score_player2):
        self.result = (score_player1, score_player2)

    def display_information(self):
        print(f"Player 1: {self.player1.first_name} {self.player1.last_name}")
        print(f"Player 2: {self.player2.first_name} {self.player2.last_name}")
        if self.result:
            print(f"Result: {self.result[0]} - {self.result[1]}")
        else:
            print("Result: N/A")

