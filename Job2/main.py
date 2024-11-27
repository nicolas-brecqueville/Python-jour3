age = int(input("Rentrez votre âge : "))
assert 3 < age < 150

if age >= 18:
    print("Tu peux voter.")
else:
    print("Tu ne peux pas voter.")
