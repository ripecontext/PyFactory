import pygame

class Entity:

    def __init__(self, position, size, color):

        self.position = position
        self.size = size
        self.color = color

    def update(self):

        pass

    def draw(self, window):

        pygame.draw.rect(window, self.color, self.position + self.size)