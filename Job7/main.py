alphabetNombre = 97
alphabet = ""

fois = 1
while fois < 10:
    nombre = 0
    for i in range(26):
        alphabet += chr(alphabetNombre)
        alphabetNombre += 1
        if alphabetNombre > 122:
            alphabetNombre = 97
        if nombre % 2 == 0:
            print(alphabet)
        nombre += 1
    fois += 1
    