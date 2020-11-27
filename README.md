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

### Librairies de tests 

 + Unittest
 + Pytest

Dans ce projet, nous utilisons _Pytest_ .

Pour lancer pytest : 
```
pytest
```
Ceci va lancer tous les tests de tous les fichiers qui commencent par `test_` ou qui finissent par `_test`.

Pour voir les `print()` lors du lancement des tests, il faut utiliser l'option `-s` comme suit : `pytest -s`

A retenir :
 + pour tester des valeurs : `assert`
 + pour tester des exceptions : `raises(SomeException)`. Attention, ne pas oublier d'importer le module pytest dans le fichier test.py