from tinydb import TinyDB, Query

db_tournaments = TinyDB("data/tournaments.json", indent=4)


class Tournament:
    """Tournament class"""

    tournaments_table = db_tournaments.table("tournaments")

    def __init__(self, name, location, date, rounds):
        self.name = name
        self.location = location
        self.date = date
        self.rounds = rounds

    def save_to_db(self):
        """Save tournament data to database"""

        tournament_query = Query()
        existing_tournament = self.tournaments_table.get(
            tournament_query.name == self.name
        )
        if existing_tournament is None:
            tournament_data = {
                "name": self.name,
                "location": self.location,
                "date": self.date,
                "rounds": self.rounds,
            }
            self.tournaments_table.insert(tournament_data)
            print("\nTournament created successfully.")
        else:
            print("\nA tournament with the same name already exists.")

    @classmethod
    def get_all_tournaments(cls):
        """Retrieve all tournaments from the database"""

        tournaments_data = cls.tournaments_table.all()
        tournaments = []
        for tournament_data in tournaments_data:
            tournament = cls(**tournament_data)
            tournaments.append(tournament)
        return tournaments
