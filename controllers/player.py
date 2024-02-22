from models.player import Player
from views.player import ViewPlayer
import random

from tinydb import Query


class PlayerController:
    """The PlayerController class is the controller for the player menu."""

    def __init__(self):
        """Initialize the PlayerController class."""
        self.player_view = ViewPlayer()
        #self.players = []
        # Load players from the database
        self.player_model = Player
        self.players = self.load_players()
        
        
    def handle_player_menu(self):
        """Display the player menu and manage user choice."""
        
        exit_requested = False
        
        while not exit_requested:
            choice = self.player_view.display_player_menu()
            
            if choice == "1":
                # create new player
                self.create_player()
            elif choice == "2":
                # modify player
                self.update_player()
            elif choice == "3":
                # liste players by name
                self.list_players_by_name()
            elif choice == "4":
                # list players by rank
                self.list_players_by_rank()
            elif choice == "5":
                # go back to main menu
                exit_requested = True

        
    def create_player(self):
        """Create a new player."""
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
        player_id = input("Enter player ID: ")
        
        # Initialize the player with a random rank
        new_player = Player(first_name, last_name, date_of_birth, player_id)
        new_player.save_to_db()

        # Update the players list
        #self.players.append(new_player)
        print(f"Player {new_player.full_name} created successfully ")


    def update_player(self):
        """Modify a player."""
        player_id = input("Enter player ID to update: ")
        player = self.player_model.players_table.get(Query().player_id == player_id)
        if player:
            print("Found player:")
            print(player)
            first_name = input("Enter new first name (leave empty to keep existing): ")
            last_name = input("Enter new last name (leave empty to keep existing): ")
            date_of_birth = input("Enter new date of birth (YYYY-MM-DD) (leave empty to keep existing): ")

            if first_name:
                player.first_name = first_name
            if last_name:
                player.last_name = last_name
            if date_of_birth:
                player.date_of_birth = date_of_birth

            player.update()
            print("Player updated successfully")
        else:
            print("Player not found")


    def load_players(self):
        """Load players from the database."""
        players = self.player_model.players_table.all()
        if players:
            return players
        else:
            return []

    def list_players_by_name(self):
        """List players by name."""
        players_data = self.player_model.players_table.all()
        if players_data:
            players = [self.player_model.deserialize(player) for player in players_data]
            players_sorted = sorted(players, key=lambda p: p.full_name)
            print("\nPlayers sorted by name:")
            for player in players_sorted:
                print("- ", player)
            print()
        else:
            print("No players found")


    def list_players_by_rank(self):
        """List players by rank."""
        pass
        # sorted_players = sorted(self.players, key=lambda p: p.rank)
        # for index, player in enumerate(sorted_players, start=1):
        #     print(f"{index}. {player.full_name} - Rank: {player.rank}")






if __name__ == "__main__":
    print("Executing player controller.py")
    player_controller = PlayerController()
    player_controller.handle_player_menu()

