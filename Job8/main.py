a = int(input("Rentrez la longueur du premier côté du triangle : "))
b = int(input("Rentrez la longueur du deuxieme côté du triangle : "))
c = int(input("Rentrez la longueur du troisieme côté du triangle : "))

if a < b + c and b < c + a and c < b + a:
    print("Votre triangle est :")
    if a == b == c:
        print("équilatéral")
    elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
        print("rectangle")
        if a == b or b == c or c == a:
            print("rectangle et isocèle")
    elif a == b or b == c or c == a:
        print("isocèle")
    else:
        print("quelquonque")



