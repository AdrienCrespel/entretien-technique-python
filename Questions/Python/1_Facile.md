# Niveau Facile 🟢

## Qu'est-ce que PEP 8 et pourquoi est-il important ?

**Réponse Attendue :**
PEP 8 est le guide de style pour le code Python. Il fournit des recommandations sur la façon de formater le code Python pour le rendre plus lisible et cohérent. Suivre PEP 8 est important pour maintenir un code propre et compréhensible par tous les membres de l'équipe.

## Quelle est la différence entre une liste et un tuple en Python ?

**Réponse Attendue :**
- **Liste :** Les listes sont mutables, ce qui signifie que vous pouvez modifier leurs éléments après leur création. Elles sont définies en utilisant des crochets [].
- **Tuple :** Les tuples sont immuables, ce qui signifie que leurs éléments ne peuvent pas être modifiés après leur création. Ils sont définis en utilisant des parenthèses ().

## Qu'est-ce qu'une list comprehension et comment l'utilisez-vous ?

**Réponse Attendue :**
Une list comprehension est une syntaxe concise pour créer des listes. Elle permet de générer une nouvelle liste en appliquant une expression à chaque élément d'une séquence.
**Exemple :**

```python
carres = [x**2 for x in range(10)]
```

## Quelle est la différence entre `is` et `==` en Python ?

**Réponse Attendue :**
- `is` vérifie si deux variables pointent vers le même objet en mémoire (opérateur d'identité).
- `==` vérifie si deux objets ont la même valeur (opérateur d'égalité).

## Qu'est-ce qu'un module en Python et comment l'utilisez-vous ?

**Réponse Attendue :**
Un module est un fichier contenant du code Python qui peut être importé et utilisé dans d'autres fichiers Python. Les modules permettent de structurer et d'organiser le code.
**Exemple :**

```python
import math
print(math.sqrt(16))  # Output: 4.0
```