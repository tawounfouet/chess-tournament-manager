
import sys
sys.path.append("/Users/awf/Projects/openclassrooms/DA. Python _ OCR/P4 - POO - Jeu d'echecs/chess_tournament")

# Importing modules
from models.tournament import Tournament
from models.player import Player


class Report:
    def __init__(self):
        self.players = Player.get_all_players()
        self.tournaments = Tournament.get_all_tournaments()

    @staticmethod
    def players_alphabetical(players):
        sorted_players = sorted(players, key=lambda player: player.last_name)
        report = "List of Players (Alphabetical Order):\n\n"
        for player in sorted_players:
            report += f"{player.first_name} {player.last_name}\n"
        return report

    @staticmethod
    def tournament_list(tournaments):
        report = "List of Tournaments:\n\n"
        for tournament in tournaments:
            report += f"{tournament.name}\n"
        return report

    @staticmethod
    def tournament_details(tournament):
        report = f"Tournament Details:\n\nName: {tournament.name}\n"
        report += f"Start Date: {tournament.start_date}\n"
        report += f"End Date: {tournament.end_date}\n"
        return report

    @staticmethod
    def tournament_players_alphabetical(tournament):
        sorted_players = sorted(tournament.players, key=lambda player: player.last_name)
        report = f"List of Players in Tournament '{tournament.name}' (Alphabetical Order):\n\n"
        for player in sorted_players:
            report += f"{player.first_name} {player.last_name}\n"
        return report

    @staticmethod
    def tournament_rounds_and_matches(tournament):
        report = f"Tournament Rounds and Matches for '{tournament.name}':\n\n"
        for round in tournament.rounds_results:
            report += f"Round {round.round_number}:\n"
            for match in round.matches:
                player1 = match[0]
                player2 = match[2]
                report += f"{player1.first_name} {player1.last_name} vs. {player2.first_name} {player2.last_name}\n"
            report += "\n"
        return report

    @staticmethod
    def tournament_results(tournament):
        report = f"Tournament Results for '{tournament.name}':\n\n"
        for round in tournament.rounds_results:
            report += f"Round {round.round_number}:\n"
            for match in round.matches:
                player1 = match[0]
                player2 = match[2]
                report += f"{player1.first_name} {player1.last_name} ({match[1]}) vs. {player2.first_name} {player2.last_name} ({match[3]})\n"
            report += "\n"
        return report


# Instantiate the controller
if __name__ == "__main__":
    rp = Report()
    print(rp.players_alphabetical(rp.players))
    print(rp.tournament_list(rp.tournaments))
