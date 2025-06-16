import random
#Cria a variavel do peso da mochila (peso)
peso = 0
#Cria a lista de itens (itens)
itens = ["livro","celular","bola","martelo","toalha","agenda","garrafa de água","caderno","penal"]
#Cria a lista de peso (pesos)
pesos = [2, 0.5, 1, 3, 0.5, 0.5, 1, 0.5, 0.5]
#Cria a lista de itens na mochila (na_mochila)
na_mochila = []
#enquanto o peso da mochila nao for 5
while peso < 5 and itens:
    #aleatoriamente escolhe um item
    item = random.choice(itens)
    index = int(itens.index(item))
    peso_item = pesos[index]
    #se o peso do item cabe na mochila
    if peso + peso_item <= 5:
        #adiciona o peso do item na variavel do peso
        peso += peso_item
        #adiciona o item em na_mochila
        na_mochila.append(item)
    #remove o item da lista de itens e o peso do item da lista de peso
    itens.pop(index)
    pesos.pop(index)
    #mostra a combinação de itens da mochila
print(na_mochila)
print(peso)