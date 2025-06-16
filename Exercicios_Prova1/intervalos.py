#inicializa os contadores de intervalos (i1 = 0, ..., i4 = 0)
i1 = 0
i2 = 0
i3 = 0
i4 = 0
#cria um laco de repeticao de 20 iteracoes
for i in range(20):
    #pede um numero e armazena (n)
    n = int(input("Digite um número: "))
    #se o numero for negativo
    if n < 0:
        #encerra
        break
    #senão
    else:
        #se o numero esta entre 0-25:
        if n <= 25:
            #incrementa em i1
            i1 += 1
        #senão se o numero esta entre 26-50
        if 26 <= n <= 50:
            #incremente em i2
            i2 += 1
        #senão se o numero esta entre 51-75
        elif 51 <= n <= 75:
            #incremente em i3
            i3 += 1
        #senão se o numero esta entre 76-100
        elif 76 <= n <= 100:
            #incremente em i4
            i4 += 1
            
print(i1, i2, i3, i4)