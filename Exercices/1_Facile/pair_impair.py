# Exercice : Écrivez une fonction pour vérifier si un nombre est pair ou impair.

# Correction :

def est_pair(nombre):
    return nombre % 2 == 0

print(est_pair(4))  # Output: True
print(est_pair(7))  # Output: False

# Explication :
#
# La fonction est_pair(nombre) vérifie si le nombre est pair ou impair en utilisant l'opérateur modulo (%).
# L'opérateur modulo (%) renvoie le reste de la division du nombre par 2.
# Si le reste est égal à 0, le nombre est pair, sinon il est impair.
