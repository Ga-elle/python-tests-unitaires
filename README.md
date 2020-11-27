# Tester votre projet avec python

Tutoriel suivi sur la plateforme OpenClassroom : testez votre projet avec python.
Ce projet est un fork depuis [ce dépôt GitHub](https://github.com/OpenClassrooms-Student-Center/la_poo_avec_python/tree/master).


## Getting started

```
python program/download_agents.py > program/agent-100k.json
python program/world.py program/agent-100k.json
```

Le script world.py affiche 2 graphiques : 
 + l'agréability moyenne en fonction de la densité de la population
 + les revenus en fonction de l'âge
 

## Tester son projet

### Utilisation des doctests

```
python -m doctest -v program/world.py
```
