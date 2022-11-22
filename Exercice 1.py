x = int(input("Entrez x:"))
y = int(input("Entrez y:"))

print(f"Avant permutation: \n x : {x} \n y : {y}")


t = x
x = y
y = t
print(f"Après permutation: \n x : {x} \n y : {y}")