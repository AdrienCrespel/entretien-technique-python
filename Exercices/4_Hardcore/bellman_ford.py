# Exercice : Écrivez une fonction pour implémenter l'algorithme de Bellman-Ford pour trouver le plus court chemin dans un graphe pondéré avec des poids négatifs.

def bellman_ford(graphe, depart):
    distances = {noeud: float('inf') for noeud in graphe}
    distances[depart] = 0
    for _ in range(len(graphe) - 1):
        for noeud in graphe:
            for voisin, poids in graphe[noeud].items():
                if distances[noeud] + poids < distances[voisin]:
                    distances[voisin] = distances[noeud] + poids
    for noeud in graphe:
        for voisin, poids in graphe[noeud].items():
            if distances[noeud] + poids < distances[voisin]:
                raise ValueError("Le graphe contient un cycle de poids négatif")
    return distances

graphe = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': -3, 'D': 2},
    'C': {'D': 2},
    'D': {}
}
print(bellman_ford(graphe, 'A'))  # Output: {'A': 0, 'B': 1, 'C': -2, 'D': 0}

# Explication :
#
# Dans cet exemple, nous avons un graphe pondéré avec des nœuds A, B, C et D. Les poids des arêtes sont indiqués entre les nœuds.
# Nous utilisons l'algorithme de Bellman-Ford pour trouver le plus court chemin du nœud de départ A à tous les autres nœuds.
# L'algorithme commence par initialiser les distances de tous les nœuds à l'infini, sauf le nœud de départ, qui est initialisé à 0.
# Ensuite, nous itérons sur tous les nœuds et leurs voisins pour mettre à jour les distances si un chemin plus court est trouvé.
# Nous répétons cette étape (nombre de nœuds - 1) fois pour garantir la convergence de l'algorithme.
# Enfin, nous vérifions s'il y a un cycle de poids négatif en vérifiant si une mise à jour supplémentaire est possible.
# Si un cycle de poids négatif est trouvé, nous levons une exception car l'algorithme ne peut pas converger.
# Dans cet exemple, le plus court chemin de A à B est 1, de A à C est -2 et de A à D est 0.