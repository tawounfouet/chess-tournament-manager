import sys
import os

# Define the root directory of the project
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(ROOT_DIR)

"""Round controller. """
from models.player import Player
from models.round import Round
from views.round import RoundView

import random
from datetime import datetime


class RoundController:
    def __init__(self, num_rounds=4):
        self.view = RoundView()
        self.model = Round
        self.num_rounds = num_rounds
        self.rounds = self.model.get_all_rounds()
        self.players = Player.get_all_players()
        self.matches = []

    def handle_round_menu(self):
        """Gère le menu du round"""
        exit_requested = False

        while not exit_requested:
            choice = self.view.display_round_menu()

            if choice == "1":
                self.create_round()
            elif choice == "2":
                self.display_rounds()
            elif choice == "3":
                self.generate_round_matches(current_round=round)
            elif choice == "4":
                self.update_scores()
            elif choice == "5":
                exit_requested = True
            else:
                self.view.display_message("Choix invalide. Veuillez réessayer.")



    def create_round(self):
        """Crée un nouveau round"""
        round_data = self.view.get_round_data()
        round = Round(**round_data)
        round.save_to_db()

        self.view.display_message(f"Round créé avec succès.")

        # Pass the newly created round as current_round argument
        self.generate_round_matches(current_round=round)

    

    def get_match_pairing(self, player_1, player_2):
        """Set match pairing as tuple"""
        match = (
            f"{player_1.player_id}, {player_1.first_name}",
            player_1.score,
            f"{player_2.player_id}, {player_2.first_name}",
            player_2.score,
        )
        self.matches.append(match)


    def generate_round_matches(self, current_round):
        """Generate matches for the current round"""
        matches = []

        #current_round = int(input("Enter current round: "))

        # Shuffle the players randomly at the beginning of the first round
        if current_round == 1:
            random.shuffle(self.players)

        # Sort the players based on their total points in the tournament
        sorted_players = sorted(
            self.players, key=lambda player: player.score, reverse=True
        )

        # Generate match pairs
        num_players = len(sorted_players)
        for i in range(0, num_players, 2):
            player_1 = sorted_players[i]
            player_2 = sorted_players[i + 1] if i + 1 < num_players else None

            # Avoid creating duplicate matches
            while player_2 is not None and self.is_duplicate_match(player_1, player_2):
                i += 1
                player_2 = sorted_players[i + 1] if i + 1 < num_players else None

            # Set match pairing
            if player_2 is not None:
                self.get_match_pairing(player_1, player_2)

        #return matches
        # Display matches
        print(matches)
        #self.view.display_matches(self.matches)
   


    def is_duplicate_match(self, player_1, player_2):
        """Check if a match between player_1 and player_2 already exists"""
        for match in self.matches:
            if (match[0] == player_1.player_id and match[2] == player_2.player_id) or (
                match[0] == player_2.player_id and match[2] == player_1.player_id
            ):
                return True
        return False
    


    def update_scores(self):
        """Met à jour les scores en fonction des résultats des matches"""
        if len(self.rounds) < self.num_rounds:
            self.view.display_message(
                "Veuillez créer tous les rounds et générer les matches d'abord."
            )
            return

        match_results = self.view.get_match_results()

        current_round = len(self.rounds)
        round_obj = self.rounds[current_round - 1]
        round_obj.update_scores(match_results)

        self.view.display_message("Les scores ont été mis à jour.")


    def display_rounds(self):
        """Retrieve and display all rounds"""
        rounds = self.model.get_all_rounds()
        self.view.display_rounds(rounds)

if __name__ == "__main__":
    """Test TournamentController class"""
    rc = RoundController()
    rc.handle_round_menu()
# Compare this snippet from controllers/round_old4.py:
