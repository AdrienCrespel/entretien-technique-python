# Exercice : Écrivez une fonction pour résoudre le problème du sac à dos (knapsack problem) en utilisant la programmation dynamique.
#            Le problème du sac à dos consiste à maximiser la valeur totale des objets que l'on peut mettre dans un sac à dos de capacité donnée.
#            Chaque objet a un poids et une valeur associée, et on ne peut mettre qu'une seule copie de chaque objet dans le sac.
#            La fonction doit prendre trois arguments : capacite (capacité maximale du sac à dos), poids (liste des poids des objets) et valeurs (liste des valeurs des objets).
#            La fonction doit renvoyer la valeur maximale que l'on peut obtenir en remplissant le sac à dos avec les objets donnés.

def sac_a_dos(capacite, poids, valeurs):
    n = len(poids)
    dp = [[0 for x in range(capacite + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for w in range(capacite + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif poids[i-1] <= w:
                dp[i][w] = max(valeurs[i-1] + dp[i-1][w-poids[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][capacite]

poids = [1, 2, 3, 5]
valeurs = [10, 20, 30, 50]
capacite = 8
print(sac_a_dos(capacite, poids, valeurs))  # Output: 80

# Explication :
#
# Le problème du sac à dos est un problème d'optimisation classique en informatique.
# La fonction sac_a_dos(capacite, poids, valeurs) résout ce problème en utilisant la programmation dynamique.
# La fonction prend trois arguments : capacite (capacité maximale du sac à dos), poids (liste des poids des objets) et valeurs (liste des valeurs des objets).
# Nous initialisons une matrice dp de dimensions (n+1) x (capacite+1) où n est le nombre d'objets.
# Nous parcourons la matrice dp en utilisant deux boucles for pour remplir les valeurs de la matrice.
# Si i est égal à 0 ou w est égal à 0, alors la valeur est 0.
# Sinon, si le poids de l'objet i-1 est inférieur ou égal à w, alors nous prenons le maximum entre la valeur de l'objet i-1 ajoutée à la valeur précédente (dp[i-1][w-poids[i-1]]) et la valeur précédente (dp[i-1][w]).
# Sinon, nous prenons la valeur précédente (dp[i-1][w]).
# À la fin, nous retournons la valeur maximale obtenue pour la capacité donnée.
