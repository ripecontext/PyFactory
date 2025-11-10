import pygame

from utilities import convert_to_screenspace_coords

class Tile:

    def __init__(self, position, color):

        self.position = [position[0] * 32, position[1] * 32]
        self.color = color
        
    def draw(self, window, offset, zoom):

        adjusted_position = convert_to_screenspace_coords(self.position, offset, zoom)

        pygame.draw.rect(window, self.color, adjusted_position+[32*zoom,32*zoom],1)