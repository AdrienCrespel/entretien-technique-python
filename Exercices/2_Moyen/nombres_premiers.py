# Exercice : Écrivez une fonction pour trouver tous les nombres premiers jusqu'à un nombre donné.

# Correction :

def nombres_premiers(n):
    premiers = []
    for num in range(2, n + 1):
        est_premier = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                est_premier = False
                break
        if est_premier:
            premiers.append(num)
    return premiers

print(nombres_premiers(20))  # Output: [2, 3, 5, 7, 11, 13, 17, 19]

# Explication :
#
# Nous avons une fonction nombres_premiers qui prend un nombre n en entrée.
# Nous initialisons une liste vide premiers pour stocker les nombres premiers.
# Nous parcourons tous les nombres de 2 à n.
# Pour chaque nombre, nous vérifions s'il est premier ou non.
# Pour vérifier si un nombre est premier, nous parcourons tous les nombres de 2 à la racine carrée de ce nombre.
# Si le nombre est divisible par un autre nombre, il n'est pas premier.
# Si le nombre est premier, nous l'ajoutons à la liste premiers.
