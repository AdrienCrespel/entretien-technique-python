# Exercice : Écrivez une fonction pour implémenter l'algorithme de Floyd-Warshall pour trouver les plus courts chemins entre toutes les paires de nœuds dans un graphe pondéré.

def floyd_warshall(graphe):
    n = len(graphe)
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
        for j, poids in graphe[i].items():
            dist[i][j] = poids

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

graphe = [
    {1: 3, 2: 1},
    {0: 3, 2: 4, 3: 2},
    {0: 1, 1: 4, 3: 5},
    {1: 2, 2: 5}
]
print(floyd_warshall(graphe))

# Explication :
#
# Dans cet exemple, nous avons un graphe pondéré avec des nœuds 0, 1, 2 et 3. Les poids des arêtes sont indiqués entre les nœuds.
# Nous utilisons l'algorithme de Floyd-Warshall pour trouver les plus courts chemins entre toutes les paires de nœuds.
# L'algorithme commence par initialiser une matrice de distances avec les poids des arêtes entre les nœuds.
# Ensuite, nous mettons à jour la matrice de distances en comparant les distances directes avec les distances passant par un nœud intermédiaire.
# À chaque étape, nous essayons de trouver un chemin plus court entre chaque paire de nœuds en passant par un nœud intermédiaire.
# La matrice de distances finale contient les plus courts chemins entre toutes les paires de nœuds.
# Dans cet exemple, les plus courts chemins entre les nœuds sont stockés dans une matrice 4x4.
