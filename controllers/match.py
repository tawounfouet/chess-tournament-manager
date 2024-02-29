from views.match import MatchView
from tinydb import TinyDB
from datetime import datetime

db_tournaments = TinyDB("db_tournaments.json").table("tournaments")


class Match:
    def __init__(self, rounds_number, current_round, tournament_doc_id):
        self.current_time = datetime.now().strftime("%d/%m/%Y-%H:%M")
        self.view = MatchView()
        self.rounds_number = rounds_number
        self.current_round = current_round
        self.tournament_doc_id = tournament_doc_id
        self.tournament = db_tournaments.get(doc_id=self.tournament_doc_id)

    def find_player(self, chess_id, score):
        players = self.tournament["players"]
        for player in players:
            if player["chess_id"] == chess_id:
                player["score"] = player["score"] + score

    def display_menu(self):
        self.view.custom_print(f"\nRound {self.current_round} sur {self.rounds_number}")
        round = self.tournament["rounds_list"][self.current_round - 1]
        matches = round["matches"]

        for match in matches:
            player1 = match["players"][0]
            player2 = match["players"][1]
            match_name = match["name"]
            self.view.custom_print(f"\n{match_name} : J1({player1}) vs J2({player2})")
            user_input = self.view.get_match_scores()

            if user_input == "1":  # P1 wins
                match["score"] = [{player1: 1}, {player2: 0}]
                match["winner"] = player1
                self.find_player(player1, 1)
            elif user_input == "2":  # P2 wins
                match["score"] = [{player1: 0}, {player2: 1}]
                match["winner"] = player2
                self.find_player(player2, 1)
            elif user_input == "3":  # Tie
                match["score"] = [{player1: 0.5}, {player2: 0.5}]
                match["winner"] = "Égalité"
                self.find_player(player1, 0.5)
                self.find_player(player2, 0.5)
            elif user_input == "4":
                return
            else:
                self.view.custom_print("Veuillez choisir une option valide")
                self.display_menu()

        round["end_time"] = self.current_time
        db_tournaments.update(self.tournament, doc_ids=[self.tournament_doc_id])