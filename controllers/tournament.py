from models import Player, Tournament, Match


class TournamentController:
    def __init__(self):
        self.tournament = None

    def create_tournament(self, name, location, start_date, end_date):
        self.tournament = Tournament(name, location, start_date, end_date)
        self.tournament.save_to_db()

    def add_player(self, first_name, last_name, date_of_birth):
        player = Player(first_name, last_name, date_of_birth)
        player.save_to_db()
        self.tournament.add_player(player)

    def generate_matches(self):
        # Implement your matching algorithm here
        for player1, player2 in match_pairs:
            match = Match(player1, player2)
            self.tournament.add_match(match)

    def enter_match_results(self, results):
        for index, match in enumerate(self.tournament.matches):
            score_player1, score_player2 = results[index]
            match.record_result(score_player1, score_player2)

    def display_players(self):
        for player in self.tournament.get_players():
            print(player.get_full_name())

    def display_tournaments(self):
        # Implement display of tournaments
        pass
