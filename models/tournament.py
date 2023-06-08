
from tinydb import TinyDB, Query


db_tournaments = TinyDB('data/tournaments.json')

class Tournament:

    def __init__(self, name, start_date, end_date) :
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.registered_players = []
        self.rounds = []

    def add_player(self, player):
        self.registered_players.append(player)

    def generate_match_pairs(self, round_number):
        # Logic to generate match pairs for a given round
        pass

    def update_scores(self):
        # Logic to update players' scores after each match
        pass

    def display_information(self):
        print(f"Tournament Name: {self.name}")
        print(f"Start Date: {self.start_date}")
        print(f"End Date: {self.end_date}")
        print("Registered Players:")
        for player in self.registered_players:
            print(player)


    def save_to_db(self):
        tournament_table = db_tournaments.table('tournaments')
        tournament_query = Query()
        existing_tournament = tournament_table.get(tournament_query.name == self.name)
        if existing_tournament is None:
            tournament_data = {
                'name': self.name,
                'start_date': self.start_date,
                'end_date': self.end_date
            }
            tournament_table.insert(tournament_data)


    def update_score_in_db(self):
        """ Update tournament's score in database"""
        tournament_table = db_tournaments.table('tournaments')
        tournament_table.update({'score': self.score}, Query().name == self.name)

if __name__ == "__main__":
    tournament1 = Tournament("Tournoi de Paris", "07/09/2021", "08/09/2021")
    tournament1.save_to_db()
    
    tournament1.add_player("player1")
    tournament1.add_player("player2")
    tournament1.add_player("player3")
    tournament1.add_player("player4")

    tournament1.display_information()

