#Declara a lista de valores
lista = list(range(0, 100))
#Declara o valor alvo
alvo = 42
#Enquanto a lista nao tem 1 elemento apenas
while len(lista) > 1:
    print(lista)
    #Declara o inicio da lista
    inicio = 0
    #Delcara o fim da lista
    final = int(len(lista)) - 1
    #Calcula o pivo
    pivo = int(final / 2)
    #Se o valor esta na 1 metade da lista
    if alvo in lista[inicio:pivo]:
        #lista recebe a 1 metade da lista
        lista = lista[inicio:pivo]
    #Senão
    else:
        #lista recebe a 2 metade da lista
        lista = lista[pivo:final]
#Mostra a lista
print(lista)