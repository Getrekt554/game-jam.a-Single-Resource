import pygame
from button import *

class window():
    def __init__(self, screen, pos, width, height):
        self.screen = screen
        self.pos = pos
        self.width = width
        self.height = height
        self.exit = Button(self.screen, self.pos, 50, 50, "red")
    
    def draw(self):
        pygame.draw.rect(self.screen,(200,200,200), pygame.Rect(self.pos[0], self.pos[1], self.width, self.height))
        self.exit.draw()