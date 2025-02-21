import pygame
from button import *

class window():
    def __init__(self, surface, pos, width, height):
        self.surface = surface
        self.pos = pos
        self.width = width
        self.height = height
    
    def draw(self):
        pygame.draw.rect(self.surface,(200,200,200), pygame.Rect(self.pos[0], self.pos[1]), self.width, self.height)