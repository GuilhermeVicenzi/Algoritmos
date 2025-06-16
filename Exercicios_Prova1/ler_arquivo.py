import csv
#Inicializa as variaveis maior e menor
maior = 0
menor = 100000
#Abre o arquivo
arquivo = open('numeros.csv', mode='r')
leitor = csv.reader(arquivo)
#Cria um laco de repeticao para percorrer o arquivo
for i in leitor:
    i = int(i[0])
    #Se o valor atual for maior que a variavel maior
    if i > maior:
        #Maior recebe o valor atual
        maior = i
    # #Senão se o valor atual for menor que a variavel menor
    if i < menor:
       #Menor recebe o valor atual
        menor = i
#Cria um arquivo
novo_arquivo = open('maior_e_menor.csv', mode='w')
escritor = csv.writer(novo_arquivo)
#Grava nele as 2 variaveis
escritor.writerow([maior])
escritor.writerow([menor])