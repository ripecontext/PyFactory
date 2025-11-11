import pygame

from entity import Entity
from utilities import convert_to_screenspace_coords

class Belt(Entity):

    def __init__(self, position, color, rotation):

        super().__init__(position, [32,32], color)

        self.rotation = rotation

    def update(self, delta):

        pass

    def draw(self, window, offset, zoom):

        walls = [[0,0],[1,0],[0,1],[1,1]]
        arrow = [[[0.6,0,5],[0.4,0.4],[0.4,0.6]],
                 [[0.5,0.6],[0.4,0.4],[0.6,0.4]],
                 [[0.4,0.5],[0.6,0.4],[0.6,0.6]],
                 [[0.5,0.4],[0.6,0.6],[0.4,0.6]]]
        
        if self.rotation % 2 != 0:
            walls[1], walls[2] = walls[2], walls[1]
        
        line_points_one_one = [self.position[0] + walls[0][0] * 32, self.position[1] + walls[0][1] * 32]
        line_points_one_two = [self.position[0] + walls[1][0] * 32, self.position[1] + walls[1][1] * 32]
        line_points_two_one = [self.position[0] + walls[2][0] * 32, self.position[1] + walls[2][1] * 32]
        line_points_two_two = [self.position[0] + walls[3][0] * 32, self.position[1] + walls[3][1] * 32]

        line_one_one_adjusted = convert_to_screenspace_coords(line_points_one_one, offset, zoom)
        line_one_two_adjusted = convert_to_screenspace_coords(line_points_one_two, offset, zoom)
        line_two_one_adjusted = convert_to_screenspace_coords(line_points_two_one, offset, zoom)
        line_two_two_adjusted = convert_to_screenspace_coords(line_points_two_two, offset, zoom)

        pygame.draw.line(window, self.color, line_one_one_adjusted, line_one_two_adjusted, 5)
        pygame.draw.line(window, self.color, line_two_one_adjusted, line_two_two_adjusted, 5)

        arrow_points = arrow[self.rotation]
        final_points = []
        for point in arrow_points:
            arrow_points_offset = [self.position[0] + point[0] * 32,
                                   self.position[1] + point[1] * 32]
            arrow_points_adjusted = convert_to_screenspace_coords(arrow_points_offset, offset, zoom)
            final_points.append(arrow_points_adjusted)

        pygame.draw.polygon(window, self.color, final_points)