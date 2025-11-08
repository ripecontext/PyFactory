import pygame
import time

from gameManager import GameManager

pygame.font.init()
window = pygame.display.set_mode((960,540))
pygame.display.set_caption("PyFactory")

manager = GameManager(window)

start_time = time.time()

running = True
while running:

    # get delta time

    current_time = time.time()
    delta_time = current_time - start_time
    start_time = current_time

    # event handling

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # gameloop

    window.fill((0,0,0))

    manager.update(delta_time)
    manager.draw(delta_time)

    pygame.display.flip()