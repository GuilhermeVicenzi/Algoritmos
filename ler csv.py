listados = []
total = 0


a = open("lista.csv", "r")

if a:
    for i in a:
        partes = i.split(",")
        if partes[0] == "2007" and partes[1] == '"Santa Catarina"':
            listados.append(i)
            total += int(partes[3])
    a.close

for i in listados:
    print(i)
print(total)