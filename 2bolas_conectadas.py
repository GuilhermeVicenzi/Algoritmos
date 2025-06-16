import pygame
import math

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

c1_x, c1_y = 100, 300
distancia_max = 100

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    screen.fill("black")

    x, y = pygame.mouse.get_pos()

    # Distância entre os pontos
    distancia_x = x - c1_x
    distancia_y = y - c1_y
    distancia = math.hypot(distancia_x, distancia_y)

    if distancia > distancia_max:
        # Normaliza o vetor (dx, dy)
        distancia_x /= distancia
        distancia_y /= distancia

        # Posiciona c1 na borda da distância máxima
        c1_x = x - distancia_x * distancia_max
        c1_y = y - distancia_y * distancia_max

    # Desenha os círculos
    pygame.draw.circle(screen, (255, 255, 255), (x, y), 25, 5)
    pygame.draw.circle(screen, (255, 255, 255), (int(c1_x), int(c1_y)), 25, 5)

    # Linha conectando os círculos
    pygame.draw.line(screen, (100, 255, 100), (x, y), (int(c1_x), int(c1_y)), 2)

    pygame.display.flip()
    clock.tick(60)
