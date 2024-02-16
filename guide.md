# Logiciel de Gestion d'un tournoi d'échecs

<p align="center">
  <img src="https://user.oc-static.com/upload/2020/09/22/16007793690358_chess%20club-01.png" alt="Logo du logiciel de gestion de tournois d'échecs"/>


Ce logiciel permet de gérer des tournois d'échecs en suivant les règles du jeu d'échecs classique.

## A propos du tournois

1. `Inscription des joueur` : Les joueurs intéressés à participer au tournoi s'inscrivent en fournissant leurs informations personnelles telles que leur nom, prénom et date de naissance. Dans votre cas, les informations des joueurs sont stockées dans des fichiers JSON.

2. `Création du tournoi`: Une fois que les joueurs sont inscrits, le directeur du tournoi crée un nouveau tournoi en spécifiant le nom, le lieu, les dates de début et de fin, ainsi que d'autres détails pertinents.

3. `Composition des rondes`: Un tournoi est composé de plusieurs rondes. Chaque ronde est un ensemble de matchs entre les joueurs. Au début du tournoi, les joueurs sont mélangés aléatoirement pour déterminer les appariements de la première ronde.

4. `Appariements des joueurs`: Les appariements sont généralement déterminés en utilisant un système de jumelage, tel que le système suisse, où les joueurs ayant des scores similaires sont appariés entre eux. Dans votre cas, les joueurs sont associés en fonction de leur nombre total de points dans le tournoi.

5. `Déroulement des matchs`: Chaque match oppose deux joueurs. Les joueurs peuvent jouer une partie d'échecs contre leur adversaire, généralement avec un temps limité par joueur pour effectuer leurs mouvements. Le résultat du match peut être une victoire pour l'un des joueurs, une défaite ou un match nul.

6. `Attribution des points`: Après chaque match, des points sont attribués aux joueurs en fonction du résultat. Par exemple, une victoire peut valoir 1 point, une défaite 0 point et un match nul 0,5 point pour chaque joueur.

7. `Avancement dans le tournoi`: Au fur et à mesure que les rondes progressent, les joueurs accumulent des points en fonction de leurs résultats. Les joueurs avec le plus grand nombre de points sont généralement classés plus haut dans le tournoi. Le nombre de rondes prévu pour le tournoi est déterminé à l'avance.

8. `Génération des paires pour les rondes suivantes`: Après chaque ronde, les appariements pour la ronde suivante sont générés en utilisant le système de jumelage approprié. Les joueurs sont associés en fonction de leur score dans le tournoi.

9. `Rapports et classements `:  À la fin du tournoi, des rapports peuvent être générés pour afficher les résultats finaux, y compris les classements des joueurs, les performances individuelles, etc.


## Simmulation d'un tournoi

Voici une simulation d'un tournoi d'échecs avec 8 joueurs inscrits et 4 rondes :

