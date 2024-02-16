from tabulate import tabulate
from colorama import Fore, Style

class TournamentView:
    def display_tournament_menu(self):
        """Display tournament main menu and return user's choice"""
        while True:
            print("\n----- Tournament Menu -----\n")
            print("1. " + Fore.BLUE + "Display Tournaments" + Style.RESET_ALL)
            print("2. " + Fore.BLUE + "Create Tournament" + Style.RESET_ALL)
            print("3. " + Fore.BLUE + "Display Players" + Style.RESET_ALL)
            print("4. " + Fore.BLUE + "Generate Round 1 Matches" + Style.RESET_ALL)
            print("5. " + Fore.BLUE + "Generate Next Round Matches" + Style.RESET_ALL)
            print("6. " + Fore.BLUE + "Start Tournament" + Style.RESET_ALL)
            print("7. " + Fore.BLUE + "Update Player Scores" + Style.RESET_ALL)
            print("8. " + Fore.BLUE + "Display Tournament Results" + Style.RESET_ALL)
            print("9. " + Fore.BLUE + "Exit" + Style.RESET_ALL)

            choice = input("\nEnter your choice: ")

            if choice in ["1", "2", "3", "4", "5"]:
                return choice
            else:
                print("Invalid choice. Please try again.")

    def get_tournament_data(self):
        tournament_id = input("Enter tournament id: ")
        name = input("Enter tournament name: ")
        location = input("Enter tournament location: ")
        start_date = input("Enter tournament start date: ")
        end_date = input("Enter tournament end date: ")
        nb_rounds = input("Enter the number of rounds: ")
        description = input("Enter tournament description: ")

        details = {
            "tournament_id": tournament_id,
            "name": name,
            "location": location,
            "start_date": start_date,
            "end_date": end_date,
            "nb_rounds": nb_rounds,
            "description": description,
        }

        return details

    def display_tournaments(self, tournaments):
        """Display the list of tournaments"""
        if not tournaments:
            print("No tournaments found.")
            return

        headers = [
            "ID",
            "Name",
            "Location",
            "Start Date",
            "End Date",
            "Number of Rounds",
            "Actual Round",
            "Description",
        ]
        tournament_data = [
            [
                tournament.tournament_id,
                tournament.name,
                tournament.location,
                tournament.start_date,
                tournament.end_date,
                tournament.nb_rounds,
                tournament.actual_round,
                tournament.description,
            ]
            for tournament in tournaments
        ]

        # Colorize the headers
        colorized_headers = [
            Fore.GREEN + header + Style.RESET_ALL for header in headers
        ]

        # Colorize the tournament data
        colorized_tournament_data = [
            [
                Fore.RED + tournament_id + Style.RESET_ALL,
                name,
                location,
                start_date,
                end_date,
                nb_rounds,
                actual_round,
                description,
            ]
            for (
                tournament_id,
                name,
                location,
                start_date,
                end_date,
                nb_rounds,
                actual_round,
                description,
            ) in tournament_data
        ]

        print(tabulate(colorized_tournament_data, headers=colorized_headers))

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

        print(tabulate(colorized_player_data, headers=colorized_headers))

    def display_round_matches(self, round_number, matches):
        """Display the matches for a round"""
        print(f"\n--- Round {round_number} Matches ---")
        if not matches:
            print("No matches found.")
            return

        headers = ["Match Number", "Player 1", "Player 2"]
        match_data = [
            [f"Match {i + 1}", match.player1.full_name, match.player2.full_name]
            for i, match in enumerate(matches)
        ]

        # Colorize the headers
        colorized_headers = [
            Fore.GREEN + header + Style.RESET_ALL for header in headers
        ]

        # Colorize the match data
        colorized_match_data = [
            [
                Fore.RED + match_number + Style.RESET_ALL,
                player1,
                player2,
            ]
            for match_number, player1, player2 in match_data
        ]

        print(tabulate(colorized_match_data, headers=colorized_headers))

    def display_match_result_form(self, match):
        print(f"\n--- Enter Match Result ---")
        print(f"Match: {match.player1.full_name} vs {match.player2.full_name}")
        result = input("Enter the match result: ")
        return result



if __name__ == "__main__":
    tournament_view = TournamentView()
    #tournament_view.display_tournament_menu()
    #tournament_view.get_tournament_data()
    tournament_view.display_tournaments()
    tournament_view.get_player_id()
    tournament_view.display_message("Test message")
    tournament_view.display_players()
    tournament_view.display_round_matches()
    tournament_view.display_match_result_form()
    