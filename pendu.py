########################
#     Jeu du pendu     #
#  Débuté ce 29/09/25  #
########################

import random
from string import ascii_uppercase

# Lettres de l'alphabet -> minuscule et majuscule
alphabet = ascii_uppercase

# Mot à trouver
mystery_word = ["PYTHON", "JOCELYN", "EXTRAVAGANT", "GOUVERNEMENT"]
mystery_word = random.choice(mystery_word)

found = False
vies = 10 # nombre de vies

blanks = ["*"] * len(mystery_word)
if __name__ == '__main__':
    print("Cherchez le mot mystère...")
    print(f"Number of blanks: {len(blanks) }")
    print("".join(blanks), "\n")


    while not found:
        choix_user = str(input("> Donnez une lettre: "))
        print(" ".join(blanks))

        if len(choix_user) > 1:
            print("> 1 caractère à la fois!\n")
            vies -= 1
            print('\033[33m' + f"Vies :{vies}" + '\033[0m')

        elif len(choix_user) == 0:
            print("> Il faut écrire quelque chose...")
            vies -= 1
            print('\033[33m' + f"Vies: {vies}" + '\033[0m')

            if vies == 0:
                print(f"Le mot mystere était {mystery_word}")
                exit()

        elif choix_user not in alphabet:
            print("> Veuillez entrer une lettre (majuscule)\n")
            vies -= 1
            print('\033[33m' + f"Vies: {vies}" + '\033[0m')


            if vies == 0:
                print(">Nombre de vies nul, fin de partie...")
                print(f"Le mot mystere était {mystery_word}")
                print('\033[31m' + "GAME OVER :(" '\033[0m')

                exit()

        elif choix_user not in mystery_word:
            print("Réésayez!\n")
            vies -= 1
            print('\033[33m' + f"Vies: {vies}" + '\033[0m')


            if vies == 0:
                print("Nombre de vies nul, fin de partie...")
                print('\033[31m' + f"GAME OVER :(" '\033[0m')

                exit()

        elif choix_user in mystery_word:
            for i, c in enumerate(mystery_word):
                if c == choix_user:
                    blanks[i] = choix_user
                    print("".join(blanks))
                    print("Bien joué!\n")
                
            print("".join(blanks))
        
        if mystery_word == "".join(blanks):
            print(f"Bravo! Le mot était bien {"".join(blanks)}")
            exit()

        