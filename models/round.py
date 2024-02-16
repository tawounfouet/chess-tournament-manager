from tinydb import TinyDB, Query
from datetime import datetime

db_tournament = TinyDB("../data/tournaments.json", indent=4)

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
    round1 = Round(1, "Round 1")
    round1.save_to_db()
    round2 = Round(2, "Round 2")
    round2.save_to_db()
    round3 = Round(3, "Round 3")
    round3.save_to_db()
    round4 = Round(4, "Round 4")
    round4.save_to_db()
    round5 = Round(5, "Round 5")
    round5.save_to_db()
    round6 = Round(6, "Round 6")
    round6.save_to_db()
    round7 = Round(7, "Round 7")
    round7.save_to_db()
    round8 = Round(8, "Round 8")
    round8.save_to_db()
    round9 = Round(9, "Round 9")
    round9.save_to_db()
    round10 = Round(10, "Round 10")
    round10.save_to_db()
    round11 = Round(11, "Round 11")
    round11.save_to_db()
    round12 = Round(12, "Round 12")
    round12.save_to_db()
    round13 = Round(13, "Round 13")
    round13.save_to_db()
    round14 = Round(14, "Round 14")
    round14.save_to_db()
    round15 = Round(15, "Round 15")
    round15.save_to_db()
    round16 = Round(16, "Round 16")
    round16.save_to_db()
    round17 = Round(17, "Round 17")
    round17.save_to_db()
    round18 = Round(18, "Round 18")
    round18.save_to_db()
    round19 = Round(19, "Round 19")
    round19.save_to_db()
    round20 = Round(20, "Round 20")
    round20.save_to_db()
    round21 = Round(21, "Round 21")
    round21.save_to_db()
    round22 = Round(22, "Round 22")
    round22.save_to_db()
    round23 = Round(23, "Round 23")
    round23.save_to_db()
    round24 = Round(24, "Round 24")
    round24.save_to_db()
    round25 = Round(25, "Round 25")
    round25.save_to_db()

