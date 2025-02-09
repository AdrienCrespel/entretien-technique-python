# Exercice : Écrivez une fonction pour calculer la factorielle d'un nombre.

# Correction :

def factorielle(n):
    if n == 0:
        return 1
    resultat = 1
    for i in range(1, n + 1):
        resultat *= i
    return resultat

print(factorielle(5))  # Output: 120
print(factorielle(10))  # Output: 3628800

# Explication :
#
# La factorielle d'un nombre n est le produit de tous les entiers de 1 à n.
# Si n est égal à 0, la factorielle de 0 est 1.
# Sinon, nous initialisons un résultat à 1 et multiplions chaque entier de 1 à n pour obtenir le résultat final.
