#pedir string ao usario e armezenar em uma variavel (frase)
frase = str(input("Digite uma frase: "))

#incializar contadores de vogais (qa = 0, ... qu = 0)
qa = 0
qe = 0
qi = 0
qo = 0
qu = 0

#percorrer a frase
for i in frase:
    #se o caracter for um vogal
    if i == "A" or i == "a":
        #incrementa no caracter da vogal respectiva
        qa += 1
    elif i == "E" or i == "e":
        qe += 1
    elif i == "I" or i == "i":
        qi += 1
    elif i == "O" or i == "o":
        qo += 1
    elif i == "U" or i == "u":
        qu += 1


if qa != 0:
    print(f"a={qa}, ", end="")

if qe != 0:
    print(f"e={qe}, ", end="")

if qi != 0:
    print(f"i={qi}, ", end="")

if qo != 0:
    print(f"o={qo} ", end="")

if qu != 0:
    print(f"u={qu}", end="")