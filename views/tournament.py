class TournamentView:
    def __init__(self, controller):
        self.controller = controller

    def create_tournament_prompt(self):
        name = input("Enter the tournament name: ")
        location = input("Enter the tournament location: ")
        start_date = input("Enter the tournament start date (YYYY-MM-DD): ")
        end_date = input("Enter the tournament end date (YYYY-MM-DD): ")
        self.controller.create_tournament(name, location, start_date, end_date)

    def add_player_prompt(self):
        first_name = input("Enter the player's first name: ")
        last_name = input("Enter the player's last name: ")
        date_of_birth = input("Enter the player's date of birth (YYYY-MM-DD): ")
        self.controller.add_player(first_name, last_name, date_of_birth)

    def generate_matches(self):
        self.controller.generate_matches()

    def enter_match_results_prompt(self):
        results = []
        for match in self.controller.tournament.matches:
            print(f"Match: {match.player1.first_name} vs {match.player2.first_name}")
            score_player1 = input("Enter the score for player 1: ")
            score_player2 = input("Enter the score for player 2: ")
            results.append((score_player1, score_player2))
        self.controller.enter_match_results(results)

    def display_players(self):
        self.controller.display_players()

    def display_tournaments(self):
        self.controller.display_tournaments()
