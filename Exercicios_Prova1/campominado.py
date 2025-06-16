#criar variavel que contem a matriz
matriz =[
    [0, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 2, 1],
    [1, 2, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0],
    [0, 0, 1, 2, 1, 0]
]
#pedir ao usuario as coordenadas em x e y (x, y)
x = int(input("Digite o valor da coordenada X: "))
y = int(input("Digite o valor da coordenada em Y: "))
#verifica na matriz qual o valor em (x, y) e armazena em (valor)
valor = matriz[x][y]
#se valor igual 2
if valor == 2:
    #mostra "Existe uma bomba!"
    print("Existe uma bomba!")
#senão se valor igual 1
elif valor == 1:
    #mostra "Bomba ao redor"
    print("Bomba ao redor")
#senão
else: 
    #mostra "Sem bombas por perto"
    print("Sem bombas ao redor")