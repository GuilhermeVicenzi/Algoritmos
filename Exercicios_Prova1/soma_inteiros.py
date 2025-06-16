#Inicializa as variaveis maior e segundo maior
maior = 0
segundo_maior = 0
#Cria um loop de repeticao
for i in range(10):
    #Pede o numero e armazena
    n = int(input("Digite um numero: "))
    #Se o numero for 0
    if n == 0:
        #Encerra o codigo
        break
    #Se o numero for maior que maior
    if n > maior:
        #Maior recebe o numero e segundo menor recebe o antigo maior numero
        segundo_maior = maior
        maior = n
    #Senão se o numero for maior que segundo maior 
    elif n > segundo_maior:
        #Segundo maior recebe o numero
        segundo_maior = n
#Soma os 2 maiores e mostra
soma = maior + segundo_maior
print(f"A soma dos 2 maiores numeros, {maior} e {segundo_maior} é {soma}")