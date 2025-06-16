#Recebe as dimensões do terreno e armazena
terreno_largura = int(input("Digite a largura do terreno: "))
terreno_comprimento = int(input("Digite o comprimento do terreno: "))
#Recebe as dimensões da casa e armazena
casa_largura = int(input("Digite a largura da casa: "))
casa_comprimento = int(input("Digite o comprimento da casa: "))
#Calcula a area do terreno
area_terreno = terreno_comprimento * terreno_largura
#Calcula a area da casa
area_casa = casa_comprimento * casa_largura
#Calcula a area livre do terreno
area_livre = area_terreno - area_casa
#Calcula a area livre do terreno em percentual
area_livre_percentual = (area_livre / area_terreno) * 100
#Mostra os valores
print(f"A área livre do terreno é {area_livre}mt^2 / {area_livre_percentual}")