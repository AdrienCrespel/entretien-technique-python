# Exercice : Écrivez une fonction pour implémenter l'algorithme de Kruskal pour trouver l'arbre couvrant minimum (Minimum Spanning Tree) d'un graphe non orienté pondéré.

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            else:
                self.parent[root_u] = root_v
                if self.rank[root_u] == self.rank[root_v]:
                    self.rank[root_v] += 1

def kruskal(graphe):
    edges = [(poids, u, v) for u in graphe for v, poids in graphe[u].items()]
    edges.sort()
    uf = UnionFind(len(graphe))
    mst = []
    for poids, u, v in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, poids))
    return mst

graphe = {
    0: {1: 10, 2: 6, 3: 5},
    1: {0: 10, 3: 15},
    2: {0: 6, 3: 4},
    3: {0: 5, 1: 15, 2: 4}
}
print(kruskal(graphe))  # Output: [(2, 3, 4), (0, 3, 5), (0, 1, 10)]

# Explication :
#
# Dans cet exemple, nous avons un graphe non orienté pondéré avec des nœuds 0, 1, 2 et 3. Les poids des arêtes sont indiqués entre les nœuds.
# Nous utilisons l'algorithme de Kruskal pour trouver l'arbre couvrant minimum (Minimum Spanning Tree) du graphe.
# L'algorithme commence par trier toutes les arêtes du graphe par poids croissant.
# Ensuite, nous initialisons une structure de données Union-Find pour suivre les composantes connexes du graphe.
# Nous parcourons les arêtes triées et ajoutons chaque arête à l'arbre couvrant minimum si elle ne forme pas de cycle.
# Pour vérifier si une arête forme un cycle, nous utilisons la structure Union-Find pour trouver les composantes connexes des nœuds.
# L'algorithme s'arrête lorsque tous les nœuds sont connectés dans l'arbre couvrant minimum.
# Dans cet exemple, l'arbre couvrant minimum du graphe est [(2, 3, 4), (0, 3, 5), (0, 1, 10)] avec un poids total de 15.
