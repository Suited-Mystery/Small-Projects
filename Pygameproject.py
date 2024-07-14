import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect((300, 400, 25, 25))

run = True
while run:
    screen.fill((0, 0, 0))

    key = pygame.key.get_pressed()
    if key[pygame.K_w] == True:
        player.move_ip(0, -1)
    if key[pygame.K_a] == True:
        player.move_ip(-1, 0)
    if key[pygame.K_s] == True:
        player.move_ip(0, 1)
    if key[pygame.K_d] == True:
        player.move_ip(1, 0)

    pygame.draw.rect(screen, (0, 120, 150), player)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()