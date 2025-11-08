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

        self.entities = []

    def update(self, delta_time, mouse_pos):

        if(self.control_state["up"]):
            self.entities[0].position[1] -= 100 * delta_time
        if(self.control_state["down"]):
            self.entities[0].position[1] += 100 * delta_time
        if(self.control_state["right"]):
            self.entities[0].position[0] += 100 * delta_time
        if(self.control_state["left"]):
            self.entities[0].position[0] -= 100 * delta_time

        if (self.control_state["l_click"]) and self.entities[0].is_within(mouse_pos):
            self.entities[0].color = (255,0,0)
        else:
            self.entities[0].color = (255,255,255)

    def draw(self, delta_time, mouse_pos):

        # draw test rect

        for entity in self.entities:

            entity.draw(self.window)

        # what keys are pressed?

        keys_pressed_string = f"Up: {self.control_state["up"]} Down: {self.control_state["down"]} Left: {self.control_state["left"]} Right: {self.control_state["right"]} Left Click: {self.control_state["l_click"]} Mouse Position: X:{mouse_pos[0]} Y:{mouse_pos[1]}"
        keys_pressed = self.main_font.render(keys_pressed_string, False, (255,255,255))
        self.window.blit(keys_pressed,(0,100))

        # FPS counter

        fps = str(int(1 / delta_time))
        fps_counter = self.main_font.render(f"{fps}FPS", False, (255,255,255))
        self.window.blit(fps_counter,(0,0))