'''
Formation en ligne {Youtube} machine learning

'''
'''
# Episode 2
def e_potentielle(masse, hauteur, e_limite, g = 9.81):
    energie = masse * hauteur * g
    return energie > e_limite

print(e_potentielle(70, 10, 100))

# Utiliser la fonction 'print' parce-que VSCode interprète mal le résultat!

#################################################################################################################

# Episode 3
def fibonacci(n):
    a = 0
    b = 1
    print(a, b, end=" ")
    while b <= n:
        print(b, end=" ")
        a, b = b, a + b


fibonacci(10000)

################################################################################################################
        
# Episode 4
def fibonacci(n):
    a = 0
    b = 1
    liste_1 = [a]
    while b < n:
        liste_1.append(b)
        a, b = b, a + b

    print(liste_1)

fibonacci(10000)

#################################################################################
# Episode 5

classeur = {
    "positif": [],
    "negatif": [],
}

def trier(classeur, nombre):
    if nombre < 0:
        classeur["negatif"].append(nombre)

    elif nombre == 0:
        quit()

    else:
        classeur["positif"].append(nombre)

    print(classeur) 

trier(classeur, -4)


##################################################################################################################
# Episode 6

dico = {k: k**2 for k in range(21)}
print(dico)

####################################################################
# Episode 7
with open("fichier.txt", "w") as f:
    for i in range(10):
        f.write("{}^2 = {} \n".format(i, i**2) )
    
with open("fichier.txt", "r") as f:
    print(list(f.read().splitlines()))
#######################################################################
# Episode 8
import glob

filenames = glob.glob("*txt")
content = {}
for file in filenames:
    with open(file, "r") as f:
        content[file] = f.read().splitlines()

print(content)

######################################################################
# Ep 10
import numpy as np

def initialisation(m, n):
    table = np.random.randn(m, n)
    table_1 = np.ones((m, 1))
    assemblage = np.concatenate((table, table_1), axis = 1)
    print(assemblage)

initialisation(3, 4)



#####################################################################
# EP 11 --> formater l'image de base de matplotlib [radoon laver]
import scipy.datasets
import matplotlib.pyplot as plt

face = scipy.datasets.face(gray = True)
y = int(face.shape[0] / 4)
x = int(face.shape[1] / 4)

y_end = y * 3
x_end = x * 3
print(face.shape)

# Eclaircir / assombrir les couleurs
face[(face > 0) & (face < 100)] = 50
face[(face > 180) & (face < 2 55)] = 210

face = face[y:y_end+1, x:x_end + 1]
plt.imshow(face, cmap=plt.cm.gray)
plt.show()
########################################################################
# EP 12 --> NUMPY ET MATHS
import numpy as np
np.random.seed(0)
A = np.random.randint(0, 100, [10, 5])
D = (A - A.mean(axis = 0)) / A.std(axis = 0)

print(D, f"\nEcart-type de la 1e colonne de la matrice D: {int(D[:, :1].std()) }\nMoyenne d'une colonne = {int(D[:, :1].mean())}")


########################################################################
# EP 13 --> NUMPY ET BRODCASTING
import numpy as np

A = np.random.randint(0, 10, [4, 1])
B = np.random.randint(0, 10, [1, 3])
 
C = A + B
print(A, "\n", B ,"\n", C)


########################################################################
# EP 14 -->MATPLOTLIB
import matplotlib.pyplot as plt
import numpy as np
import math
 
x = np.linspace(-20, 20, 10)
y = 2*x**2 - x - 6

plt.figure(figsize=(12, 8))
plt.plot(x, y, lw = 5, c = "green", label = "polynomial")
plt.plot(x, x**3, c="orange", lw = 5, label = "quadratic")
plt.xlabel("x")
plt.ylabel("y")
plt.title("First graph")
plt.legend()
plt.show()
plt.savefig("figure1.jpg")

plt.figure(figsize=(12, 8))
plt.subplot(2, 1, 1)
plt.plot(x, y, c="red")
plt.subplot(2, 1, 2)
plt.plot(x, y, c="green")

plt.show()
'''
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
dataset = {f"experience {i}": np.random.randn(100) for i in range(1, 5)}
x = dataset["experience 1"]
y = 2*x+2

fig, ax = plt.subplots(4, 1, sharex = False)
ax[0].plot(x, y)
ax[1].plot(x, y)
ax[2].plot(x, y)
ax[3].plot(x, y)

for title in range(4):
    ax[title].set_title(f"Experience {title}")
    ax[title].hspace = 30
plt.show()
