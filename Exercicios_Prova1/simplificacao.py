#pede a quantia de numeros (q)
q = int(input("Digite quantos numeros quer calcular: "))
#pede um numero e armazena (a)
a = int(input("Digite um numero: "))
#pede outro numero e armazena (b)
b = int(input("Digite outro numero: "))
#inicializa a variavel de soma geral (soma)
soma = 0
#calcula a primeira conta (x1 = a + b)
x1 = a + b
#adiciona o valor da conta na soma
soma += x1
#criar um laço de repeticao
for i in range(q-2):
    #pede um numero (c)
    c = int(input("Digite outro numero: "))
    #se indice do laco de repeticao for par (i % 2 == 0)
    if i % 2 == 0:
        #calcula x1 = x1 * c e adiciona em soma
        x1 = x1 * c
        soma += x1
    #se nao
    else:
        #calcula x1 = x1 + c e adiciona em soma
        x1 = x1 + c
        soma += x1

#mostra os calculos da soma
print(f"A soma de todos os cálculos é {soma}")