# Exercice : Écrivez une fonction pour implémenter l'algorithme de Dijkstra pour trouver le plus court chemin dans un graphe pondéré.

import heapq

def dijkstra(graphe, depart):
    distances = {noeud: float('inf') for noeud in graphe}
    distances[depart] = 0
    pq = [(0, depart)]
    while pq:
        dist_actuelle, noeud_actuel = heapq.heappop(pq)
        if dist_actuelle > distances[noeud_actuel]:
            continue
        for voisin, poids in graphe[noeud_actuel].items():
            distance = dist_actuelle + poids
            if distance < distances[voisin]:
                distances[voisin] = distance
                heapq.heappush(pq, (distance, voisin))
    return distances

graphe = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
print(dijkstra(graphe, 'A'))  # Output: {'A': 0, 'B': 1, 'C': 3, 'D': 4}

# Explication : 
#
# Dans cet exemple, nous avons un graphe pondéré avec des nœuds A, B, C et D. Les poids des arêtes sont indiqués entre les nœuds.
# Nous utilisons l'algorithme de Dijkstra pour trouver le plus court chemin du nœud de départ A à tous les autres nœuds.
# L'algorithme commence par initialiser les distances de tous les nœuds à l'infini, sauf le nœud de départ, qui est initialisé à 0.
# Ensuite, nous utilisons une file de priorité pour stocker les nœuds à explorer en fonction de leur distance par rapport au nœud de départ.
# À chaque étape, nous extrayons le nœud avec la distance minimale de la file de priorité et mettons à jour les distances de ses voisins si une distance plus courte est trouvée.
# Enfin, nous retournons les distances minimales de tous les nœuds par rapport au nœud de départ.
# Dans cet exemple, le plus court chemin de A à B est 1, de A à C est 3 et de A à D est 4.
