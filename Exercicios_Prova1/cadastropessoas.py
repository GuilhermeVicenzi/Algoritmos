import csv
#Pedir o numero de pessoas que serao cadastradas (q)
q = int(input("Digite quantas pessoas quer cadastrar: "))
#cria um laço de repeticao para cadastrar todas as pessoas
for i in range(q):
    #pede o nome da pessoa e armazena
    nome = str(input("Digite o nome da pessoa que quer cadastrar: "))
    #pede o numero da pessoa e armazena
    numero = str(input("Digite o número da pessoa que quer cadastrar: "))
    #pede o email da pessoa e armazena
    email = str(input("Digite o email da pessoa que quer cadastrar: "))
    #cria e adiciona os dados no arquivo 
    with open('cadastros.csv', mode='w', newline='')as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([nome])
        escritor.writerow([numero])
        escritor.writerow([email])