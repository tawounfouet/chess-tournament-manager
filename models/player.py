
from tinydb import TinyDB, Query
import random 
from datetime import datetime

# Initialize TinyDB database with the specified path
db_players = TinyDB("data/players.json", indent=4)


class Player:
    """Player class"""

    players_table = db_players.table("players")

    def __init__(self, first_name, last_name, date_of_birth, player_id, score=0, id_db = None):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth 
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")
        self.player_id = player_id
        self.score = score
        self.id_db = id_db  


    def __str__(self):
        """String representation of the player"""
        return f"ID: {self.player_id}, Name: {self.full_name}"
   

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


    def serialize(self):
        """Serialize the player object to a dictionary - from object to JSON format(to_dict)"""
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "date_of_birth": self.date_of_birth,
            "date_of_birth": self.date_of_birth.strftime("%Y-%m-%d"),
            "player_id": self.player_id,
            "score": self.score,
            "id_db": self.id_db,      
        }
  

    @classmethod
    def deserialize(cls, data):
        """Deserialize data dictionary to create a Player object - from JSON format(from_dict) to object"""
        #return cls(data["first_name"],data["last_name"], data["date_of_birth"], data["player_id"])
        return Player(**data)
    
    

    def save_to_db(self):
        """Save player serialized data to the TinyDB database"""
        print(f"Saving player {self.player_id} - {self.full_name} to the database")
        player_data = self.serialize()
        self.players_table.insert(player_data)
        # print(f"Player {self.full_name} created successfully with rank {self.rank}.")

    def update(self):
        """Update player data in the database"""
        print(f"Updating player {self.player_id} - {self.full_name} in the database")
        self.players_table.update(self.serialize(), Query().player_id == self.player_id)
        print("Player updated successfully")

    @classmethod
    def get_player_by_nat_id(cls, player_id):
        """Return player object."""
        player = cls.players_table.get(Query().player_id == player_id)
        if player:
            return cls.deserialize(player)
        else:
            return None 
        
    @classmethod
    def get_all_players(cls):
        """Get all players"""
        players_data = cls.players_table.all()
        for player in players_data:
            player["id_db"] = player.doc_id

        if players_data:
            return [cls.deserialize(player) for player in players_data]
        else:
            return []
        
    @classmethod
    def get_player_by_id(self, id_db):
        """Return a player dict matching the id_db (id_db = doc_id), add the id_db in the record"""
        record = self.players_table.get(doc_id=id_db)
        if record is not None:
            record["id_db"] = record.doc_id
        return record
       
if __name__ == "__main__":
    print("Executing player.py")
    # # # Test the Player class
    # player1 = Player("John", "Doe", "1980-01-01", "JD001")
    # player2 = Player("Jane", "Smith", "1990-01-01", "JS001")
    # player3 = Player("Alice", "Johnson", "2000-01-01", "AJ001")
    # player4 = Player("Bob", "Brown", "2010-01-01", "BB001")
    # player5 = Player("Charlie", "Davis", "2020-01-01", "CD001")
    # player6 = Player("Eve", "Wilson", "2030-01-01", "EW001")

    # # # Save players to the database
    # player1.save_to_db()
    # player2.save_to_db()
    # player3.save_to_db()
    # player4.save_to_db()
    # player5.save_to_db()
    # player6.save_to_db()
  

 
