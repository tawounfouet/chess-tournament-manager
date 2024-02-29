from tinydb import TinyDB, Query
import uuid


from models.player import Player
from models.round import Round
from models.match import Match

# from controllers.round import RoundController

from models.tournament import Tournament
from views.tournament import TournamentView

from datetime import datetime
import random


class TournamentController:
    def __init__(self):
        self.view = TournamentView()
        self.tournament = None
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
                self.create_tournament()
            elif choice == "2":
                self.view.display_tournaments(self.tournaments)
            elif choice == "3":
                # display tournament info using tournament ID
                tournament_id = input("Enter tournament ID to load: ")
                self.view.display_tournament_info(tournament_id)

            elif choice == "4":
                # consulter la liste des rounds d'un tournoi
                tournament_id = input("Enter tournament ID to view rounds: ")
                self.view.display_rounds_list(tournament_id)
                exit_requested = True
                

            else:
                self.view.display_message("Invalid choice. Please try again.")

    def create_tournament(self):
        tournament_data = self.view.get_tournament_data()
        self.tournament = Tournament(**tournament_data)
        
        
        self.view.display_players(self.players)

        # Add players to the tournament
        player_ids = self.view.get_player_ids_to_add()
        players_to_add = [Player.get_player_by_id(id_db)  for id_db in player_ids]
        # players_to_add = [player_id for player_id in player_ids]
        self.tournament.players = players_to_add

        
        #print(f"Players: {self.tournament.players}")
        #self.tournament.save_to_db()
        
        #self.tournament.id_db = 
        #self.tournament.tournament_id = str(uuid.uuid4())
       
       

        # Generate rounds
        rounds = self.generate_rounds(players_to_add)
        self.tournament.rounds = rounds
        self.tournament.save_to_db()

        # Display tournament results
        self.view.display_message(f"Tournament {self.tournament.name} created successfully.")

        start_round = input("Do you want to start Round 1? (y/n): ")
        if start_round.lower() == "y":
            self.start_round(self.tournament)


    



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


    def start_round(self, tournament):
        round_1 = tournament.rounds[0]
        self.view.display_message("Players for Round 1:")
        for match in round_1.matches:
            # print(f"{match.player_1.full_name} vs {match.player_2.full_name}")
            print(f"{match.player_1} vs {match.player_2}")

        save_scores = input("Do you want to save the scores? (y/n): ")
        if save_scores.lower() == "y":
            self.save_scores_to_tournament(tournament)

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



    def generate_matches(self, players):
        """Generate matches for a round."""
        matches = []
        num_players = len(players)

        # Shuffle players for random pairing
        random.shuffle(players)

        for i in range(0, num_players, 2):
            player_1 = players[i]["id_db"]
            player_2 = players[i + 1]["id_db"] if i + 1 < num_players else None
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


    def save_scores_to_tournament(self, tournament):
        """Run a round and prompt for scores."""
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


    # def display_rounds_list(self, tournament_id):
    #     """Display the list of rounds for a tournament."""
    #     db_tournaments = TinyDB("data/tournaments.json", indent=4)
    #     tournaments_table = db_tournaments.table("tournaments")

    #     # Recherche du tournoi par son identifiant
    #     tournament_record = tournaments_table.get(doc_id=tournament_id)
    #     if tournament_record:
    #         rounds = tournament_record.get('rounds', [])
    #         if rounds:
    #             print(f"Rounds for Tournament {tournament_record['name']}:")
    #             for round_data in rounds:
    #                 print(f"- {round_data['name']}")
    #         else:
    #             print("No rounds found for this tournament.")
    #     else:
    #         print("Tournament not found.")


    # def display_rounds_list(self, tournament_id):
    #     """Display the list of rounds and matches for a tournament."""
    #     db_tournaments = TinyDB("data/tournaments.json", indent=4)
    #     tournaments_table = db_tournaments.table("tournaments")

    #     # Recherche du tournoi par son identifiant
    #     tournament_record = tournaments_table.get(doc_id=tournament_id)
    #     if tournament_record:
    #         rounds = tournament_record.get('rounds', [])
    #         if rounds:
    #             print(f"Rounds for Tournament {tournament_record['name']}:")
    #             for round_data in rounds:
    #                 print(f"- {round_data['name']}")
    #                 matches = round_data.get('matches', [])
    #                 if matches:
    #                     print("  Matches:")
    #                     for match_data in matches:
    #                         print(f"    {match_data['player_1']} vs {match_data['player_2']}")
    #                 else:
    #                     print("  No matches found for this round.")
    #         else:
    #             print("No rounds found for this tournament.")
    #     else:
    #         print("Tournament not found.")


if __name__ == "__main__":
    """Test TournamentController class"""
    tc = TournamentController()
    tc.handle_tournament_menu()
