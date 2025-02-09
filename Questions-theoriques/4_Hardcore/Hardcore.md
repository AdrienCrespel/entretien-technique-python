# Niveau Hardcore 🔴

## Qu'est-ce que le modèle de concurrence en Python et quelles sont les différences entre les threads, les processus et les coroutines ?

**Réponse Attendue :**
Le modèle de concurrence en Python permet d'exécuter plusieurs tâches simultanément. Les threads sont des unités d'exécution légères au sein d'un même processus, mais ils sont limités par le GIL. Les processus sont des unités d'exécution indépendantes avec leur propre espace mémoire, gérés par le module `multiprocessing`. Les coroutines sont des fonctions asynchrones qui permettent de suspendre et de reprendre leur exécution, gérées par le mot-clé `async` et `await`.

## Comment fonctionne le mécanisme d'importation en Python et quelles sont les différences entre les imports absolus et relatifs ?

**Réponse Attendue :**
Le mécanisme d'importation en Python permet de charger des modules et des packages. Les imports absolus spécifient le chemin complet du module à partir de la racine du projet, tandis que les imports relatifs spécifient le chemin du module par rapport au module courant. Les imports relatifs utilisent des points (.) pour indiquer le répertoire courant ou parent.

**Exemple :**

```python
# Import absolu
import mon_package.mon_module

# Import relatif
from . import mon_module
```

## Qu'est-ce que le monkey patching en Python et quels sont ses avantages et inconvénients ?

**Réponse Attendue :**
Le monkey patching est la pratique de modifier ou d'étendre le comportement du code à l'exécution, souvent en remplaçant des méthodes ou des attributs existants. Cela peut être utile pour corriger des bugs ou ajouter des fonctionnalités sans modifier le code source original. Cependant, cela peut rendre le code difficile à comprendre et à maintenir, et peut introduire des comportements inattendus.

## Qu'est-ce que le métaclassing en Python et comment l'utilisez-vous ?

**Réponse Attendue :**
Le métaclassing permet de définir des classes de classes, c'est-à-dire des classes dont les instances sont elles-mêmes des classes. Les métaclasses permettent de contrôler la création et le comportement des classes. Elles sont définies en utilisant le mot-clé `metaclass`.

**Exemple :**

```python
class MaMetaClasse(type):
    def __new__(cls, name, bases, dct):
        print(f"Création de la classe {name}")
        return super().__new__(cls, name, bases, dct)

class MaClasse(metaclass=MaMetaClasse):
    pass
```

## Qu'est-ce que le type hinting en Python et comment l'utilisez-vous pour améliorer la lisibilité et la maintenabilité du code ?

**Réponse Attendue :**
Le type hinting permet de spécifier les types attendus pour les arguments et les valeurs de retour des fonctions, ainsi que les types des variables. Cela améliore la lisibilité et la maintenabilité du code en rendant les intentions du développeur plus claires. Les types sont spécifiés à l'aide de la syntaxe `: type` pour les arguments et `-> type` pour les valeurs de retour.

**Exemple :**

```python
def addition(a: int, b: int) -> int:
    return a + b
```

## Comment fonctionne le mécanisme de sérialisation et de désérialisation en Python et quels sont les modules couramment utilisés ?

**Réponse Attendue :**
La sérialisation est le processus de conversion d'un objet en un format pouvant être stocké ou transmis, tandis que la désérialisation est le processus inverse. Les modules couramment utilisés pour la sérialisation en Python incluent `pickle` pour les objets Python et `json` pour les données JSON.

**Exemple :**

```python
import pickle

# Sérialisation
with open('data.pkl', 'wb') as f:
    pickle.dump(objet, f)

# Désérialisation
with open('data.pkl', 'rb') as f:
    objet = pickle.load(f)
```

## Qu'est-ce que le contexte de gestion en Python et comment l'utilisez-vous pour gérer les ressources ?

**Réponse Attendue :**
Le contexte de gestion permet de gérer les ressources de manière sécurisée et prévisible à l'aide de la syntaxe `with`. Les objets de contexte de gestion implémentent les méthodes `__enter__` et `__exit__`.

**Exemple :**

```python
class MonContexte:
    def __enter__(self):
        print("Entrée dans le contexte")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Sortie du contexte")

with MonContexte():
    print("À l'intérieur du contexte")
```