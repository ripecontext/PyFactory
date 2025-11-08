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

        pygame.draw.rect(window, self.color, corrected_position + self.size * zoom)

    def mouse_over(self, point, offset, zoom):

        corrected_position = convert_to_screenspace_coords(self.position, offset, zoom)

        return (corrected_position[0] < point[0] < corrected_position[0] + self.size[0] * zoom and
                corrected_position[1] < point[1] < corrected_position[1] + self.size[1] * zoom)