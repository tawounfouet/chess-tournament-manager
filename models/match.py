from tinydb import TinyDB, Query


class Match:
    def __init__(self, player_1, player_2, p1_score=0, p2_score=0):
        self.player_1 = player_1
        self.player_2 = player_2
        self.p1_score = p1_score
        self.p2_score = p2_score

    def serialize(self):
        return {
            "player_1": self.player_1,
            "player_2": self.player_2,
            "p1_score": self.p1_score,
            "p2_score": self.p2_score,
        }
    
    def __str__(self):
        return f"{self.player_1}: {self.p1_score} - {self.p2_score} :{self.player_2}"
    

 