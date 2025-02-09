# Exercice : Écrivez une fonction pour inverser une chaîne de caractères.

# Correction :

def inverser_chaine(chaine):
    return chaine[::-1]

print(inverser_chaine("Bonjour"))  # Output: "ruojnoB"
print(inverser_chaine("Python"))  # Output: "nohtyP"

# Explication :
#
# Pour inverser une chaîne de caractères, nous pouvons utiliser la notation de tranche (slicing) avec un pas négatif.
# En utilisant [::-1], nous parcourons la chaîne de caractères de la fin au début, ce qui renverse la chaîne.

