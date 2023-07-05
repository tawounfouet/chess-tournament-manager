from tinydb import TinyDB, Query, where

db_players = TinyDB("data/players.json", indent=4)
# CMD + K + F


class Player:
    """Player class"""

    players_table = db_players.table("players")

    def __init__(
        self,
        first_name,
        last_name,
        date_of_birth,
        player_id="AB" + input("entrez 05 chiffres: "),
        score=0,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.player_id = player_id
        self.score = score

    def __str__(self):
        """Return player's information"""

        return f"Id :{self.first_name}, Prénom: {self.last_name},  Score: {self.score}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def display_information(self):
        """Display player's information"""
        print(f"Prénom: {self.first_name},  Score: {self.score}")

    def save_to_db(self):
        """Save player data to database"""

        player_query = Query()
        existing_player = self.players_table.get(
            player_query.player_id == self.player_id
        )
        if existing_player is None:
            player_data = {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "date_of_birth": self.date_of_birth,
                "player_id": self.player_id,
                "score": self.score,
            }
            self.players_table.insert(player_data)

    def update_score(self, new_score):
        """Update player's score"""
        self.score = new_score
        self.save_to_db()

        # Update the player's score in the database
        player_query = Query()
        self.players_table.update(
            {"score": new_score}, player_query.player_id == self.player_id
        )

    @classmethod
    def get_player_by_id(cls, player_id):
        """Retrieve a player from the database by player ID"""
        # Code to retrieve player data from the database using player ID
        # Assuming the player data is stored in a players_table database table
        player_query = Query()
        player_data = cls.players_table.get(player_query.player_id == player_id)
        if player_data:
            return cls(**player_data)
        else:
            return None

    @classmethod
    def get_all_players(cls):
        """Retrieve all players from the database"""
        player_data = cls.players_table.all()
        players = [cls(**data) for data in player_data]
        return players
