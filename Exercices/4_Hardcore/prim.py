# Exercice : Écrivez une fonction pour implémenter l'algorithme de Prim pour trouver l'arbre couvrant minimum (Minimum Spanning Tree) d'un graphe non orienté pondéré.

import heapq

def prim(graphe, depart):
    mst = []
    visites = set()
    min_heap = [(0, depart, None)]
    while min_heap:
        poids, u, parent = heapq.heappop(min_heap)
        if u in visites:
            continue
        visites.add(u)
        if parent is not None:
            mst.append((parent, u, poids))
        for voisin, poids in graphe[u].items():
            if voisin not in visites:
                heapq.heappush(min_heap, (poids, voisin, u))
    return mst

graphe = {
    0: {1: 10, 2: 6, 3: 5},
    1: {0: 10, 3: 15},
    2: {0: 6, 3: 4},
    3: {0: 5, 1: 15, 2: 4}
}
print(prim(graphe, 0))  # Output: [(0, 3, 5), (3, 2, 4), (0, 1, 10)]

# Explication :
#
# Dans cet exemple, nous avons un graphe non orienté pondéré avec des nœuds 0, 1, 2 et 3. Les poids des arêtes sont indiqués entre les nœuds.
# Nous utilisons l'algorithme de Prim pour trouver l'arbre couvrant minimum (Minimum Spanning Tree) du graphe.
# L'algorithme commence par initialiser un arbre vide et un ensemble de nœuds visités.
# Ensuite, nous utilisons une file de priorité pour stocker les arêtes à explorer en fonction de leur poids.
# À chaque étape, nous extrayons l'arête avec le poids minimum de la file de priorité et ajoutons le nœud correspondant à l'arbre couvrant minimum.
# Nous continuons ce processus jusqu'à ce que tous les nœuds soient visités.
# L'algorithme s'arrête lorsque tous les nœuds sont connectés dans l'arbre couvrant minimum.
# Dans cet exemple, l'arbre couvrant minimum du graphe est [(0, 3, 5), (3, 2, 4), (0, 1, 10)] avec un poids total de 15.