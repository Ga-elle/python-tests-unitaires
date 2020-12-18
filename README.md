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
 + bonne pratique : organiser ses tests en classes. Pytest détecte les classes qu'il doit exécuter en cherchant celles qui commencent par `Test`. Il faut donc commencer toutes les classes de nos tests avec ce mot.

#### Utiliser des mocks

Utiliser le helper `monkeypatch` dans Pytest ((documentation)[https://docs.pytest.org/en/latest/monkeypatch.html])

#### Imiter l'écriture dans un fichier

Utiliser le helper `tmpdir`dans Pytest : il permet de créer un nouveau fichier dans un répertoire temporaire. A la fin du test, Pytest le supprime pour nous.

```
p = tmpdir.mkdir("program").join("agents.json")
```

Cette fonction va créer un dossier program et un fichier agents.json à l'intérieur.


#### Améliorer la couverture des tests

Pytest nous permet d'exécuter des instructions avant ou après chaque test unitaire à l'aide de `setup` et `teardown`.
 + la méthode `setup_fonction()` est déclenchée avant votre test unitaire
 + la méthode `teardown_function()` est déclenchée à la fin de chaque test unitaire
Il existe plusieurs niveaux:
 + déclenchement avant chaque test unitaire : `setup_function(function)`, `setup_method(self, method)`
 + déclenchement à la création d'une classe : `setup_class(cls)`
 + déclenchement à l'import du module pytest : `setup_module(module)`
