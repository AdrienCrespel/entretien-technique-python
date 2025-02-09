# Exercice : Écrivez une fonction pour vérifier si une chaîne de caractères est un palindrome.

# Correction :

def est_palindrome(chaine):
    chaine = chaine.lower().replace(" ", "")
    return chaine == chaine[::-1]

print(est_palindrome("Radar"))  # Output: True
print(est_palindrome("Bonjour"))  # Output: False
print(est_palindrome("Un roc cornu"))  # Output: True

# Explication :
#
# La fonction est_palindrome(chaine) vérifie si une chaîne de caractères est un palindrome.
# Un palindrome est une chaîne qui se lit de la même manière de gauche à droite et de droite à gauche.
# La fonction convertit la chaîne en minuscules et supprime les espaces.
# Ensuite, elle compare la chaîne avec sa version inversée (chaine[::-1]).
# Si les deux chaînes sont identiques, la fonction renvoie True, sinon elle renvoie False.