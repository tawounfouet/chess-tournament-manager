# Logiciel de Gestions de tournois d'échecs


<p align="center">
  <img src="https://user.oc-static.com/upload/2020/09/22/16007793690358_chess%20club-01.png" alt="Logo du logiciel de gestion de tournois d'échecs"/>

<!-- ![Logo](https://user.oc-static.com/upload/2020/09/22/16007793690358_chess%20club-01.png) -->

Ce logiciel permet de gérer des tournois d'échecs en suivant les règles du jeu d'échecs classique.

## A propos du tournois

`Nombre de participants`: Le tournoi pourra être ouvert à un nombre précis de participants, comme 8, 10, 12 ou plus, afin de déterminer le nombre de rondes nécessaires.

`Durée des parties`: Chaque partie peut être chronométrée avec une durée spécifique allouée à chaque joueur. Par exemple, chaque joueur pourrait avoir 60 minutes pour l'ensemble de la partie.

`Système de notation`: Les points seront attribués en fonction des résultats des parties. Par exemple, une victoire peut valoir 1 point, une partie nulle peut valoir 0,5 point pour chaque joueur et une défaite peut ne pas rapporter de point (c-a-d O point).

`Appariements`: Chaque joueur rencontre tous les autres participants une fois. Il faudra se   s'assurer que chaque joueur rencontre un adversaire différent à chaque ronde.

## Installation

Pour installer le logiciel, il faut d'abord cloner le projet sur votre ordinateur.

```bash
git clone
```

Ensuite, il faut créer un environnement et activer virtuel dans le dossier du projet.

```bash
python -m venv env
source env/bin/activate
```

Enfin, il faut installer les dépendances du projet.

```bash
pip install -r requirements.txt
```


## Utilisation

Pour lancer le logiciel, il faut lancer le fichier main.py.

```bash
python main.py
```

## Tests

Pour lancer les tests, il faut lancer le fichier test.py.

```bash
python test.py
```

