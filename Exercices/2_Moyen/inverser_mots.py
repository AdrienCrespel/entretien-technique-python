# Exercice : Écrivez une fonction pour inverser les mots dans une chaîne de caractères.

# Correction :

def inverser_mots(chaine):
    return ' '.join(chaine.split()[::-1])

print(inverser_mots("Bonjour le monde"))  # Output: "monde le Bonjour"
print(inverser_mots("Python est un langage de programmation"))  # Output: "programmation de langage un est Python"

# Explication :
#
# La méthode split() divise une chaîne de caractères en une liste de mots.
# L'opérateur de tranche [::-1] renverse la liste des mots.
# Enfin, la méthode join() fusionne les mots inversés en une seule chaîne de caractères. 
