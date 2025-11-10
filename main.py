import pygame
import time
import random

from gameManager import GameManager
from entity import Entity
from tile import Tile

pygame.font.init()
window = pygame.display.set_mode((960,540))
pygame.display.set_caption("PyFactory")

stone_tilemap = pygame.image.load("resources/tiles/stone.png")
offsets = [[0,64],[32,64],[0,96],[32,96]]

manager = GameManager(window)

for x in range(1024):
    manager.tiles.append(Tile([x % 32, x // 32],[100,100,100]))

control_map = {
    pygame.K_w: "up",
    pygame.K_s: "down",
    pygame.K_a: "left",
    pygame.K_d: "right",
    1: "l_click",
    3: "r_click",
    4: "scrl_up",
    5: "scrl_down"
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

    # reset scrolls

    manager.control_state[control_map[4]] = False
    manager.control_state[control_map[5]] = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type in [pygame.KEYDOWN, pygame.KEYUP] and event.key in control_map.keys():
            manager.control_state[control_map[event.key]] = event.type == pygame.KEYDOWN 
        elif event.type in [pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP] and event.button in [1,3]:
            manager.control_state[control_map[event.button]] = event.type == pygame.MOUSEBUTTONDOWN
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button in[4,5]:
            manager.control_state[control_map[event.button]] = True

    # gameloop

    window.fill((0,0,0))

    manager.update(delta_time, mouse_position)
    manager.draw(delta_time, mouse_position)

    pygame.display.flip()