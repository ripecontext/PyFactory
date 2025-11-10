import pygame

from utilities import convert_to_screenspace_coords

class Tile:

    def __init__(self, position, texture, texture_coord):

        self.position = [position[0] * 32, position[1] * 32]
        self.texture = pygame.image.load(texture).subsurface(texture_coord+[32,32])
        
    def draw(self, window, offset, zoom):

        adjusted_position = convert_to_screenspace_coords(self.position, offset, zoom)
        scaled_texture = pygame.transform.scale(self.texture, [32*zoom,32*zoom])

        window.blit(scaled_texture,adjusted_position)