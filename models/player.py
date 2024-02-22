
from tinydb import TinyDB, Query
import random

# Initialize TinyDB database with the specified path
db_players = TinyDB("data/players.json", indent=4)


class Player:
    """Player class"""

    players_table = db_players.table("players")

    def __init__(self, first_name, last_name, date_of_birth, player_id, score=0):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.player_id = player_id
        self.score = score


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
            "player_id": self.player_id,
            "score": self.score
        }
  

    @classmethod
    def deserialize(cls, data):
        """Deserialize data dictionary to create a Player object - from JSON format(from_dict) to object"""
        #return cls(data["first_name"],data["last_name"], data["date_of_birth"], data["player_id"])
        return Player(**data)
    
    
    # def save_to_db(self):
    #     """Save player serialized data to the TinyDB database"""
    #     print(f"Saving player {self.player_id} - {self.full_name} to the database")
    #     self.players_table.insert(self.serialize())
    #     print("Player saved successfully")

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
    def get_player_by_id(cls, player_id):
        """Find a player by ID"""
        player = cls.players_table.get(Query().player_id == player_id)
        if player:
            return cls.deserialize(player)
        else:
            return None 
        
    @classmethod
    def get_all_players(cls):
        """Get all players"""
        players_data = cls.players_table.all()
        if players_data:
            return [cls.deserialize(player) for player in players_data]
        else:
            return []
  
if __name__ == "__main__":
    print("Executing player.py")
    # # Test the Player class
    player1 = Player("John", "Doe", "1990-01-01", "JD001")
    player1.save_to_db()

    player2 = Player("Jane", "Smith", "1985-05-15", "JS001")
    player2.save_to_db()

    player3 = Player("Alice", "Brown", "1995-12-25", "AB001")
    player3.save_to_db()

    player4 = Player("Bob", "Johnson", "1980-10-10", "BJ001")
    player4.save_to_db()

    player5 = Player("Charlie", "Davis", "1992-03-20", "CD001")
    player5.save_to_db()

    player6 = Player("David", "Wilson", "1998-08-30", "DW001")
    player6.save_to_db()

    player7 = Player("Eve", "Garcia", "1993-07-05", "EG001")
    player7.save_to_db()

    player8 = Player("Frank", "Martinez", "1987-04-12", "FM001")
    player8.save_to_db()


 
