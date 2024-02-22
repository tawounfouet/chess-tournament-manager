class MatchModel:
    def __init__(self, name, paired_players, winner):
        self.name = name
        self.player1 = paired_players[0]
        self.player2 = paired_players[1]
        self.winner = winner

    def serializer(self):
        match = {
            "name": self.name,
            "players": [self.player1, self.player2],
            "score": [{self.player1: 0}, {self.player2: 0}],
            "winner": self.winner,
        }
        return match