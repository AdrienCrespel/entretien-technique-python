# Niveau Difficile 🟠

## Qu'est-ce que le GIL (Global Interpreter Lock) en Python ?

**Réponse Attendue :**
Le GIL est un mécanisme utilisé par l'interpréteur Python pour gérer l'exécution des threads. Il permet à un seul thread d'exécuter du code Python à la fois, ce qui peut limiter les performances des programmes multi-threadés.

## Quelle est la différence entre `__init__` et `__new__` en Python ?

**Réponse Attendue :**
`__init__` est un constructeur qui initialise une instance d'une classe. Il est appelé après la création de l'instance.
`__new__` est un constructeur statique qui crée une nouvelle instance d'une classe. Il est appelé avant `__init__`.

## Qu'est-ce qu'un décorateur de classe et comment l'utilisez-vous ?

**Réponse Attendue :**
Un décorateur de classe est une fonction qui prend une classe en argument et retourne une nouvelle classe avec des fonctionnalités modifiées ou étendues.
Exemple :

```python
def decorateur_classe(cls):
    cls.nouvelle_methode = lambda self: "Nouvelle méthode"
    return cls

@decorateur_classe
class MaClasse:
    pass

obj = MaClasse()
print(obj.nouvelle_methode())  # Output: "Nouvelle méthode"
```

## Qu'est-ce que le duck typing en Python ?

**Réponse Attendue :**
Le duck typing est un concept où l'appartenance à une classe est déterminée par la présence de méthodes et de propriétés, plutôt que par l'héritage d'une classe spécifique. Si un objet "marche comme un canard et parle comme un canard", il peut être traité comme un canard.

## Qu'est-ce que le garbage collection en Python ?

**Réponse Attendue :**
Le garbage collection est un processus automatique de gestion de la mémoire qui libère la mémoire occupée par des objets qui ne sont plus utilisés. Python utilise un garbage collector pour gérer cela.

## Qu'est-ce qu'une exception en Python et comment la gérez-vous ?

**Réponse Attendue :**
Une exception est une erreur qui se produit pendant l'exécution d'un programme. Les exceptions peuvent être gérées à l'aide de blocs `try`, `except`, `else`, et `finally`.
Exemple :

```python
try:
    resultat = 10 / 0
except ZeroDivisionError:
    print("Division par zéro !")
```

## Quelle est la différence entre `deepcopy` et `copy` dans le module `copy` ?

**Réponse Attendue :**
`copy` crée une copie superficielle (shallow copy) d'un objet, ce qui signifie que les objets imbriqués ne sont pas copiés.
`deepcopy` crée une copie profonde (deep copy) d'un objet, ce qui signifie que tous les objets imbriqués sont également copiés.