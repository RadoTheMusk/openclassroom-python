fruits = {
    "pomme" : "rouge",
    "banane" : "jaune",
    "orange" : "orange"
}
fruits["kiwi"] = "vert"
fruits.pop("banane")
fruits['pomme'] = "vert"
couleur_banane = fruits.get("banane") 

print (fruits)  # ou print (fruits.keys())