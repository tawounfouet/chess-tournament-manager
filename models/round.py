from tinydb import TinyDB, Query
from datetime import datetime

db_tournament = TinyDB("data/tournaments.json", indent=4)

class Round:
    """Round class"""

    round_table = db_tournament.table("rounds")


    def __init__(self,round_number, name, start_time=None, end_time=None, matches=None):
        self.round_number = round_number
        self.name = name
        self.matches = matches or []
        self.start_time = start_time or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.end_time = end_time
        #self.db = TinyDB('data/rounds_db.json')  # Initialise la base de données TinyDB
        #self.round_table = self.db.table('rounds')  # Crée une table pour stocker les rounds


    def save_to_db(self):
        """Save round data to database"""
        round_query = Query()
        existing_round = self.round_table.get(round_query.round_number == self.round_number)
        round_data = {
            "round_number": self.round_number,
            "name": self.name,
            "matches": self.matches,
            "start_time": self.start_time,
            "end_time": self.end_time
        }

        if existing_round is None:
            self.round_table.insert(round_data)
            print("\nRound saved successfully in DB.")
        else:
            print("\nRound already exists in DB.")

    def mark_as_finished(self):
        """Mark the round as finished and update end time"""
        self.end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.save_to_db()

        
    @classmethod
    def get_all_rounds(cls):
        """Retrieve all rounds from the database"""
        round_data = cls.round_table.all()
        rounds = [cls(**data) for data in round_data]
        return rounds


# test round.py using if __name__ == "__main__"
    
if __name__ == "__main__":
    ## Test Round class
    round1 = Round(1, "Round 1")
    round1.save_to_db()
    round2 = Round(2, "Round 2")
    round2.save_to_db()
    round3 = Round(3, "Round 3")
    round3.save_to_db()
    round4 = Round(4, "Round 4")
    