### Inscription des joueurs :
- `Joueur 1`: Nom de famille - Dupont, Prénom - Jean, Date de naissance - 1990-03-15
- `Joueur 2` : Nom de famille - Martin, Prénom - Marie, Date de naissance - 1985-07-25
- `Joueur 3 `: Nom de famille - Durand, Prénom - Pierre, Date de naissance - 1995-11-10
- `Joueur 4`: Nom de famille - Lefebvre, Prénom - Emma, Date de naissance - 2000-09-05
- `Joueur 5`: Nom de famille - Garcia, Prénom - Lucas, Date de naissance - 1998-02-20
- `Joueur 6`:  `om de famille - Leroy, Prénom - Laura, Date de naissance - 1989-12-01
- `Joueur 7`: Nom de famille - Moreau, Prénom - Thomas, Date de naissance - 1993-06-08
- `Joueur 8`: Nom de famille - Laurent, Prénom - Chloe, Date de naissance - 1996-04-18

### Composition des rondes :

**Ronde 1** : Les joueurs sont mélangés aléatoirement pour les appariements.
- Match 1 : Joueur 1 vs. Joueur 2
- Match 2 : Joueur 3 vs. Joueur 4
- Match 3 : Joueur 5 vs. Joueur 6
- Match 4 : Joueur 7 vs. Joueur 8

**Ronde 2** : Les joueurs sont appariés en fonction de leur score après la ronde 1.
- Match 5 : Joueur 1 vs. Joueur 4
- Match 6 : Joueur 2 vs. Joueur 3
- Match 7 : Joueur 5 vs. Joueur 8
- Match 8 : Joueur 6 vs. Joueur 7

**Ronde 3** : Les joueurs sont appariés en fonction de leur score après la ronde 2.
- Match 9 : Joueur 1 vs. Joueur 3
- Match 10 : Joueur 2 vs. Joueur 4
- Match 11 : Joueur 5 vs. Joueur 7
- Match 12 : Joueur 6 vs. Joueur 8

Ronde 4 : Les joueurs sont appariés en fonction de leur score après la ronde 3.
- Match 13 : Joueur 1 vs. Joueur 8
- Match 14 : Joueur 2 vs. Joueur 5
- Match 15 : Joueur 3 vs. Joueur 6
- Match 16 : Joueur 4 vs. Joueur 7

### Attribution des points :
- `Victoire`: 1 point
- `Défaite`: 0 point
- `Match nul`: 0,5 point pour chaque joueur

### Classement final (après la ronde 4) :
- Joueur 1 - Jean Dupont : 4 points
- Joueur 2 - Marie Martin : 3 points
- Joueur 3 - Pierre Durand : 3 points
- Joueur 4 - Emma Lefebvre : 2,5 points
- Joueur 5 - Lucas Garcia : 2,5 points
- Joueur 6 - Laura Leroy : 2 points
- Joueur 7 - Thomas Moreau : 1,5 points
- Joueur 8 - Chloe Laurent : 1 point


Ceci est une simulation simplifiée d'un tournoi d'échecs avec 8 joueurs et 4 rondes. Les appariements et les résultats peuvent varier en fonction du système de jumelage utilisé et des performances individuelles des joueurs.



## Structure du projet

La structure du projet sera organisée en 03 packages et suivra le modèle de conception modèle-vue-contrôleur (MVC). Voici un aperçu de chaque répertoire :

Le projet est composé de 3 packages :
- `models` : Ce package contient les classes du projet.
- `views` : Ce package contient les vues du projet.
- `controllers` : Ce package contient les contrôleurs du projet.


- Le fichier `main.py` est le point d'entrée de  l'application.
- Le fichier `requirements.txt` contient la liste des dépendances nécessaires au projet.
- Le répertoire `data/` contient les fichiers JSON pour stocker les données des joueurs et des tournois.
- Le répertoire `models/` contient les modèles de données
- Le répertoire `views/` contient les fichiers liés à l'interface utilisateur, 


Voici la structure que j'aimerais donner au logiciel : projet/
```css
projet/
├── main.py
├── requirements.txt
├── data/
│   ├── players.json
│   └── tournaments.json
├── models/
│   ├── player.py
│   ├── match.py
│   ├── round.py
│   └── tournament.py
├── views/
│   ├── main_menu.py
│   ├── report.py
│   ├── player_views.py
│   ├── match_views.py
│   ├── round_views.py
│   └── tournament_views.py

└── controllers/
    ├── player_controller.py
    ├── match_controller.py 
    ├── round_controller.py
    └── tournament_controller.py
```


## Création d'un tournoié
Pour créer un tournoi avec des rounds, affecter les matches, saisir les résultats et afficher les vainqueurs à la fin, vous pouvez suivre ces étapes :

- Initialisez un tournoi avec les détails nécessaires, y compris le nombre de rounds souhaités.
- Pour chaque round, créez un nouvel objet Round, générez les matches et enregistrez-les dans la base de données.
- Saisissez les résultats des matches pour chaque round.
- Répétez les étapes 2 et 3 jusqu'à la fin du dernier round.

À la fin du dernier round, affichez la liste des vainqueurs en fonction des scores accumulés.