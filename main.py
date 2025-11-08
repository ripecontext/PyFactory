import pygame

window = pygame.display.set_mode((960,540))
pygame.display.set_caption("PyFactory")

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((0,0,0))

    pygame.draw.rect(window, (255,255,255), (40,40,500,500))

    pygame.display.flip()