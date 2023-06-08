from tinydb import TinyDB, Query

db_players = TinyDB('data/players.json')

class Player:
    """ Player class"""
    def __init__(self, first_name, last_name, date_of_birth, player_id):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.player_id = player_id
        self.score = 0
      

        #self.player_db = TinyDB('data/players.json')


    def __str__(self):
        """ Return player's information"""
        return f"Id :{self.first_name}, Prénom: {self.last_name},  Score: {self.score}"


    def display_information(self):
        """ Display player's information"""

        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Date of Birth: {self.date_of_birth}")
        print(f"Player ID: {self.player_id}")
        print(f"Score: {self.score}")


    def save_to_db(self):
        """ Save player data to database"""
        players_table = db_players.table('players')
        player_query = Query()
        existing_player = players_table.get(player_query.player_id == self.player_id)
        if existing_player is None:
            player_data = {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'date_of_birth': self.date_of_birth,
                'player_id': self.player_id,
                'score': self.score
            }
            players_table.insert(player_data)



    def calculate_score(self, points):
        """ Calculate player's score"""

        self.score += points

        
    def update_score_in_db(self):
        """ Update player's score in database"""
        players_table = db_players.table('players')
        players_table.update({'score': self.score}, Query().player_id == self.player_id)


if __name__ == "__main__":

    player1 = Player("Thomas", "Awounfouet", "07/09/1995", 1) 
    player2 = Player("John", "Doe", "01/01/2000", 2)
    player3 = Player("Jane", "Walker", "01/01/1990", 3)
    player4 = Player("Tom", "Smith", "01/01/1985", 4)

    # Save player to database if not already saved (based on player_id)
    player1.save_to_db()
    player2.save_to_db()
    player3.save_to_db()
    player4.save_to_db()


    player1.display_information()
