# Player View

# pip install colorama tabulate
from tabulate import tabulate
from colorama import Fore, Style


class PlayerView:
    def display_player_menu(self):
        """Display player main menu and return user's choice"""

        while True:
            print("\n----- Player Menu -----\n")
            print("1. " + Fore.BLUE + "Create Player" + Style.RESET_ALL)
            print("2. " + Fore.BLUE + "Update Player" + Style.RESET_ALL)
            print("3. " + Fore.BLUE + "Display Players" + Style.RESET_ALL)
            print("4. " + Fore.BLUE + "Exit" + Style.RESET_ALL)

            choice = input("\nEnter your choice: ")

            if choice in ["1", "2", "3", "4"]:
                return choice
            else:
                print("Invalid choice. Please try again.")

    def get_infos_player(self):
        first_name = input("Enter player's first name: ")
        last_name = input("Enter player's last name: ")
        date_of_birth = input("Enter player's date of birth: ")
        player_id = input("Enter player's id: ")

        infos = {
            "first_name": first_name,
            "last_name": last_name,
            "date_of_birth": date_of_birth,
            "player_id": player_id,
        }

        return infos

    def get_player_id(self):
        player_id = input("Enter player's id: ")
        return player_id


    def display_message(self, message):
        print(message)



    def display_players(self, players):
        """Display the list of players"""
        if not players:
            print("No players found.")
            return

        headers = ["ID", "First Name", "Last Name", "Date of Birth", "Score"]
        player_data = [
            [
                player.player_id,
                player.first_name,
                player.last_name,
                player.date_of_birth,
                player.score,
            ]
            for player in players
        ]

        # Colorize the headers
        colorized_headers = [
            Fore.GREEN + header + Style.RESET_ALL for header in headers
        ]

        # Colorize the player data
        colorized_player_data = [
            [
                Fore.RED + player_id + Style.RESET_ALL,
                first_name,
                last_name,
                date_of_birth,
                score,
            ]
            for player_id, first_name, last_name, date_of_birth, score in player_data
        ]

        # print(tabulate(player_data, headers=headers))
        print(tabulate(colorized_player_data, headers=colorized_headers))


if __name__ == "__main__":
 """Test PlayerView class"""

view = PlayerView()
    
# Test display_player_menu
print(view.display_player_menu())

# Test get_infos_player
print(view.get_infos_player())

# # Test get_player_id
# print(view.get_player_id())

# # Test display_message
# view.display_message("This is a test message.")

# # Test display_players
# from models.player import Player
# players = [
#     Player("John", "Doe", "1990-01-01", "1", 0),
#     Player("Jane", "Doe", "1995-01-01", "2", 0),
# ]
# view.display_players(players)
