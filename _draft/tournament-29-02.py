from tinydb import TinyDB, Query

from models.player import Player
from models.round import Round
from models.match import Match

# from controllers.round import RoundController

from models.tournament import Tournament
from views.tournament import TournamentView

from datetime import datetime
import random

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
        # self.round_controller = RoundController()

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
            elif choice == "6":
                self.start_tournament()
            elif choice == "7":
                tournament_id = input("Enter tournament ID to load: ")
                tournament = self.load_tournament(tournament_id)
                if tournament:
                    self.view.display_message(
                        f"Tournament {tournament.name} loaded successfully."
                    )
                    self.display_rounds(tournament)
                    self.display_matches(tournament)
                # go back to main menu
                exit_requested = True

            else:
                self.view.display_message("Invalid choice. Please try again.")

    def create_tournament(self):
        tournament_data = self.view.get_tournament_data()
        # self.model = Tournament(**tournament_data)
        tournament = Tournament(**tournament_data)
        self.view.display_players(self.players)
        # Display list of players
        # players = Player.get_all_players()
        # self.view.display_players(players)

        # Add players to the tournament
        player_ids = (
            self.view.get_player_ids_to_add()
        )  # Assuming this method prompts for player IDs
        # players_to_add = [Player.get_player_by_id(player_id)  for player_id in player_ids]
        players_to_add = [player_id for player_id in player_ids]
        tournament.add_players(players_to_add)

        # Save tournament to database
        self.model = tournament  # Initialiser l'attribut self.model
        self.model.save_to_db()

        # Generate rounds
        rounds = self.generate_rounds(players_to_add)
        tournament.rounds = rounds
        tournament.save_to_db()

        # Display tournament results
        # self.display_tournament_results()
        self.view.display_message(f"Tournament {self.model.name} created successfully.")

        # start_round = input("Do you want to start Round 1? (y/n): ")
        # if start_round.lower() == "y":
        #     round_1 = rounds[0]
        #     self.display_round_players(round_1)
        #     self.add_score_to_tournament(round_1)

        # save_scores = input("Do you want to save the scores? (y/n): ")
        # if save_scores.lower() == "y":
        #     self.save_scores_to_tournament(tournament)

        start_round = input("Do you want to start Round 1? (y/n): ")
        if start_round.lower() == "y":
            self.start_round(tournament)

    def start_round(self, tournament):
        round_1 = tournament.rounds[0]
        self.view.display_message("Players for Round 1:")
        for match in round_1.matches:
            # print(f"{match.player_1.full_name} vs {match.player_2.full_name}")
            print(f"{match.player_1} vs {match.player_2}")

        save_scores = input("Do you want to save the scores? (y/n): ")
        if save_scores.lower() == "y":
            self.save_scores_to_tournament(tournament)

    # def display_round_players(self, round):
    #     """Display the list of players in a round."""
    #     players = [match.player_1 for match in round.matches]
    #     self.view.display_players(players)

    def display_round_players(self, round):
        """Display the players for a specific round."""
        print(f"Players for {round.name}:")
        for match in round.matches:
            if match.player_2:
                print(f"{match.player_1.full_name} vs {match.player_2.full_name}")
            else:
                print(f"{match.player_1.full_name} (Bye)")

    def display_tournament_results(self):
        """Display tournament results"""
        self.view.display_tournament_results(self.model)

    def generate_rounds(self, players):
        """Generate rounds with matches for the tournament."""
        num_players = len(players)
        num_rounds = num_players - 1
        rounds = []

        for round_num in range(1, num_rounds + 1):
            round_name = f"Round {round_num}"
            start_date = datetime.now().strftime("%Y-%m-%d")
            end_date = None  # Set end date accordingly
            matches = self.generate_matches(players)
            status = ""  # Set status accordingly
            round = Round(
                name=round_name,
                start_date=start_date,
                end_date=end_date,
                matches=matches,
                status=status,
            )
            rounds.append(round)

        return rounds

    def generate_matches(self, players):
        """Generate matches for a round."""
        matches = []
        num_players = len(players)

        # Shuffle players for random pairing
        random.shuffle(players)

        for i in range(0, num_players, 2):
            player_1 = players[i]
            player_2 = players[i + 1] if i + 1 < num_players else None
            match = Match(player_1=player_1, player_2=player_2)
            matches.append(match)

        return matches

    # def generate_matches(self, players):
    #     """Generate matches for a round."""
    #     matches = []
    #     num_players = len(players)

    #     # Shuffle players for random pairing
    #     random.shuffle(players)

    #     for i in range(0, num_players, 2):
    #         player_1_id = players[i]
    #         player_2_id = players[i+1] if i+1 < num_players else None

    #         # Fetch Player objects based on their IDs
    #         player_1 = Player.get_player_by_id(player_1_id)
    #         player_2 = Player.get_player_by_id(player_2_id) if player_2_id else None

    #         match = Match(player_1=player_1, player_2=player_2)
    #         matches.append(match)

    #     return matches

    # def add_score_to_tournament(self, round: Round):
    #     """Add scores to matches in a round."""
    #     for match in round.matches:
    #         choice = input(f"Enter result for {match.player_1.full_name} vs {match.player_2.full_name}: "
    #                        "1 for Player 1, 2 for Player 2, 3 for Draw: ")
    #         if choice == "1":
    #             match.p1_score = 1
    #         elif choice == "2":
    #             match.p2_score = 1
    #         elif choice == "3":
    #             match.p1_score = 0.5
    #             match.p2_score = 0.5

    # def add_score_to_tournament(self, round):
    #     """Run a round and prompt for scores."""
    #     for match in round.matches:
    #         if match.player_2:
    #             choice = input(f"Enter result for {match.player_1.full_name} vs {match.player_2.full_name}: "
    #                         "1 for Player 1, 2 for Player 2, 3 for Draw: ")
    #             if choice == "1":
    #                 match.p1_score = 1
    #             elif choice == "2":
    #                 match.p2_score = 1
    #             elif choice == "3":
    #                 match.p1_score = 0.5
    #                 match.p2_score = 0.5

    # def save_scores_to_tournament(self, tournament):
    #     """Save scores to the tournament."""
    #     for round in tournament.rounds:
    #         for match in round.matches:
    #             match.save_to_db()

    def save_scores_to_tournament(self, tournament):
        for round in tournament.rounds:
            for match in round.matches:
                # choice = input(f"Enter result for {match.player_1.full_name} vs {match.player_2.full_name}: "
                choice = input(
                    f"Enter result for {match.player_1} vs {match.player_2}: "
                    "1 for Player 1, 2 for Player 2, 3 for Draw: "
                )
                if choice == "1":
                    match.p1_score = 1
                elif choice == "2":
                    match.p2_score = 1
                elif choice == "3":
                    match.p1_score = 0.5
                    match.p2_score = 0.5

                # match.save_to_db()

                # Update database records with new scores
                self.update_match_record_in_database(
                    tournament_id=tournament.tournament_id,
                    round_name=round.name,
                    player_1_id=match.player_1,
                    player_2_id=match.player_2,
                    p1_score=match.p1_score,
                    p2_score=match.p2_score,
                )

    def update_match_record_in_database(
        self, tournament_id, round_name, player_1_id, player_2_id, p1_score, p2_score
    ):
        """Update match record in the database."""
        db_tournaments = TinyDB("data/tournaments.json", indent=4)
        tournaments_table = db_tournaments.table("tournaments")

        # Create a Query object to locate the tournament by its tournament_id
        query = Query()
        tournament_record = tournaments_table.get(query.tournament_id == tournament_id)

        # Find the round within the tournament's rounds list
        for round_record in tournament_record["rounds"]:
            if round_record["name"] == round_name:
                # Find the match within the round's matches list
                for match in round_record["matches"]:
                    if (
                        match["player_1"] == player_1_id
                        and match["player_2"] == player_2_id
                    ):
                        # Update the scores for the match
                        match["p1_score"] = p1_score
                        match["p2_score"] = p2_score
                        # Update the tournament record in the database
                        tournaments_table.update(
                            tournament_record, doc_ids=[tournament_record.doc_id]
                        )
                        return

    def load_tournament(self, tournament_id):
        """Load a tournament from the database by its ID."""
        tournament = Tournament.get_tournament_by_id(tournament_id)
        if tournament:
            return tournament
        else:
            print("Tournament not found.")
            return None

    def display_rounds(self, tournament):
        """Display the list of rounds in a tournament."""
        rounds = tournament.rounds_results
        if not rounds:
            print("No rounds found.")
            return
        print("List of Rounds:")
        for round in rounds:
            print(f"- {round.name}")

    def display_matches(self, tournament):
        """Display the list of matches in a tournament."""
        rounds = tournament.rounds_results
        if not rounds:
            print("No matches found.")
            return
        print("List of Matches:")
        for round in rounds:
            print(f"Round: {round.name}")
            for match in round.matches:
                # print(f"  {match.player_1.full_name} vs {match.player_2.full_name}")
                print(f"  {match.player_1} vs {match.player_2}")


if __name__ == "__main__":
    """Test TournamentController class"""
    tc = TournamentController()
    tc.handle_tournament_menu()
