# Exercice : Écrivez une fonction pour compter les occurrences de chaque caractère dans une chaîne de caractères.

def compter_occurrences(chaine):
    occurrences = {}
    for char in chaine:
        if char in occurrences:
            occurrences[char] += 1
        else:
            occurrences[char] = 1
    return occurrences

print(compter_occurrences("bonjour"))  # Output: {'b': 1, 'o': 2, 'n': 1, 'j': 1, 'u': 1, 'r': 1}
print(compter_occurrences("python"))  # Output: {'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1}

# Explication :
#
# Nous initialisons un dictionnaire occurrences pour stocker les occurrences de chaque caractère.
# Nous parcourons chaque caractère de la chaîne.
# Si le caractère est déjà présent dans le dictionnaire, nous incrémentons son compteur d'occurrences.
# Sinon, nous ajoutons le caractère au dictionnaire avec une occurrence de 1.
