import pygame
import math

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

#Variaveis de controle
quantidade = 50
tamanho = 20
distancia = 20
distancia_maxima = 20

#Cria uma lista de posicoes. Cada elemento da lista e uma lista contendo as coordendas.
def posicoes(n, d):
    lista = [] * n
    x, y = 0, 0
    distancia = d
    for i in range(n):
        if i == 0:
            x, y = pygame.mouse.get_pos()
        else:
            par_anterior = lista[i-1]
            x = par_anterior[0] - distancia
            y = par_anterior[1] - distancia
        valores = [x, y] 
        lista.append(valores)
            
    return lista

#Verifica a distancia das posicoes das bolas. Se a distancia for maior que a distancia maxima,
#Normaliza o vetor da distancia, e estabelece a nova posicao
def atualiza_posicoes(lista, d):
    dist_max = d
    for i in range(len(lista)):
        if i == 0:
            lista[0] = pygame.mouse.get_pos()
        else:
            par_atual = lista[i]
            par_anterior = lista[i-1]
            
            x_1, y_1 = par_anterior
            x_2, y_2 = par_atual
            
            d_x = x_2 - x_1
            d_y = y_2 - y_1
            dist = math.hypot(d_x, d_y)
            
            if dist > dist_max:
                d_x /= dist
                d_y /= dist
                
                x_2 = x_1 + d_x * dist_max
                y_2 = y_1 + d_y * dist_max
                
                valores = [int(x_2), int(y_2)]
                lista[i] = valores
                
    return lista

#Desenha as bolas na tela usando a lista de coordenadas
def desenha(lista, tamanho):
    tamanho = tamanho
    for i in range(len(lista)):
        pygame.draw.circle(screen, (100, 255, 50), lista[i], tamanho, tamanho)
        

bolas = posicoes(quantidade, distancia)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        
    
    
    screen.fill("black")
    
    bolas = atualiza_posicoes(bolas, distancia_maxima)    
    desenha(bolas, 10)
    
    pygame.display.flip()
    clock.tick(60)