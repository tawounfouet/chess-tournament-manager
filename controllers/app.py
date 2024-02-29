import sys
from config import ROOT_DIR

sys.path.append(ROOT_DIR)

# print(sys.path)
# print(ROOT_DIR)

from views.view_app import ViewApp
from chess_game.controllers.tournament import TournamentController
from chess_game.controllers.player import PlayerController
# from chess_game.controllers.round import RoundController


class AppController:
    """The AppController class is the main controller for the application."""

    def __init__(self):
        """Initialize the AppController class."""
        self.view_app = ViewApp()
        self.tournament_controller = TournamentController()
        #self.round_controller = RoundController()
        self.player_controller = PlayerController()

    def start(self):
        """Display the main menu and manage user choice."""
        exit_requested = False

        while not exit_requested:
            choice = self.view_app.display_main_menu()

            if choice == "1":
                # go to tournament menu
                self.tournament_controller.handle_tournament_menu()
            elif choice == "2":
                # go to player menu
                self.player_controller.handle_player_menu()
            elif choice == "3":
                # go to round menu
                # self.round_controller.handle_round_menu()
                pass
            elif choice == "4":
                exit_requested = True


if __name__ == "__main__":
    print("Executing app.py")
    # app = AppController()
    # app.start()

    # def start(self):
    #     """Start the application."""
    #     self.view_app.start()
    #     self.tournament_controller.start()
    #     self.player_controller.start()
    #     self.view_app.end()
