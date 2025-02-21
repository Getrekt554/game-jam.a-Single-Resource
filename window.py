import pygame
from button import *

class window():
    def __init__(self, screen, pos, width, height):
        self.surface = pygame.Surface((width, height))
        self.screen = screen
        self.pos = pos
        self.width = width
        self.height = height
        self.exit = Button(self.screen, (self.pos[0] + self.width - 31, self.pos[1]), 31, 31, "red")
        self.window_topper = pygame.image.load("resources/window_topper.png")
        self.window_topper = pygame.transform.scale_by(self.window_topper, 3.90625)
        self.dragged = False
    
    def draw(self):
        self.surface.fill((250,250,250))
        self.screen.blit(self.surface, self.pos)
        self.exit.pos = (self.pos[0] + self.width - 31, self.pos[1])
        self.exit.draw()
        self.screen.blit(self.window_topper, self.pos)
    
    def clickable(self):
       if pygame.mouse.get_pos()[0] >= self.pos[0] and pygame.mouse.get_pos()[0] <= self.pos[0] + self.width:
           if pygame.mouse.get_pos()[1] >= self.pos[1] and pygame.mouse.get_pos()[1] <= self.pos[1] + self.height:
               return True