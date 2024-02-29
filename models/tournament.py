from tinydb import TinyDB, Query
from datetime import datetime
from models.player import Player
from models.round import Round

db_tournaments = TinyDB("data/tournaments.json", indent=4)


class Tournament:
    """Tournament class"""

    tournaments_table = db_tournaments.table("tournaments")


    ## load tournaments from the database
    ##  - charger les tournament dont le status est "In progress"
    ## - afficher cette liste par la view
    ## - recupere l'identifiat du tournous selectionné
    ## - charger le tournoi selectionné - get_tournament_by_id
    ## - reprendre la gestion des rounds a partir de la ou on s'est arreté (grace au current_round)

    def __init__(
        self,
        tournament_id,
        name,
        location,
        start_date,
        end_date,
        current_round=1,
        players=None,
        rounds=None,
        description="",
        status="Done",
        id_db = None,
    ):
        self.tournament_id = tournament_id
        self.name = name
        self.location = location
        self.current_round = current_round
        self.start_date = start_date # or datetime.now().strftime("%Y-%m-%d")
        self.end_date = end_date
        self.status = status
        # self.status = "Done" if self.end_date < datetime.now().strftime("%Y-%m-%d") else "In progress"
        self.description = description
        self.players = players or []
        self.rounds = rounds or []
        self.number_of_players = len(self.players)
        self.number_of_rounds = len(self.rounds)
        self.id_db = id_db


    def serialize(self):
        """Serialize the tournament object to a dictionary"""
        return {
            "tournament_id": self.tournament_id,
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "current_round": self.current_round,
            "status": self.status,
            "description": self.description,
            #"players": [player.serialize() for player in self.players],
            "players": [player["id_db"] for player in self.players],
            "rounds": [round.serialize() for round in self.rounds],
            "id_db": self.id_db,
        }
   

    def save_to_db(self):
        """Save tournament serialized data to the TinyDB database"""
        print(f"Saving tournament {self.tournament_id} - {self.name} to the database")
        tournament_data = self.serialize()
        self.tournaments_table.insert(tournament_data)
        print("Tournament saved successfully")
   


    # def save_to_db(self):
    #     """Save tournament data to database"""
    #     tournament_query = Query()
    #     existing_tournament = self.tournaments_table.get(
    #         tournament_query.tournament_id == self.tournament_id
    #     )
    #     if existing_tournament is not None:
    #         self.tournaments_table.update(
    #             {
    #                 "name": self.name,
    #                 "location": self.location,
    #                 "start_date": self.start_date,
    #                 "end_date": self.end_date,
    #                 "status": self.status,
    #                 "description": self.description,
    #                 "players": [player for player in self.players],
    #                 "rounds": [round.serialize() for round in self.rounds],
    #             },
    #             tournament_query.tournament_id == self.tournament_id,
    #         )
    #     else:
    #         tournament_data = {
    #             "tournament_id": self.tournament_id,
    #             "name": self.name,
    #             "location": self.location,
    #             "start_date": self.start_date,
    #             "end_date": self.end_date,
    #             "status": self.status,
    #             "description": self.description,
    #             "players": [player.player_id for player in self.players],
    #             "rounds": [round.serialize() for round in self.rounds],
    #         }
    #         self.tournaments_table.insert(tournament_data)

    


       




        

                

    @classmethod
    def get_all_tournaments(cls):
        """Retrieve all tournaments from the database"""
        tournaments_data = cls.tournaments_table.all()
        for tournament in tournaments_data:
            tournament["id_db"] = tournament.doc_id

        tournaments = [cls(**data) for data in tournaments_data]
        return tournaments

    # @classmethod
    # def get_tournament_by_id(cls, tournament_id):
    #     """Retrieve a tournament from the database by tournament ID"""
    #     tournament_query = Query()
    #     tournament_data = cls.tournaments_table.get(
    #         tournament_query.tournament_id == tournament_id
    #     )
    #     if tournament_data:
    #         return cls(**tournament_data)
    #     else:
    #         return None
    
    
    @classmethod
    def get_tournament_by_id(cls, id_db):
        """Return a tournament dict matching the id_db (id_db = doc_id), add the id_db in the record"""
        record = cls.tournaments_table.get(doc_id=id_db)
        if record is not None:
            record["id_db"] = record.doc_id
        return record





    # def add_players(self, players):
    #     """Add players to the tournament"""
    #     self.players.extend(players)
        


# test tournament.py using if __name__ == "__main__"
if __name__ == "__main__":
    print("Executing tournament.py")
    # tournament1 = Tournament(
    #     "123",
    #     "Tournament 1",
    #     "Paris",
    #     "2021-01-01",
    #     "2021-01-05",
    #     nb_rounds=4,  # Include the nb_rounds argument
    #     description="Tournament 1 description",
    # )
    # tournament1.save_to_db()
    # tournament2 = Tournament(
    #     "456",
    #     "Tournament 2",
    #     "Lyon",
    #     "2021-02-01",
    #     "2021-02-05",
    #     nb_rounds=4,  # Include the nb_rounds argument
    #     description="Tournament 2 description",
    # )
    # tournament2.save_to_db()
    # print(Tournament.get_all_tournaments())
    # print(Tournament.get_tournament_by_id("123"))
    # print(Tournament.get_tournament_by_id("456"))
    # print(Tournament.get_tournament_by_id("789"))