# from .match import Match

from tinydb import TinyDB, Query

db_rounds = TinyDB("data/rounds.json")


class Round:
    def __init__(self, round_number):
        self.round_number = round_number
        self.matches = []

    def add_match(self, player1, player2):
        match = Match(player1, player2)
        self.matches.append(match)

    def display_information(self):
        print(f"Round Number: {self.round_number}")
        print("Matches:")
        for match in self.matches:
            match.display_information()
            # print(match)

    def save_to_db(self):
        rounds_table = db_rounds.table("rounds")
        rounds_query = Query()
        existing_round = rounds_table.get(
            rounds_query.round_number == self.round_number
        )
        if existing_round is None:
            round_data = {
                "round_number": self.round_number,
                #'matches': [match.to_dict() for match in self.matches]
            }
            rounds_table.insert(round_data)


class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.result = None

    def record_result(self, score_player1, score_player2):
        self.result = (score_player1, score_player2)

    def display_information(self):
        print(f"{self.player1} vs  {self.player2}")
        if self.result:
            print(f"Result: {self.result[0]} - {self.result[1]}")
        else:
            print("Result: N/A")


if __name__ == "__main__":
    match1 = Match("player1", "player2")
    match1.record_result(1, 0)

    match2 = Match("player3", "player4")
    match2.record_result(1, 2)

    round1 = Round(1)
    round1.add_match("player1", "player2")
    round1.add_match("player3", "player4")
    round1.save_to_db()
    round1.display_information()
