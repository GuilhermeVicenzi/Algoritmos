#Declara a distancia a ser percorrida e armazena
distancia_total = 240
#Declara o rendimento do carro km/l
rendimento = 19
#Declara a capacidade do tanque do carro
capacidade = 55
#Declara o vetor das distancias entre os postos
postos = [30, 100, 170, 240]
#Declara a velocidade
velocidade = 80
#Declara o tempo de abastecimento
tempo_abastecimento = 10
#inicializa o tempo da viagem
tempo = 0
#Pede quanta gasolina tem no carro
gasolina = int(input("Digite quanta gasolina tem no carro: "))
#Inicializa a variavel da posicao_atual
posicao_atual = 0
#Enquanto a posicao_atual for diferente da distancia total:
while posicao_atual != distancia_total:
    #Se a posicao for multiplo do rendimento
    print(f"O carro está em {posicao_atual}, com {gasolina} gasolina")
    if posicao_atual % rendimento == 0:
        #Decrementa a gasolina no carro
        gasolina -= 1
    #Se posicao atual for igual ao km de um posto:
    if posicao_atual in postos:
        indice = int(postos.index(posicao_atual))
        #Se o tanque tiver menos de 25%
        if gasolina < capacidade / 4:
            #Adiciona gasolina em tanque
            gasolina += 20
            #Adiciona tempo de abastecimento em total
            tempo += tempo_abastecimento
            print(f"Parou no posto, e agora tem {gasolina} gasolina")
        #Senão verifica se tem gasolina para chegar no proximo posto
        elif (gasolina * rendimento) > postos[indice + 1]:
            #Se tiver, segue viagem
            print("Não parou no posto atual")
        #Senão abastece
        else:
            #Adiciona gasolina em tanque
            gasolina += 20
            #Adiciona tempo de abastecimento em total
            tempo += tempo_abastecimento
            print("Parou no posto pois não iria conseguir chegar no próximo")
    #Incrementa posicao atual
    posicao_atual += 1

tempo += (distancia_total / velocidade) * 60


#Inicializa as variaveis hora e segundos
horas = 0
segundos = 0
#Se o tempo for divisivel por 60:
if tempo // 60 >= 1:
    #Adiciona o quociente da divisao em horas
    horas = int(tempo / 60)
    #Minutos recebe o resto da divisao
    minutos = int(tempo - (horas * 60))
#Mostra o resultado da conversao
print(f"A viagem durou exatamente: {horas}h {minutos}m {segundos}s.")