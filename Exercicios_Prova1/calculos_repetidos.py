#inicializa a soma (soma)
soma = 0
#pede a quantidade de numeros que serao calculados (q)
q = int(input("Digite quantos numeros quer calcular: "))
#cria um laco de repetição
for i in range(q):
    #pede um numero
    a = int(input("Digite um numero: "))
    #calcula o numero x o numero da iteração atual
    calculo = a * (i+1)
    #adiciona o numero em soma
    soma += calculo
#mostra o resultado final
print(soma)