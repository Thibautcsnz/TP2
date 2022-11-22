NB = int(input("Entrez un nombre entier"))
if NB==0:
    print("Le nombre est zéro (et il est pair)")
elif NB%2 == 0:
    if NB>0:
        print("Le nombre est positif et pair")
    else:
        print("Le nombre est négatif et pair")
else:
    if NB>0:
        print("Le nombre est positif et impair")
    else:
        print("Le nombre est négatif et impair")