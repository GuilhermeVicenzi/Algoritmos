import random
#Inicializa um vetor para as respostas
respostas = []
#Cria um laco de repeticao
for i in range(100000):
    #Sorteia um numero aleatorio
    n = random.randrange(-1000, 1000)
    #Se uma raiz for sorteada de novo
    if n in respostas:
        #Pula pra proxima iteração
        continue
    #Se o numero substituido torna a equacao 0
    if 2*(n**3) - 3*(n**2) - 3*n + 2 == 0:
        #Adiciona o numero no vetor das respostas
        respostas.append(n)
    if len(respostas) == 3:
        break
    
print(respostas)