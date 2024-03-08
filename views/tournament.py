from tabulate import tabulate
from colorama import Fore, Style
from tinydb import TinyDB, Query

class TournamentView:
    def __init__(self):
        self.db_tournaments = TinyDB("data/tournaments.json", indent=4)

    def display_tournament_menu(self):
        """Display tournament main menu and return user's choice"""
        while True:
            print("\n----- Tournament Menu -----\n")
            print("1. " + Fore.BLUE + "Create Tournament" + Style.RESET_ALL)
            print("2. " + Fore.BLUE + "Display Tournaments" + Style.RESET_ALL)
            print("3. " + Fore.BLUE + "Display a Tournament Info" + Style.RESET_ALL)
            print("4. " + Fore.BLUE + "Display the list of rounds for a tournament" + Style.RESET_ALL)
    
            
            print("6. " + Fore.BLUE + "Exit" + Style.RESET_ALL)

            choice = input("\nEnter your choice: ")
            #print("\n")

            if choice in ["1", "2", "3", "4", "5", "6"]:
                return choice
            else:
                print("Invalid choice. Please try again.")

    def get_tournament_data(self):
        #tournament_id = input("- Enter tournament id: ")
        name = input("- Enter tournament name: ")
        location = input("- Enter tournament location: ")
        start_date = input("- Enter tournament start date: ")
        end_date = input("- Enter tournament end date: ")
        # Ask the user for the number of rounds
        rounds_input = input("- Enter the number of rounds: ")
        nb_rounds = int(rounds_input) if rounds_input else 4
        # nb_of_players = int(input("Enter the number of players: "))  # Convert input to integer
        description = input("- Enter tournament description: ")

        details = {
            #"tournament_id": tournament_id,
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
            #"Start Date",
            #"End Date",
            "Number of Players",
            "Number of Rounds",
            #"Current Round",
            #"Description",
        ]

        tournament_data = [
            [
                tournament.tournament_id,
                tournament.name,
                tournament.location,
               #tournament.start_date,
                #tournament.end_date,
                tournament.number_of_players,
                tournament.nb_rounds,
                #tournament.current_round,
                #tournament.description,
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
                #start_date,
                #end_date,
                num_players,
                #num_of_rounds,
                nb_rounds,
                #actual_round,
                #description,
            ]
            for (
                tournament_id,
                name,
                location,
                #start_date,
                # end_date,
                num_players,
                #num_of_rounds,
                nb_rounds,
                #actual_round,
                #description,
            ) in tournament_data
        ]

        print(tabulate(colorized_tournament_data, headers=colorized_headers))


    def display_tournament_info(self, tournament_id):
        """Display all information about a tournament based on its ID"""
        tournaments_table = self.db_tournaments.table("tournaments")
        tournament_data = tournaments_table.get(Query().tournament_id == tournament_id)

        if not tournament_data:
            print(f"Tournament with ID {tournament_id} not found.")
            return

        headers = ["Attribute", "Value"]
        data = [
            ["Tournament ID", tournament_data["tournament_id"]],
            ["Name", tournament_data["name"]],
            ["Location", tournament_data["location"]],
            ["Start Date", tournament_data["start_date"]],
            ["End Date", tournament_data["end_date"]],
            ["Status", tournament_data["status"]],
            ["Description", tournament_data["description"]],
            ["Players", "\n".join(tournament_data["players"])],
            ["Number of Rounds", tournament_data["nb_rounds"]],
            ["Rounds", "\n".join([round_info["name"] for round_info in tournament_data["rounds"]])]
        ]

        colorized_data = [
            [Fore.GREEN + row[0] + Style.RESET_ALL, row[1]] for row in data
        ]

        print(tabulate(colorized_data, headers=headers, tablefmt="fancy_grid"))


    def get_player_id(self):
        player_id = input("Enter player's id: ")
        return player_id
    
    # def get_player_ids_to_add(self):
    #     # rahouter le nombre de joueur en parametre et plutot faire une boucle for pour demander le nombre de joueur
    #     """Prompt user to enter player IDs to add to the tournament"""
    #     player_ids = []
    #     while True:
    #         player_id = input("Enter player ID to add (press Enter to finish): ")
    #         if not player_id:  # Check if user pressed Enter without entering an ID
    #             break
    #         player_ids.append(player_id)
    #     return player_ids
    def get_player_ids_to_add(self):
        """Prompt user to enter player IDs to add to the tournament"""
        num_players_to_add = int(input("Enter the number of players to add: "))
        player_ids = []

        print(f"\n{Fore.YELLOW}Enter the IDs of {num_players_to_add} players:{Style.RESET_ALL}")

        for i in range(num_players_to_add):
            player_id = input(f"\tEnter ID for player {i+1}: ")
            player_ids.append(player_id)
        
        #print(f"\n{Fore.GREEN}Players added: {player_ids}{Style.RESET_ALL}\n")
        return player_ids



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
                player.date_of_birth.strftime('%Y-%m-%d'), 
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

        # Centered and styled title
        title = f"{Style.BRIGHT}{Fore.BLUE}List of Players:{Style.RESET_ALL}"
        title_width = len(title)
        padding = (80 - title_width) // 2
        formatted_title = f"{' ' * padding}{title}{' ' * padding}"

        print("\n")  # Add an empty line before the title
        print(formatted_title.center(80))  # Centered title
        print(tabulate(colorized_player_data, headers=colorized_headers, tablefmt="fancy_grid"))
        print("\n")  # Add an empty line after the player list

    

    def display_rounds_list(self, tournament_id):
        """Display the list of rounds and matches for a tournament."""
        db_tournaments = TinyDB("data/tournaments.json", indent=4)
        tournaments_table = db_tournaments.table("tournaments")

        # Recherche du tournoi par son identifiant
        tournament_record = tournaments_table.get(doc_id=tournament_id)
        if tournament_record:
            rounds = tournament_record.get('rounds', [])
            if rounds:
                print(Fore.CYAN + f"Rounds for Tournament {tournament_record['name']}:")
                round_data = []
                for round_info in rounds:
                    round_data.append([round_info['name'], round_info['start_date'], round_info['end_date'], round_info['status']])
                
                headers = ["Round Name", "Start Date", "End Date", "Status"]
                print(tabulate(round_data, headers=headers, tablefmt="pretty"))
                
                for round_info in rounds:
                    matches = round_info.get('matches', [])
                    if matches:
                        print(Fore.GREEN + f"Matches for Round {round_info['name']}:")
                        match_data = []
                        for match_info in matches:
                            match_data.append([match_info['player_1'], match_info['player_2'], match_info['p1_score'], match_info['p2_score']])
                        match_headers = ["Player 1", "Player 2", "Player 1 Score", "Player 2 Score"]
                        print(tabulate(match_data, headers=match_headers, tablefmt="pretty"))
                    else:
                        print(Fore.RED + "No matches found for this round.")
            else:
                print(Fore.RED + "No rounds found for this tournament.")
        else:
            print(Fore.RED + "Tournament not found.")


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
    """Test the TournamentView class."""
    # tournament_view = TournamentView()
    # #tournament_view.display_tournament_menu()
    # #tournament_view.get_tournament_data()
    # tournament_view.display_tournaments()
    # tournament_view.get_player_id()
    # tournament_view.display_message("Test message")
    # tournament_view.display_players()
    # tournament_view.display_round_matches()
    # tournament_view.display_match_result_form()
    