import pygame
import time

from gameManager import GameManager

pygame.font.init()
window = pygame.display.set_mode((960,540))
pygame.display.set_caption("PyFactory")

manager = GameManager(window)

control_map = {
    pygame.K_w: "up",
    pygame.K_s: "down",
    pygame.K_a: "left",
    pygame.K_d: "right",
    1: "l_click"
}

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
        elif event.type in [pygame.KEYDOWN, pygame.KEYUP] and event.key in control_map.keys():
            manager.control_state[control_map[event.key]] = 1 if event.type == pygame.KEYDOWN else 0
        elif event.type in [pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP] and event.button in control_map.keys():
            manager.control_state[control_map[event.button]] = 1 if event.type == pygame.MOUSEBUTTONDOWN else 0

    # gameloop

    window.fill((0,0,0))

    manager.update(delta_time)
    manager.draw(delta_time)

    pygame.display.flip()