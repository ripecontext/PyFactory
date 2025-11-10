import pygame

from utilities import convert_from_screenscape_coords
from entity import Entity

class GameManager:

    def __init__(self, window):

        self.window = window
        self.main_font = pygame.font.SysFont("Bebas Neue", 30)

        self.entities = []
        self.tiles = []

        self.camera_position = [0, 0]
        self.zoom_level = 1

        self.old_win_size = self.window.get_size()

        self.control_state = {
            "up": False,
            "down": False,
            "left": False,
            "right": False,
            "l_click": False,
            "r_click": False,
            "scrl_up": False,
            "scrl_down": False
        }


    def update(self, delta_time, mouse_pos):

        if(self.control_state["up"]):
            self.camera_position[1] -= 100 * delta_time
        if(self.control_state["down"]):
            self.camera_position[1] += 100 * delta_time
        if(self.control_state["right"]):
            self.camera_position[0] += 100 * delta_time
        if(self.control_state["left"]):
            self.camera_position[0] -= 100 * delta_time

        zoom_step = 0.125
        cam_centre = self.calculate_cam_centre()

        if(self.control_state["scrl_up"]) and self.zoom_level < 4:
            
            self.zoom_level += zoom_step

        if(self.control_state["scrl_down"]) and self.zoom_level > 0.125:

            self.zoom_level -= zoom_step

        new_cam_centre = self.calculate_cam_centre()
        difference = [new_cam_centre[0] - cam_centre[0],
                      new_cam_centre[1] - cam_centre[1]]
            
        self.camera_position[0] -= difference[0]
        self.camera_position[1] -= difference[1]

        absolute_mouse_coordinates = convert_from_screenscape_coords(mouse_pos, self.camera_position, self.zoom_level)
        mouse_coords_tile = [absolute_mouse_coordinates[0] % 32, absolute_mouse_coordinates[1] % 32]

        if(self.control_state["l_click"]):
            if not any([entity.mouse_over(mouse_pos, self.camera_position, self.zoom_level) for entity in self.entities]):
                self.entities.append(Entity([mouse_coords_tile[0]*32,mouse_coords_tile[1]*32],[32,32],[0,255,0]))
                print(mouse_coords_tile)

        for entity in self.entities:
            if entity.mouse_over(mouse_pos, self.camera_position, self.zoom_level):
                entity.color = (255,0,0)
            else:
                entity.color = (255,255,255)

    def draw(self, delta_time, mouse_pos):

        # draw tiles

        for tile in self.tiles:

            tile.draw(self.window, self.camera_position, self.zoom_level)

        # draw entities

        for entity in self.entities:

            entity.draw(self.window, self.camera_position, self.zoom_level)

        # what keys are pressed?

        win_size = self.window.get_size()
        cam_centre = [self.camera_position[0] + win_size[0] * 0.5 / self.zoom_level,
                      self.camera_position[1] + win_size[1] * 0.5 / self.zoom_level]

        keys_pressed_string = f"Up: {self.control_state["up"]} Down: {self.control_state["down"]} Left: {self.control_state["left"]} Right: {self.control_state["right"]} Left Click: {self.control_state["l_click"]}"
        more_info_string = f"Mouse Position: X:{mouse_pos[0]} Y:{mouse_pos[1]} Screen Center: X:{cam_centre[0]} Y: {cam_centre[1]}"
        keys_pressed = self.main_font.render(keys_pressed_string, False, (255,255,255))
        self.window.blit(keys_pressed,(0,100))
        more_info = self.main_font.render(more_info_string, False, (255,255,255))
        self.window.blit(more_info,(0,130))

        # FPS counter

        fps = str(int(1 / delta_time))
        fps_counter = self.main_font.render(f"{fps}FPS", False, (255,255,255))
        self.window.blit(fps_counter,(0,0))

        # crosshair

        pygame.draw.circle(self.window, (0,0,255), (win_size[0] / 2, win_size[1] / 2), 3)

    def calculate_cam_centre(self):

        win_size_adjusted = (self.window.get_size()[0] / self.zoom_level, self.window.get_size()[1] / self.zoom_level)
        cam_centre = [self.camera_position[0] + win_size_adjusted[0] / 2,
                      self.camera_position[1] + win_size_adjusted[1] / 2]
        return cam_centre