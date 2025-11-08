import pygame
import time

from gameManager import GameManager
from entity import Entity

pygame.font.init()
window = pygame.display.set_mode((960,540))
pygame.display.set_caption("PyFactory")

manager = GameManager(window)
manager.entities.append(Entity([100,100], [100,100], (255, 255, 255)))

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

    mouse_position = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type in [pygame.KEYDOWN, pygame.KEYUP] and event.key in control_map.keys():
            manager.control_state[control_map[event.key]] = event.type == pygame.KEYDOWN 
        elif event.type in [pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP] and event.button in control_map.keys():
            manager.control_state[control_map[event.button]] = event.type == pygame.MOUSEBUTTONDOWN

    # gameloop

    window.fill((0,0,0))

    manager.update(delta_time, mouse_position)
    manager.draw(delta_time, mouse_position)

    pygame.display.flip()