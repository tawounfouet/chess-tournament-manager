from tinydb import TinyDB, Query

# Initialize TinyDB database with the specified path
db_tournaments = TinyDB("data/tournaments.json", indent=4)


class Tournament:
    """Tournament class"""

    tournaments_table = db_tournaments.table("tournaments")

    def __init__(self, name, location, start_date, end_date, players=None, nb_round=4, round_list=None, current_round=1):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.players = [] if players is None else players
        self.nb_round = nb_round
        self.round_list = [] if round_list is None else round_list 
        self.current_round = current_round,
        self.scores = {}
       


    def __str__(self):
        """String representation of the tournament"""
        return f"Name: {self.name}, Location: {self.location}, Start Date: {self.start_date}, End Date: {self.end_date}, Players: {self.players}, Rounds: {self.rounds}, Current Round: {self.current_round}, Rounds List: {self.rounds_list}"

    def serialize(self):
        """Serialize the tournament object to a dictionary"""
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "players": self.players,
            "nb_round": self.nb_round,
            "current_round": self.current_round,
            "round_list": self.round_list
        }


    @classmethod
    def deserialize(cls, data):
        """Deserialize data dictionary to create a Tournament object"""
        return cls(**data)
    

    def save_to_db(self):
        """Save tournament data to database"""
        tournament_data = self.serialize()
        tournament_id = self.tournaments_table.insert(tournament_data)
        print(f"\nTournament saved successfully in DB with ID: {tournament_id}")
    
    @classmethod
    def find_by_id(cls, tournament_id):
        """Find a tournament by ID"""
        tournament_query = Query()
        tournament = cls.tournaments_table.get(doc_id=int(tournament_id))  # Convert ID to int if needed
        if tournament:
            return Tournament.deserialize(tournament)
        else:
            return None
    
    @classmethod
    def get_all_sorted_by_date():
        """Get all tournaments sorted by date"""
        tournaments = db_tournaments.table("tournaments").all()
        if tournaments:
            return [Tournament.deserialize(tournament) for tournament in tournaments]
        else:
            return []
        
    def add_player(self, player):
        """Add a player to the tournament"""
        self.players.append(player)
        print(f"Player {player.full_name} added to the tournament {self.name}.")






if __name__ == "__main__":
    print("Executing tournament.py")    
          # Test Tournament class
    tournament1 = Tournament("Tournament 1", "Paris", "2021-01-01", "2021-01-10")
    tournament1.save_to_db()

