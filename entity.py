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

    def is_within(self, point):

        return (self.position[0] < point[0] < self.position[0] + self.size[0] and
                self.position[1] < point[1] < self.position[1] + self.size[1])