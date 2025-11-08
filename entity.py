import pygame

from utilities import convert_to_screenspace_coords

class Entity:

    def __init__(self, position, size, color):

        self.position = position
        self.size = size
        self.color = color

    def update(self):

        pass

    def draw(self, window, offset, zoom):

        corrected_position = convert_to_screenspace_coords(self.position, offset, zoom)
        corrected_size = [self.size[0] * zoom, self.size[1] * zoom]

        pygame.draw.rect(window, self.color, corrected_position + corrected_size)

    def mouse_over(self, point, offset, zoom):

        corrected_position = convert_to_screenspace_coords(self.position, offset, zoom)
        corrected_size = [self.size[0] * zoom, self.size[1] * zoom]

        return (corrected_position[0] < point[0] < corrected_position[0] + corrected_size[0] and
                corrected_position[1] < point[1] < corrected_position[1] + corrected_size[1])