from models.player import Player
from models.round import Round
from controllers.round import RoundController
from models.tournament import Tournament
from views.tournament import TournamentView

from datetime import datetime

# Affecter la lister des match
# printer les match
# saisi des résultats (score) du tournois
# tirer les match du round 2
# Creation des matchs du rouund
# saisi le resulat des match avec 3 options
# voulez-vous lancer le round suivant
# voulez-vous saisi r les résultats

# creation du round, affectation des match, saisi des résulats --> En boucle 

# à la fin du dernier round montrer la liste des vainqueurs


# Fonction reprise d'un tournois (quel round c'est et dans quel état il est)
# - Fonctionnalité qui display une liste de tournois
# - saisi par l'utilisateur de l'ID 

# Rapport - une fonctionnamité du tournamentController 
# Gestions des rapports 

# créer une fonction dans la TournamentController pour gérer les rapport

class TournamentController:
    def __init__(self):
        self.view = TournamentView()
        self.model = Tournament
        self.players = Player.get_all_players()
        self.tournaments = Tournament.get_all_tournaments()
        self.round_controller = RoundController()

        self.timer = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def handle_tournament_menu(self):
        """Handle tournament menu"""
        exit_requested = False

        while not exit_requested:
            choice = self.view.display_tournament_menu()

            if choice == "1":
                self.view.display_tournaments(self.tournaments)
            elif choice == "2":
                self.create_tournament()
            elif choice == "3":
                self.view.display_players(self.players)
            elif choice == "4":
                self.first_round()
            elif choice == "5":
                self.generate_next_round_matches()
            elif choice == "6":
                self.start_tournament()
            elif choice == "7":
                self.update_player_scores()
            elif choice == "8":
                self.display_tournament_results()
            elif choice == "9":
                exit_requested = True
            else:
                self.view.display_message("Invalid choice. Please try again.")

    def create_tournament(self):
        tournament_data = self.view.get_tournament_data()
        self.model = Tournament(**tournament_data)
        self.model.save_to_db()

        self.view.display_message(f"Tournament {self.model.name} created successfully.")

    def first_round(self):
        """Generate matches for the first round"""
        self.round_controller.generate_round_matches(self.model, self.model.current_round)

    def next_round(self):
        """Generate matches for the next round"""
        self.round_controller.generate_round_matches(self.model, self.model.current_round)

    
    def get_scores(self):
        """Get scores for each match"""
        self.round_controller.get_scores(self.model)


    def update_player_scores(self):
        for round in self.model.rounds_results:
            for match in round.matches:
                player1, player2 = match
                result = self.view.get_match_result(player1, player2)

                if result == 1:
                    player1.update_score(1)
                    player2.update_score(0)
                elif result == 2:
                    player1.update_score(0)
                    player2.update_score(1)
                elif result == 3:
                    player1.update_score(0.5)
                    player2.update_score(0.5)


if __name__ == "__main__":
    """Test TournamentController class"""
    tc = TournamentController()
    tc.handle_tournament_menu()
