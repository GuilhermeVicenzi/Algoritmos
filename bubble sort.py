lista = [5, 3, 4, 0, 9, 1, 2]
moveu = False
i = 0

while True:
    
    # verifica se está no ultimo elemento da lista
    if i+1 == len(lista):
        print(lista)
        # reseta a variável i para reiniciar caso tenha movido, caso não tenha movido ele encerra o loop
        i = 0
        if not moveu:
            break
        else:
            moveu = False
            continue
    # verifica se o elemento da esquerda é menor que o da direita
    elif lista[i] > lista[i+1]:
        # caso seja, troca de lugar o elemento da esquerda com o da direita
        menor = lista[i+1]
        lista[i+1] = lista[i]
        lista[i] = menor
        # sinaliza que moveu para poder continuar o loop
        moveu = True

    # incrementa 1 na variável i, que está sendo usada para percorrer todos os elementos da lista
    i += 1
    