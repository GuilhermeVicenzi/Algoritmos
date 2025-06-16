import pygame
import math

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

# Posições iniciais
c1_x, c1_y = 300, 400
c2_x, c2_y = 200, 300

distancia_max = 100

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        
    screen.fill("black")
    
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    # ---------- Bola 1 puxada pelo mouse ----------
    dx1 = c1_x - mouse_x
    dy1 = c1_y - mouse_y
    dist1 = math.hypot(dx1, dy1)

    if dist1 > distancia_max:
        dx1 /= dist1
        dy1 /= dist1
        c1_x = mouse_x + dx1 * distancia_max
        c1_y = mouse_y + dy1 * distancia_max

    # ---------- Bola 2 puxada por Bola 1 ----------
    dx2 = c2_x - c1_x
    dy2 = c2_y - c1_y
    dist2 = math.hypot(dx2, dy2)

    if dist2 > distancia_max:
        dx2 /= dist2
        dy2 /= dist2
        c2_x = c1_x + dx2 * distancia_max
        c2_y = c1_y + dy2 * distancia_max

    # ---------- Desenho ----------
    pygame.draw.circle(screen, (255, 255, 255), (mouse_x, mouse_y), 25, 5)
    pygame.draw.circle(screen, (255, 255, 255), (int(c1_x), int(c1_y)), 25, 5)
    pygame.draw.circle(screen, (255, 255, 255), (int(c2_x), int(c2_y)), 25, 5)

    pygame.draw.line(screen, (100, 255, 100), (mouse_x, mouse_y), (int(c1_x), int(c1_y)), 2)
    pygame.draw.line(screen, (100, 255, 100), (int(c1_x), int(c1_y)), (int(c2_x), int(c2_y)), 2)
    
    pygame.display.flip()
    clock.tick(60)
