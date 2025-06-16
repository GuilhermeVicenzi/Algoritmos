#Recebe a primeira fracao
fracao = (input("Digite a primeira fração: "))
#Separa o numerador do denominador
fracao = fracao.split("/")
numerador1 = int(fracao[0])
denominador1 = int(fracao[1])
#Recebe a segunda funcao
fracao = (input("Digite a outra fração: "))
#Separa o numerador do denomindaor
fracao = fracao.split("/")
numerador2 = int(fracao[0])
denominador2 = int(fracao[1])

soma_numerador = 0
soma_denominador = 0

#Se os denominadores forem iguais
if denominador1 == denominador2:
    #Soma os numeradores normal
    soma_numerador = numerador1 + numerador2
    soma_denominador = denominador1
#Se nao
else:
    #Calcula o MMC
    soma_denominador = denominador1 * denominador2
    #Multiplica os numeradores
    numerador1 *= denominador2
    numerador2 *= denominador1
    #Faz a soma
    soma_numerador = numerador1 + numerador2

#Mostra o resultado
print(f"A fração somada é {soma_numerador}/{soma_denominador} = {soma_numerador / soma_denominador}")