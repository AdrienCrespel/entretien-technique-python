# Exercice : Écrivez une fonction pour implémenter l'algorithme de tri rapide (quick sort).

def tri_rapide(liste):
    if len(liste) <= 1:
        return liste
    pivot = liste[len(liste) // 2]
    gauche = [x for x in liste if x < pivot]
    milieu = [x for x in liste if x == pivot]
    droite = [x for x in liste if x > pivot]
    return tri_rapide(gauche) + milieu + tri_rapide(droite)

print(tri_rapide([3, 6, 8, 10, 1, 2, 1]))  # Output: [1, 1, 2, 3, 6, 8, 10]

# Explication :
#
# La fonction tri_rapide(liste) trie une liste donnée en utilisant l'algorithme de tri rapide.
# Si la liste est vide ou ne contient qu'un seul élément, la fonction renvoie la liste telle quelle.
# Sinon, elle choisit un élément pivot au milieu de la liste.
# Elle crée trois listes : gauche, milieu et droite.
# La liste gauche contient tous les éléments plus petits que le pivot.
# La liste milieu contient tous les éléments égaux au pivot.
# La liste droite contient tous les éléments plus grands que le pivot.
# Enfin, la fonction récursivement trie les listes gauche et droite, puis les concatène avec la liste milieu pour obtenir la liste triée.
