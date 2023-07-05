from models.tournament import Tournament
from views.tournament import TournamentView

from models.player import Player
from views.player import PlayerView


class TournamentController:
    """Tournament controller class"""

    def __init__(self):
        self.view = TournamentView()
        self.model = Tournament

    def handle_tournament_menu(self):
        """Handle tournament menu"""

        while True:
            choice = self.view.display_tournament_menu()

            if choice == "1":
                self.create_tournament()
            elif choice == "2":
                self.display_tournaments()
            elif choice == "3":
                break

    def create_tournament(self):
        """Create a new tournament"""

        tournament_info = self.view.get_tournament_info()
        tournament = self.model(**tournament_info)
        tournament.save_to_db()

        print("\nTournament created successfully.")

    def display_tournaments(self):
        """Display all tournaments"""

        tournaments = self.model.get_all_tournaments()
        self.view.display_tournaments(tournaments)

    def add_player_to_tournament(self, tournament):
        player_id = self.view.get_player_id()
        player = Player.get_player_by_id(player_id)

        if player is not None:
            # tournament.add_player(player)
            self.players.append(player)
            self.view.display_message(
                f"Player {player.full_name} added to the tournament."
            )
        else:
            self.view.display_message("Player not found.")


if __name__ == "__main__":
    """Test PlayerController class"""
    tc = TournamentController()
    tc.handle_tournament_menu()
