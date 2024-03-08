
# Logiciel de gestion tournois d'échecs


## Initialisation du projet :

- Créer un nouveau projet Python.
```bash
mkdir _chess_game
cd _chess_game
```
- Ajouter un fichier requirements.txt pour répertorier les dépendances.
```bash
touch requirements.txt
```

- Configurer un environnement virtuel pour gérer les dépendances du projet.
```bash
python3 -m venv .venv
source .venv/bin/activate

# installer les dépendances du projet
pip install tinydb colorama flake8 black

# enregistrer les dépendances dans le fichier requirements.txt
pip freeze > requirements.txt
```


## Structure du projet :

Par “structurer” nous entendons les décisions que vous faites concernant comment votre projet atteint au mieux son objectif. Nous avons besoin de considérer comment exploiter au mieux les fonctionnalités de Python pour créer un code propre et efficace. En termes pratiques, “structurer” signifie produire du code propre dont la logique et les dépendances sont claires ainsi que la façon dont les fichiers et dossiers sont organisés dans le système de fichiers.

```
_chess_game/
│
├── data/
│   ├── players.json
│   └── tournaments.json
│
├── src/
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── app.py
│   │   ├── player_controller.py
│   │   └── tournament_controller.py
│   │
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── player.py
│   │   ├── tournament.py
│   │   ├── round.py
│   │   └── match.py
│   │
│   └── views/
│       ├── __init__.py
│       ├── player_view.py
│       ├── tournament_view.py
│       └── main_view.py
│
├── tests/
│   ├── test_player_controller.py
│   ├── test_tournament_controller.py
│   ├── test_player.py
│   ├── test_tournament.py
│   ├── test_round.py
│   └── test_match.py
│
├── config.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## fichier config.py
```python
# config.py
import os
from colorama import Fore, Style

# base de données
DB_PATH = os.path.join(os.path.dirname(__file__), "data")



# Configuration des couleurs pour l'affichage dans la console
COLORS = {
    "RED": Fore.RED,
    "GREEN": Fore.GREEN,
    "YELLOW": Fore.YELLOW,
    "BLUE": Fore.BLUE,
    "MAGENTA": Fore.MAGENTA,
    "CYAN": Fore.CYAN,
    "WHITE": Fore.WHITE,
    "BRIGHT_RED": Fore.LIGHTRED_EX,
    "BRIGHT_GREEN": Fore.LIGHTGREEN_EX,
    "BRIGHT_YELLOW": Fore.LIGHTYELLOW_EX,
    "BRIGHT_BLUE": Fore.LIGHTBLUE_EX,
    "BRIGHT_MAGENTA": Fore.LIGHTMAGENTA_EX,
    "BRIGHT_CYAN": Fore.LIGHTCYAN_EX,
    "BRIGHT_WHITE": Fore.LIGHTWHITE_EX,
    "RESET": Style.RESET_ALL,
}

# Configuration des options pour l'affichage dans la console
OPTIONS = {
    "BOLD": Style.BRIGHT,
    "UNDERLINE": Style.UNDERLINE,
    "BLINK": Style.BLINK,
    "RESET": Style.RESET_ALL,
}
```



##  Conception de la structure du programme :
- Diviser le programme en packages selon le modèle MVC (Modèle-Vue-Contrôleur).
- Créer les packages modèles, vues et contrôleurs.
- Définir les classes pour les modèles de joueurs, tournois, tours et matchs dans le package modèles.

Pour un projet de gestion de tournoi d'échecs, il est essentiel de bien organiser les différentes parties du code pour assurer la lisibilité, la maintenabilité et la scalabilité du programme. Voici une proposition de conception de la structure du programme basée sur les spécifications fournies et la structure du projet que vous avez déjà proposée :

### Modèles (models)
Joueur (Player) :
Attributs : nom de famille, prénom, date de naissance, identifiant national d’échecs.
Méthodes : initialisation, représentation sous forme de chaîne.
```python
from tinydb import TinyDB, Query
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
        return Player(**data)
    
    

    def save_to_db(self):
        """Save player serialized data to the TinyDB database"""
        #print(f"Saving player {self.player_id} - {self.full_name} to the database")
        player_data = self.serialize()
        if self.player_id:  
            self.players_table.update(player_data, Query().player_id == self.player_id)
            print(f"Player {self.full_name} data updated successfully.")
        else:
            self.players_table.insert(player_data)
            # print("Player saved successfully")
            

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
    
```




##  Gestion des joueurs :

Implémenter la fonctionnalité d'ajout de joueurs avec les données requises (nom de famille, prénom, date de naissance) dans le package contrôleurs.
Stocker les joueurs dans des fichiers JSON dans le dossier data/players.
Gestion des tournois :

Mettre en place la création de tournois avec les informations requises (nom, lieu, dates, etc.) dans le package contrôleurs.
Stocker les tournois dans des fichiers JSON dans le dossier data/tournaments.
Déroulement des tournois :

Développer la logique pour générer les paires de matchs pour chaque tournoi en fonction des résultats précédents.
Gérer les scores des joueurs et mettre à jour les résultats après chaque tour.
Génération de rapports :

Créer des fonctions pour générer les différents rapports demandés (liste des joueurs, liste des tournois, etc.) dans le package vues.
Sauvegarde et chargement des données :

Implémenter la fonctionnalité de sauvegarde et de chargement de l'état du programme entre les actions de l'utilisateur.
S'assurer que les fichiers JSON sont synchronisés avec les objets en mémoire.
Interface utilisateur via la console :

Créer un menu principal dans le package vues pour permettre à l'utilisateur d'effectuer différentes actions (ajouter un joueur, créer un tournoi, etc.).
Utiliser des boucles et des structures de contrôle pour gérer les interactions avec l'utilisateur.
Validation et tests :

Élaborer des jeux de tests pour chaque fonctionnalité du logiciel.
Effectuer des tests d'intégration pour vérifier le bon fonctionnement global du système.
Nettoyage du code et génération de rapports :

Utiliser flake8 pour vérifier et nettoyer le code conformément aux directives PEP 8.
Générer un rapport flake8-html pour afficher les résultats de l'analyse de linting.
Documentation :

Rédiger un fichier README.md décrivant comment exécuter le programme, ses fonctionnalités et comment générer un nouveau rapport flake8.
Finalisation et déploiement :

Effectuer des tests finaux pour s'assurer que toutes les fonctionnalités fonctionnent correctement.
Préparer les livrables pour le club d'échecs, y compris le lien vers le repository GitHub contenant le code et les rapports.
