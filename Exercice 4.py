BASE = 4

fromage = 800.0
eau = 2
ail = 2
pain = 400

nbConvives = int(input("Entrez le nombre de personne(s) conviées à la fondue :"))

print(f"Pour faire une fondue fribourgeoise pour {nbConvives} personnes, il vous faut :")

nouvelleQuantité = fromage * nbConvives / BASE
print(f"-{nouvelleQuantité} gr de fromage")
nouvelleQuantité = eau * nbConvives / BASE
print(f"-{nouvelleQuantité} dl d'eau")
nouvelleQuantité = ail * nbConvives / BASE
print(f"-{nouvelleQuantité} gousse(s) d'ail")
nouvelleQuantité = pain * nbConvives / BASE
print(f"-{nouvelleQuantité} gr de pain")






