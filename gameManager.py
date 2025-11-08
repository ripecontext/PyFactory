import pygame

class GameManager:

    def __init__(self, window):

        self.window = window
        self.main_font = pygame.font.SysFont("Bebas Neue", 30)

        self.entities = []

        self.camera_position = [0, 0]
        self.zoom_level = 1

        self.control_state = {
            "up": False,
            "down": False,
            "left": False,
            "right": False,
            "l_click": False,
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
        win_size = self.window.get_size()
        zoom_ratio = (self.zoom_level + zoom_step) / (self.zoom_level)
        if(self.control_state["scrl_up"]):
            self.zoom_level += zoom_step
        if(self.control_state["scrl_down"]):
            self.zoom_level -= zoom_step

        for entity in self.entities:
            if entity.mouse_over(mouse_pos, self.camera_position, self.zoom_level):
                entity.color = (255,0,0)
            else:
                entity.color = (255,255,255)

    def draw(self, delta_time, mouse_pos):

        # draw test rect

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