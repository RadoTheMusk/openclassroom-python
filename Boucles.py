list_de_nombres = input("Entrez une liste de nombres séparés par une virgule s'il vous plait : ")
nombres = list_de_nombres
liste = nombres.split(", ") 
print ("La liste de nombres est: ", liste)
liste_entiers = []
for nombre in liste:
    nombre_entier = int(nombre)
    liste_entiers.append(nombre_entier)

for nombre_entier in liste_entiers:
    somme_des_nombres = sum(liste_entiers)
print (f"La somme des nombres est : {somme_des_nombres}")

for nombre in liste_entiers:
    moyenne = somme_des_nombres / len(liste_entiers)
print (f"La moyenne des nombres est : {moyenne}")

nombre_au_dessus_moyenne = 0
for nombre in liste_entiers:
    if nombre > moyenne:
        nombre_au_dessus_moyenne += 1
print (f"Il y a {nombre_au_dessus_moyenne} nombre(s) qui est(sont) au-dessus de la moyenne")
    