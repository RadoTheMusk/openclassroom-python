nombre1 = input("Donnez moi le premier nombre s'il vous plait: ")
nombre2 = input("Donnez moi le deuxième nombre s'il vous plait: ")

if not nombre1.isnumeric or not nombre2.isnumeric():
    print ("ERREUR")
    raise SystemExit("Fin du programme")
nombre2 = int(nombre2)
nombre1 = int(nombre1)

operation = input("Quelle opération voulez-vous effectuer? ")
if operation != "+" and operation != "-" and operation != "*" and operation != "/":
    raise SystemExit("Outil d'opération non valide")
elif operation == "+":  
    resultat = nombre1 + nombre2
    
elif  operation == "-":
    resultat = nombre1 - nombre2
    
elif operation == "*":
    resultat = nombre1 * nombre2
    
else:
    if  nombre2 == 0:
        print ("Division par zéro impossible, rééssayez!")
        raise SystemExit("Fin du programme")
    else:
        resultat = nombre1 / nombre2
    resultat = round(nombre1 / nombre2, 2)
    
print (f"Le résultat de cette opération est: {resultat}")