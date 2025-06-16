#Cria o contador de uso do pendrive
uso = 0
#Cria a lista de tamanho
arquivos = [300, 700, 150, 500, 200, 400, 800, 250, 100, 50, 650, 120, 90, 330, 60]

#Cria a variavel para verificar enquanto tem mudanças
mudancas = True
arquivos_ordenados = []
#Cria um laço de repeticao para ordena
while len(arquivos) != 0:
    #Supoe que o maior da lista é o primeiro
    maior = arquivos[0]
    #Percorre a lista inteira
    for i in arquivos:
        #Verifica se o atual da lista é maior que a variavel maior
        if i > maior:
            #Se for, a variavel maior recebe o valor atual
            maior = i
    #Pega o index do maior
    index = arquivos.index(maior)
    #Adiciona na lista ordenada
    arquivos_ordenados.append(maior)
    #Remove da lista desordenada
    arquivos.pop(index)
        

print(arquivos)
print(arquivos_ordenados)

#Define o espaço disponivel do pendrive
espaco = 0
#Cria um laço de repeticao
#Enquanto tiver arquivos na lista de arquivos:
while arquivos_ordenados:
    #Pegar o maior arquivo e colocar no pendrive
    espaco += arquivos_ordenados[0]
    #Remover o tamanho dele da lista de tamanhos
    arquivos_ordenados.pop(0)
    #Enquanto ainda tiver espaço disponivel:
    for i in arquivos_ordenados[:]:
        #Se mais um arquivo caber no pendrive:
        if espaco + i <= 1000:
            #Adiciona ele do pendrive
            espaco += i
            #Remove ele da lista de tamanhos
            arquivos_ordenados.remove(i)
            #Incrementa no contador
    print(f"Total de espaço usado nessa viagem: {espaco}")
    uso += 1
    espaco = 0
    
#Mostra quantas vezes foi usado o pendrive
print(f"Total de vezes que o pendrive foi usado: {uso}")