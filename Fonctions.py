"""
Ce script a pour but de calculer le salaire horaire d'une personne à partir de son salaire annuel et ses horaires de travail
par semaine.
"""

import math


def salaire_mensuel_calcul(salaire_annuel):
    salaire_mensuel = salaire_annuel / 12
    return salaire_mensuel
def salaire_hebdomadaire_calcul(salaire_mensuel):  
    salaire_hebdomadaire = salaire_mensuel / 4
    return salaire_hebdomadaire
def salaire_horaire_calcul(salaire_hebdomadaire, heures_travaillees):
    salaire_horaire = salaire_hebdomadaire / heures_travaillees
    return salaire_horaire

salaire_annuel_input = float(input("Entrez votre salaire annuel s'il vous plait: "))
heures_travaillees_semaine = float(input("Entrez votre nombre d'heures travailées par semaine s'il vous plait: "))

salaire_mensuel_resultat = salaire_mensuel_calcul(salaire_annuel_input)
salaire_hebdo_final = salaire_hebdomadaire_calcul(salaire_mensuel_resultat)

salaire_mensuel_resultat = salaire_mensuel_calcul(salaire_annuel_input)
salaire_hebdomadaire_resultat = salaire_hebdomadaire_calcul(salaire_mensuel_resultat)
salaire_horaire_resultat = salaire_horaire_calcul(salaire_hebdo_final, heures_travaillees_semaine)

print (f"Vous avez un salaire horaire de {math.ceil(salaire_horaire_resultat)} euros.")