###################################
#     Iterface du Jeu du pendu    #
#       Débuté ce 30/09/25        #
###################################

from turtle import*
from pynput import keyboard
import threading, random, functools

'''
Définition des mots mystères choisis aléatoirement {module random}

'''
mystery_word = ["PYTHON", "JOCELYN", "EXTRAVAGANT", "GOUVERNEMENT"]
mystery_word = random.choice(mystery_word)
mystery_word_separated = list(mystery_word)
print(mystery_word)
print(mystery_word_separated)


listen() # Ecouter et relever les évènements sur le clavier
def afficher_touche(key):
    print(key)
    Text(-240, -50, key, True, "right", ("Arial", 16))   
onkey(lambda: afficher_touche("p"), "p")
onkey(lambda: afficher_touche("y"), "y")


#############################################################################

# Définnions de base de l'interface
window = Turtle()
window.screen.title("Le PENDU")
window.screen.bgcolor("black")

class Text: # classe pour écrire du texte à l'écran
    def __init__(self, x, y, text, move, align, font):
        self.x = x
        self.y = y
        self.text = text
        pencolor("cyan")
        window.color("cyan")

        
        window.penup()
        window.goto((x, y))
        window.pendown()
        window.write(text, move, align, font)

'''

Text(-240, -50, "P", True, "right", ("Arial", 16))   
Text(-200, -50, "Y", True, "right", ("Arial", 16))   
Text(-160, -50, "T", True, "right", ("Arial", 16))   
Text(-120, -50, "H", True, "right", ("Arial", 16))   
Text(-80, -50, "O", True, "right", ("Arial", 16))   
Text(-40, -50, "N", True, "right", ("Arial", 16))   
'''

Text(150, 300, "Bienvenue dans le jeu du pendu \n     Proposez des lettres!", True, "right", ("Consolas", 14))

def reset_position():
    teleport(-30, 250)

width(5) # Taille des tirets

# Fonction pour dessiner les cases qui vont contenir les lettres
def cases():
    '''
    Boucle pour les cases
    '''
    reset_position()
    up()
    left(180)
    forward(250)
    left(90)
    forward(480)
    left(90)
    for i in range(len(mystery_word) + 1):
        steps = 20
        forward(steps)
        up()
        forward(steps)
        down()

cases() # Appel de la fonction au début du jeu


################################################################
def on_press(key):
        if key == keyboard.Key.enter:
            corde()

        elif key == keyboard.Key.space:
            head()

        elif key == keyboard.Key.right:
            neck()

        elif key == keyboard.Key.left:
            first_hand()

        elif key == keyboard.Key.up:
            second_hand()

        elif key == keyboard.Key.down:
            buste()

        elif key == keyboard.Key.delete:
            first_foot()

        elif key == keyboard.Key.esc:
            second_foot()

        elif key == keyboard.Key.caps_lock:
            undo()

def keyboard_event(): 
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

##############################################################
'''
Mise en commun de l'output dans la console et l'interface graphique
avec la bibliothèque thread

'''
thread = threading.Thread(target=keyboard_event)
thread.start()
teleport(-30, 250)


width(5) # Taille de la barre
forward(200) # Longueur

width(10) # Taille du bonhomme
up()
backward(100)



def corde():
    right(90)
    down()
    forward(50) # Corde

def head():
    up()
    right(90)
    down()
    circle(40) # Tête

def neck():
    up()
    left(90)
    forward(80)
    down()
    forward(50) # Cou

def first_hand():
    right(45)
    forward(100)
    left(180) # Main

def second_hand():
    up()
    forward(100)
    right(90)
    down()
    forward(100)
    right(180) # MAIN

def buste():
    up()
    forward(100)
    down()
    left(135)
    forward(150) # BUste

def first_foot():
    left(45)
    forward(100)
    right(180)
    up()
    forward(100)


def second_foot():
    left(90)
    down()
    forward(100)
    

def direction():
    right(45)
    up()
    forward(250)

    right(90)
    forward(50)
    left(90)
    down()
    right(180)

window.hideturtle()

mainloop()