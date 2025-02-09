# Exercice : Écrivez une fonction pour trouver le plus court chemin dans un graphe non pondéré en utilisant l'algorithme de BFS (Breadth-First Search).

from collections import deque

def plus_court_chemin(graphe, depart, arrivee):
    queue = deque([depart])
    visites = {depart}
    distances = {depart: 0}
    while queue:
        noeud = queue.popleft()
        if noeud == arrivee:
            return distances[noeud]
        for voisin in graphe[noeud]:
            if voisin not in visites:
                visites.add(voisin)
                queue.append(voisin)
                distances[voisin] = distances[noeud] + 1
    return -1

graphe = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
print(plus_court_chemin(graphe, 'A', 'F'))  # Output: 2

# Explication :
#
# Nous avons une fonction plus_court_chemin(graphe, depart, arrivee) qui prend un graphe non pondéré, un noeud de départ et un noeud d'arrivée en entrée.
# Nous utilisons une file (deque) pour stocker les noeuds à visiter.
# Nous utilisons un ensemble (visites) pour suivre les noeuds déjà visités.
# Nous utilisons un dictionnaire (distances) pour stocker les distances de chaque noeud par rapport au noeud de départ.
# Nous initialisons la file avec le noeud de départ et les structures de données visites et distances.
# Nous parcourons la file tant qu'elle n'est pas vide.
# Nous retirons le premier noeud de la file.
# Si ce noeud est le noeud d'arrivée, nous renvoyons la distance de ce noeud par rapport au noeud de départ.
# Sinon, nous parcourons tous les voisins du noeud actuel.
# Si un voisin n'a pas été visité, nous l'ajoutons à l'ensemble visites, à la file et nous mettons à jour sa distance par rapport au noeud de départ.
# Si nous ne trouvons pas le noeud d'arrivée, nous renvoyons -1.
# Dans cet exemple, nous avons un graphe non pondéré avec des noeuds A, B, C, D, E et F.
# Le noeud de départ est A et le noeud d'arrivée est F.
# Le plus court chemin entre A et F est de longueur 2 (A -> C -> F).
