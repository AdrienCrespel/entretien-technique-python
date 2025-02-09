# Exercice : Écrivez une fonction pour implémenter l'algorithme de A (A-star) pour trouver le plus court chemin dans un graphe pondéré avec heuristique.*

import heapq

def heuristique(a, b):
    # Exemple d'heuristique : distance de Manhattan
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(graphe, depart, arrivee):
    ouvert = []
    heapq.heappush(ouvert, (0, depart))
    came_from = {}
    cout_actuel = {depart: 0}
    cout_estime = {depart: heuristique(depart, arrivee)}

    while ouvert:
        _, noeud_actuel = heapq.heappop(ouvert)
        if noeud_actuel == arrivee:
            chemin = []
            while noeud_actuel in came_from:
                chemin.append(noeud_actuel)
                noeud_actuel = came_from[noeud_actuel]
            chemin.append(depart)
            chemin.reverse()
            return chemin

        for voisin, cout in graphe[noeud_actuel].items():
            cout_total = cout_actuel[noeud_actuel] + cout
            if voisin not in cout_actuel or cout_total < cout_actuel[voisin]:
                came_from[voisin] = noeud_actuel
                cout_actuel[voisin] = cout_total
                cout_estime[voisin] = cout_total + heuristique(voisin, arrivee)
                heapq.heappush(ouvert, (cout_estime[voisin], voisin))
    return None

graphe = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
print(a_star(graphe, 'A', 'D'))  # Output: ['A', 'B', 'C', 'D']

# Explication :
#
# Dans cet exemple, nous avons un graphe pondéré avec des nœuds A, B, C et D. Les poids des arêtes sont indiqués entre les nœuds.
# Nous utilisons l'algorithme A* pour trouver le plus court chemin du nœud de départ A au nœud d'arrivée D.
# L'algorithme commence par initialiser une liste ouverte pour stocker les nœuds à explorer en fonction de leur coût total estimé.
# Nous utilisons une file de priorité pour extraire le nœud avec le coût total estimé minimum à chaque étape.
# À chaque étape, nous mettons à jour le coût actuel et le coût total estimé des nœuds voisins si un coût plus court est trouvé.
# Nous utilisons une fonction heuristique pour estimer le coût restant du nœud actuel au nœud d'arrivée.
# L'algorithme continue jusqu'à ce que le nœud d'arrivée soit atteint ou que la liste ouverte soit vide.
# Si le nœud d'arrivée est atteint, nous reconstruisons le chemin en remontant les nœuds parents à partir du nœud d'arrivée.
# Dans cet exemple, le plus court chemin de A à D est ['A', 'B', 'C', 'D'].