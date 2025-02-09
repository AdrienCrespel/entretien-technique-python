# Exercice : Écrivez une fonction pour trouver le plus grand élément dans une liste.

# Correction :

def trouver_maximum(liste):
    if not liste:
        return None
    max_element = liste[0]
    for element in liste:
        if element > max_element:
            max_element = element
    return max_element

print(trouver_maximum([1, 3, 5, 2, 4]))  # Output: 5
print(trouver_maximum([9, 3, 6, 1, 2]))  # Output: 9

# Explication :
#
# La fonction trouver_maximum(liste) trouve le plus grand élément dans une liste donnée.
# Si la liste est vide, la fonction renvoie None.
# La fonction initialise max_element à la première valeur de la liste.
# Ensuite, elle parcourt tous les éléments de la liste et compare chaque élément avec max_element.
# Si un élément est plus grand que max_element, max_element est mis à jour avec la nouvelle valeur.
# À la fin, la fonction renvoie max_element qui est le plus grand élément de la liste.
