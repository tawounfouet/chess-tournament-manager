# Player Controller
"""Création de la classe PlayerController qui va gérer les actions sur les joueurs
 à partir de la classe Player et passer les informations à la classe PlayerView"""

from models.player import Player
from views.player import PlayerView

from tinydb import Query


class PlayerController:
    def __init__(self):
        self.view = PlayerView()
        self.model = Player

    def handle_player_menu(self):
        """Handle player menu"""
        exist_requested = False

        while not exist_requested:
            choice = self.view.display_player_menu()

            if choice == "1":
                self.create_player()
            elif choice == "2":
                self.update_player()
            elif choice == "3":
                self.display_players()
            elif choice == "4":
                break

    def create_player(self):
        player_infos = self.view.get_infos_player()
        player = Player(**player_infos)

        player.save_to_db()

        self.view.display_message(
            f"Le joueur {player.full_name}  a été créé avec succès"
        )

    def update_player(self):
        player_id = self.view.get_player_id()
        new_score = self.view.get_new_score()

        player = self.model.get_player_by_id(player_id)

        if player is not None:
            player.update_score(new_score)

            self.view.display_message(
                f"Player {player.player_id} information updated successfully."
            )
        else:
            self.view.display_message("Player not found.")

    def display_players(self):
        """Retrieve and display all players"""
        players = self.model.get_all_players()
        self.view.display_players(players)


if __name__ == "__main__":
    """Test PlayerController class"""
    pc = PlayerController()
    # pc.create_player()
    pc.handle_player_menu()
