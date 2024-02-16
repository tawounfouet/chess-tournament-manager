from tinydb import TinyDB, Query, where

db_players = TinyDB("../data/players.json", indent=4)
# CMD + K + F


class Player:
    """Player class"""

    players_table = db_players.table("players")

    def __init__(
        self,
        first_name,
        last_name,
        date_of_birth,
        player_id,
        score=0,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.player_id = player_id
        self.score = score


    def __str__(self):
        """Return player's information"""

        return f"Prénome:{self.first_name},  Nom:{self.last_name},  Score:{self.score}"

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


if __name__ == "__main__":
    # player1 = Player("John", "Doe", "1990-01-01", "123")
    # player1.save_to_db()

    # get all players
    print(Player.get_all_players())



























# player1 = Player("John", "Doe", "1990-01-01", "123")  
# test player.py using if __name__ == "__main__"

# if __name__ == "__main__":
#     player1 = Player("John", "Doe", "1990-01-01", "123")
#     player1.save_to_db()
#     player2 = Player("Jane", "Doe", "1992-01-01", "124")
#     player2.save_to_db()
#     player3 = Player("Alice", "Doe", "1995-01-01", "125")
#     player3.save_to_db()
#     player4 = Player("Bob", "Doe", "1998-01-01", "126")
#     player4.save_to_db()

#     print(player1)
#     print(player2)
#     print(player3)
#     print(player4)

    # print(Player.get_player_by_id("123"))
    # print(Player.get_player_by_id("124"))
    # print(Player.get_player_by_id("125"))
    # print(Player.get_player_by_id("126"))

    # print(Player.get_all_players())
    # player1.update_score(100)
    # print(player1)
    # print(Player.get_player_by_id("123"))
    # print(Player.get_all_players())
    # player2.update_score(200)
    # print(player2)
    # print(Player.get_player_by_id("124"))
    # print(Player.get_all_players())
    # player3.update_score(300)
    # print(player3)
    # print(Player.get_player_by_id("125"))
    # print(Player.get_all_players())
    # player4.update_score(400)
    # print(player4)
    # print(Player.get_player_by_id("126"))
    # print(Player.get_all_players())
    # print(player1.full_name)
    # print(player2.full_name)
    # print(player3.full_name)
    # print(player4.full_name)
    # print(player1.display_information())
    # print(player2.display_information())
    # print(player3.display_information())
    # print(player4.display_information())
    # print(player1.save_to_db())
    # print(player2.save_to_db())
    # print(player3.save_to_db())
    # print(player4.save_to_db())
    # print(player1.update_score(100))
    # print(player2.update_score(200))
    # print(player3.update_score(300))
    # print(player4.update_score(400))
    # print(player1.get_player_by_id("123"))
    # print(player2.get_player_by_id("124"))
    # print(player3.get_player_by_id("125"))
    # print(player4.get_player_by_id("126"))
    # print(player1.get_all_players())
    # print(player2.get_all_players())
    # print(player3.get_all_players())