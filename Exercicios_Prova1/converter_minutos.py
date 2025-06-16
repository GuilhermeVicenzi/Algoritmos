#Pede o tempo e armazena em minutos
minutos = int(input("Digite quantos minutos quer converter "))
#Inicializa as variaveis hora e segundos
horas = 0
segundos = 0
#Se o tempo for divisivel por 60:
if minutos // 60 >= 1:
    #Adiciona o quociente da divisao em horas
    horas = int(minutos / 60)
    #Minutos recebe o resto da divisao
    minutos = minutos - (horas * 60)
#Mostra o resultado da conversao
print(f"{horas}h {minutos}m {segundos}s.")