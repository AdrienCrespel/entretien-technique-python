# Niveau Moyen 🟡

## Qu'est-ce qu'un générateur en Python et comment l'utilisez-vous ?

**Réponse Attendue :**
Un générateur est une fonction qui retourne un itérateur. Les générateurs utilisent le mot-clé `yield` pour retourner des valeurs une par une, ce qui permet de gérer de grandes quantités de données de manière efficace.
Exemple :

```python
def mon_generateur():
    yield 1
    yield 2
    yield 3

for valeur in mon_generateur():
    print(valeur)
```

## Qu'est-ce que la programmation orientée objet (POO) et quels sont ses principes fondamentaux ?

**Réponse Attendue :**
La POO est un paradigme de programmation basé sur des objets et des classes. Ses principes fondamentaux sont l'encapsulation, l'héritage, le polymorphisme et l'abstraction.

## Quelle est la différence entre une méthode de classe et une méthode statique en Python ?

**Réponse Attendue :**
Une méthode de classe prend `cls` comme premier argument et peut accéder aux attributs de classe. Elle est définie avec le décorateur `@classmethod`.
Une méthode statique ne prend pas de premier argument implicite et ne peut pas accéder aux attributs de classe ou d'instance. Elle est définie avec le décorateur `@staticmethod`.

## Qu'est-ce qu'un décorateur en Python et comment l'utilisez-vous ?

**Réponse Attendue :**
Un décorateur est une fonction qui prend une autre fonction en argument et étend ou modifie son comportement. Les décorateurs sont souvent utilisés pour ajouter des fonctionnalités comme la journalisation, la gestion des autorisations, etc.
Exemple :

```python
def mon_decorateur(fonction):
    def wrapper():
        print("Quelque chose avant la fonction.")
        fonction()
        print("Quelque chose après la fonction.")
    return wrapper

@mon_decorateur
def dire_bonjour():
    print("Bonjour !")

dire_bonjour()
```

## Qu'est-ce qu'un package en Python et comment l'utilisez-vous ?

**Réponse Attendue :**
Un package est un dossier contenant plusieurs modules et un fichier `__init__.py`. Les packages permettent de regrouper des modules liés.
Exemple :

```python
from mon_package import mon_module
mon_module.ma_fonction()
```
