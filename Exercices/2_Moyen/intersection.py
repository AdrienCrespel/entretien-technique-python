# Exercice : Écrivez une fonction pour trouver l'intersection de deux listes.

def intersection(liste1, liste2):
    return list(set(liste1) & set(liste2))

print(intersection([1, 2, 3, 4], [3, 4, 5, 6]))  # Output: [3, 4]
print(intersection([1, 2, 3], [4, 5, 6]))  # Output: []

# Explication :
#
# Nous avons deux listes, liste1 et liste2.
# Nous utilisons l'opérateur & pour trouver l'intersection des deux ensembles créés à partir des listes.
# Enfin, nous convertissons l'ensemble résultant en une liste et le renvoyons.
