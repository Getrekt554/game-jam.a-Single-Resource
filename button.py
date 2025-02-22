import pygame

class Button():
    def __init__(self, surface, pos, width, height, color, hover_color):
        self.surface = surface
        self.pos = pos
        self.width = width
        self.height = height
        self.color = color
        self.mode = 'up'
        self.hover_color = hover_color

    def draw(self):
        if self.clickable():
            pygame.draw.rect(self.surface, self.hover_color, pygame.Rect(self.pos[0], self.pos[1], self.width, self.height))
        else: pygame.draw.rect(self.surface, self.color, pygame.Rect(self.pos[0], self.pos[1], self.width, self.height))

    def clickable(self):
        if pygame.mouse.get_pos()[0] >= self.pos[0] and pygame.mouse.get_pos()[0] <= self.pos[0] + self.width:
            if pygame.mouse.get_pos()[1] >= self.pos[1] and pygame.mouse.get_pos()[1] <= self.pos[1] + self.height:
                return True
