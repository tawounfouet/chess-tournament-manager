from views.tournament import ViewTournament



from models.player import Player


import datetime


class TournamentController:
    """The TournamentController class is the controller for the tournament menu."""

    def __init__(self):
        """Initialize the TournamentController class."""
        self.tournament_view = ViewTournament()
     

    def handle_tournament_menu(self):
        """Display the tournament menu and manage user choice."""

        exit_requested = False

        while not exit_requested:
            choice = self.tournament_view.display_tournament_menu()

            if choice == "1":
                # create new tournament
                self.create_tournament()
                # register players to the tournament
                self.add_player_to_tournament()            

            elif choice == "2":
                # load a tournament
                self.load_tournament()
            elif choice == "3":
                # list tournaments by date
                self.list_tournaments_by_date()
            elif choice == "4":
                # list rounds of a tournament
                self.list_rounds_of_tournament()
            elif choice == "5":
                # list pairings of a round
                self.list_pairings_of_round()
            elif choice == "6":
                # add player to tournament
                self.add_player_to_tournament(self.tournament)
            elif choice == "7":
                # go back to main menu
                exit_requested = True
            else:
                print("Invalid choice. Please try again.")
                print()
                continue

        def create_tournament(self):
            tournament_data = self.view.get_tournament_data()
            self.model = Tournament(**tournament_data)
            self.model.save_to_db()

            self.view.display_message(f"Tournament {self.model.name} created successfully.")

    # def add_player_to_tournament(self, tournament):
    #     """Add a player to the tournament."""
    #     player_id = input("Enter player's ID: ")

    #     # Search for the player in the database using their ID
    #     player = Player.get_by_id(player_id)

    #     if player:
    #         # Check if the player is already registered in the tournament
    #         if player in tournament.players:
    #             print("Player is already registered in the tournament.")
    #         else:
    #             # Add the player to the tournament
    #             tournament.players.append(player)
    #             print(f"Player {player_id} added to the tournament.")
    #             # Save the updated tournament data to the database
    #             tournament.save_to_db()
    #     else:
    #         print("Player not found.")
        

    def add_player_to_tournament(self, tournament):
        """Add players to the tournament."""
        while True:
            player_id = input("Enter player's ID (or 'q' to quit): ")

            if player_id.lower() == 'q':
                break

            # Search for the player in the database using their ID
            player = Player.get_by_id(player_id)

            if player:
                # Check if the player is already registered in the tournament
                if player in tournament.players:
                    print("Player is already registered in the tournament.")
                else:
                    # Add the player to the tournament
                    tournament.players.append(player)
                    print(f"Player {player_id} added to the tournament.")
            else:
                print("Player not found.")

        # Save the updated tournament data to the database
        tournament.save_to_db()


    def load_tournament(self):
        """Load a tournament."""
        tournament_id = input("Enter tournament ID to load: ")
        tournament = self.tournament_model.find_by_id(tournament_id)  # Call find_by_id as a class method
        if tournament:
            self.tournament = tournament
            print(f"Tournament {tournament.name} loaded successfully.")
        else:
            print("Tournament not found.")

    def list_rounds_of_tournament(self):
        """List rounds of a tournament."""
        if not self.tournament:
            print("Error: No tournament loaded.")
            return

        print(f"Rounds of Tournament {self.tournament.name}:")
        for round_obj in self.tournament.round_list:
            print(f"{round_obj.name} - Start Date: {round_obj.start_date}")

    def list_pairings_of_round(self):
        """List pairings of a round."""
        round_name = input("Enter round name to list pairings: ")
        round_obj = self.tournament.get_round_by_name(
            round_name
        )  # Assuming a method to get a round by name
        if round_obj:
            print(f"Pairings for Round {round_name}:")
            for match in round_obj.matches:
                print(f"{match.player1.name} vs {match.player2.name}")
        else:
            print("Round not found.")

    def list_tournaments_by_date(self):
        """List tournaments by date."""
        tournaments = (
            Tournament.get_all_sorted_by_date()
        )  # Assuming a method to get all tournaments sorted by date
        if tournaments:
            print("Tournaments by Date:")
            for tournament in tournaments:
                print(f"{tournament.name} - Start Date: {tournament.start_date}")
        else:
            print("No tournaments found.")

    def create_round(self, players, current_round):
        """Create a new round."""
        name = f"Round {current_round}"
        date = datetime.now().strftime("%d/%m/%Y")
        matches = []

        # Generate matches with available players
        while len(players) > 0:
            player_1 = players.pop(0)
            player_2 = players.pop(0) if players else None
            match = Match(player_1=player_1, player_2=player_2)
            matches.append(match)

        round = Round(name=name, start_date=date, matches=matches)
        return round

    def get_matches_list(self, round):
        """Display matches with pair of players."""

    def add_scores_to_tournament(self, round):
        """Add scores to the tournament."""
        for match in round.matches:
            choice = input(
                f"Enter the score for match {match.player_1} vs {match.player_2}: "
            )
            if choice == "1":
                match.p1_score = 1
            elif choice == "2":
                match.p2_score = 1
            elif choice == "3":
                match.p1_score = 0.5
                match.p2_score = 0.5
        round.status = "Done"
        print("Scores added successfully.")

        date = date.strftime("%d/%m/%Y")
        round.status = "Done"
        self.view.display_message(f"Round terminé")

        def resume_tournament(self, tournament):
            """Resume the tournament."""
            pass
