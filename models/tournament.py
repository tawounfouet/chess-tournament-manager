from tinydb import TinyDB, Query

db_tournaments = TinyDB("data/tournaments.json", indent=4)


class Tournament:
    """Tournament class"""

    tournaments_table = db_tournaments.table("tournaments")

    def __init__(
        self,
        tournament_id,
        name,
        location,
        start_date,
        end_date,
        nb_rounds=4,
        actual_round=0,
        players=None,
        description="",
    ):
        self.tournament_id = tournament_id
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.nb_rounds = nb_rounds
        self.actual_round = actual_round
        self.players = players or []
        self.description = description
        
        self.rounds_results = []


    def save_to_db(self):
        """Save tournament data to database"""
        tournament_query = Query()
        existing_tournament = self.tournaments_table.get(
            tournament_query.tournament_id == self.tournament_id
        )
        if existing_tournament is None:
            tournament_data = {
                "tournament_id": self.tournament_id,
                "name": self.name,
                "location": self.location,
                "start_date": self.start_date,
                "end_date": self.end_date,
                "nb_rounds": self.nb_rounds,
                "actual_round": self.actual_round,
                "players": [player.__dict__ for player in self.players],
                "description": self.description,
            }
            self.tournaments_table.insert(tournament_data)
            print("\nTournament created successfully.")
        else:
            print("\nA tournament with the same ID already exists.")

    @classmethod
    def get_all_tournaments(cls):
        """Retrieve all tournaments from the database"""
        tournaments_data = cls.tournaments_table.all()
        tournaments = [cls(**data) for data in tournaments_data]
        return tournaments

    @classmethod
    def get_tournament_by_id(cls, tournament_id):
        """Retrieve a tournament from the database by tournament ID"""
        tournament_query = Query()
        tournament_data = cls.tournaments_table.get(
            tournament_query.tournament_id == tournament_id
        )
        if tournament_data:
            return cls(**tournament_data)
        else:
            return None


# test tournament.py using if __name__ == "__main__"
if __name__ == "__main__":
    tournament1 = Tournament(
        "123",
        "Tournament 1",
        "Paris",
        "2021-01-01",
        "2021-01-05",
        nb_rounds=4,  # Include the nb_rounds argument
        description="Tournament 1 description",
    )
    tournament1.save_to_db()
    tournament2 = Tournament(
        "456",
        "Tournament 2",
        "Lyon",
        "2021-02-01",
        "2021-02-05",
        nb_rounds=4,  # Include the nb_rounds argument
        description="Tournament 2 description",
    )
    tournament2.save_to_db()
    print(Tournament.get_all_tournaments())
    print(Tournament.get_tournament_by_id("123"))
    print(Tournament.get_tournament_by_id("456"))
    print(Tournament.get_tournament_by_id("789"))