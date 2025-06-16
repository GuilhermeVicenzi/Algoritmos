#Declara a lista de valores
valores = list(range(0,100))
#Declara o valor alvo
alvo = 42
#Define busca_binaria
def busca_binaria(lista, alvo):
    #Parametros lista, alvo
    #Se a lista so tem 1 elemento e ele é o alvo
    if lista[0] == alvo and len(lista) == 1:
        #Retorna lista
        return lista
    #Define inicio
    inicio = 0
    #Define final
    final = len(lista) - 1
    #Calcula o pivo
    pivo = int(final / 2)
    #Se o valor esta na 1 metade da list
    if alvo in lista[inicio:pivo]:
        #Chama busca_binaria passando a primeira metade da lista
        return busca_binaria(lista[inicio:pivo], alvo)
    #Senão
    else:
        #Chama busca_binaria passando a segunda metade da lista
        return busca_binaria(lista[pivo:final], alvo)

valor = busca_binaria(valores, alvo)
print(valor)