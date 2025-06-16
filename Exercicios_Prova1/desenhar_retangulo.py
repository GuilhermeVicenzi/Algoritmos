#Pede o valor da base do retangulo e armazena
base = int(input("Digite o tamanho da base do retangulo: "))
#Pede o valor da largura do retangulo e armazena
largura = int(input("Digite o tamanho da largura do triangulo: "))
#Cria um laco de repeticao para desenhar
for i in range(largura):
    #Se for a primeira iteracao ou a ultima
    if i == 0 or i == largura - 1:
        #Desenha uma linha com base caracteres
        print('*' * base)
    #Senao
    else:
        #Desenha a linha lateral
        print('*'+ " " * (base - 2)+ "*")