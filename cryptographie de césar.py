'''
Ce script a pour but de décoder un message écris avec le code de Jules César (code césar)

'''


import string


# L'alphabet normal transformé en liste pour accession plus facile
alphabet_upper = list(string.ascii_uppercase) # majuscule
alphabet_lower = list(string.ascii_lowercase) # minuscule


# Transformation de l'alphabet vers celui utilisé pour le code de césar
alphabet_code_césar_upper = alphabet_upper
for letter in range(3):
    letter = alphabet_code_césar_upper.pop(0)
    letter_insert = alphabet_code_césar_upper.insert(len(alphabet_code_césar_upper), letter)

alphabet_code_césar_lower = alphabet_lower
for letter2 in range(3):
    letter2 = alphabet_code_césar_lower.pop(0)
    letter_insert = alphabet_code_césar_lower.insert(len(alphabet_code_césar_lower), letter2)


# Redéfinition des variables stockant les alphabets majuscule et minuscule qui ont été modifiées précédemment 
alphabet_upper = list(string.ascii_uppercase)
alphabet_lower= list(string.ascii_lowercase)
correspodance_upper = dict(zip(alphabet_code_césar_upper, alphabet_upper)) 
correspodance_lower = dict(zip(alphabet_code_césar_lower, alphabet_lower))


# Demande du message à coder à l'utilisateur
message_utilisateur = input("Entrez votre message je vais le déchiffrer: ")

list_msg_utilisateur = list (message_utilisateur) # Facilitation d'accès


# Formater le message codé sous forme de message compéhensible
for lettre in list_msg_utilisateur:
    try:
        if lettre in correspodance_lower:
            print (correspodance_lower[lettre], end = "")
        else:
            print (correspodance_upper[lettre], end = "")
    except KeyError:
        print(" ", end = "") # Mise en exception de l'espace qui n'est pas compris dans le dictionnaire, évitant le crash du programme