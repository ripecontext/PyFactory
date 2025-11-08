import pygame

class GameManager:

    def __init__(self, window):

        self.window = window
        self.main_font = pygame.font.SysFont("Bebas Neue", 30)

        self.control_state = {
            "up": False,
            "down": False,
            "left": False,
            "right": False,
            "l_click": False
        }

        self.rect_coords = [100, 100]
        self.rect_color = (255,255,255)

    def update(self, delta_time):

        if(self.control_state["up"]):
            self.rect_coords[1] += 100 * delta_time
        if(self.control_state["down"]):
            self.rect_coords[1] -= 100 * delta_time
        if(self.control_state["right"]):
            self.rect_coords[0] += 100 * delta_time
        if(self.control_state["left"]):
            self.rect_coords[0] -= 100 * delta_time

        if (self.control_state["l_click"]):
            self.rect_color = (255,0,0)
        else:
            self.rect_color = (255,255,255)

    def draw(self, delta_time):

        # draw test rect

        pygame.draw.rect(self.window, self.rect_color, self.rect_coords + [40,40])

        # what keys are pressed?

        keys_pressed_string = f"Up: {self.control_state["up"]} Down: {self.control_state["down"]} Left: {self.control_state["left"]} Right: {self.control_state["right"]} Left Click: {self.control_state["l_click"]}"
        keys_pressed = self.main_font.render(keys_pressed_string, False, (255,255,255))
        self.window.blit(keys_pressed,(0,100))

        # FPS counter

        fps = str(int(1 / delta_time))
        fps_counter = self.main_font.render(f"{fps}FPS", False, (255,255,255))
        self.window.blit(fps_counter,(0,0))