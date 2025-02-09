# Exercice : Écrivez une fonction pour fusionner deux listes triées en une seule liste triée.

# Correction :

def fusionner_listes(liste1, liste2):
    liste_fusionnee = []
    i, j = 0, 0
    while i < len(liste1) and j < len(liste2):
        if liste1[i] < liste2[j]:
            liste_fusionnee.append(liste1[i])
            i += 1
        else:
            liste_fusionnee.append(liste2[j])
            j += 1
    liste_fusionnee.extend(liste1[i:])
    liste_fusionnee.extend(liste2[j:])
    return liste_fusionnee

print(fusionner_listes([1, 3, 5], [2, 4, 6]))  # Output: [1, 2, 3, 4, 5, 6]
print(fusionner_listes([1, 3, 5], [2, 4]))  # Output: [1, 2, 3, 4, 5]

# Explication :
#
# Nous avons deux listes triées, liste1 et liste2.
# Nous avons deux indices, i et j, qui sont initialisés à 0.
# Nous parcourons les deux listes en comparant les éléments des deux listes.
# Si l'élément de liste1 est inférieur à l'élément de liste2, nous ajoutons l'élément de liste1 à la liste fusionnée et incrémentons i.
# Sinon, nous ajoutons l'élément de liste2 à la liste fusionnée et incrémentons j.
# Nous continuons ce processus jusqu'à ce que nous ayons parcouru toutes les deux listes.
# Enfin, nous ajoutons les éléments restants de liste1 et liste2 à la liste fusionnée.
