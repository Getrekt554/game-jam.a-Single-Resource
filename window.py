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
        self.clicked_dif = pygame.Vector2(0, 0)
        self.run = True


    
    def draw(self):
        if self.run:
            self.surface.fill((250,250,250))
            self.exit.pos = (self.pos[0] + self.width - 31, self.pos[1])
            self.exit.draw()
            self.screen.blit(self.window_topper, self.pos)

        #window exit button stuff
        if self.exit.clickable() and pygame.mouse.get_just_released()[0]:
            self.run = False
        
        #window drag stuff
        if pygame.mouse.get_pos()[0] >= self.pos[0] and pygame.mouse.get_pos()[0] <= self.pos[0] + self.width:
           if pygame.mouse.get_pos()[1] >= self.pos[1] and pygame.mouse.get_pos()[1] <= self.pos[1] + 31:
                if pygame.mouse.get_just_pressed()[0]:
                    self.dragged = True
                    self.clicked_dif = pygame.Vector2(pygame.mouse.get_pos()) - self.pos
        if pygame.mouse.get_just_released()[0] and self.dragged == True:
            self.dragged = False
        
        if self.dragged == True:
            self.pos = pygame.Vector2(pygame.mouse.get_pos()) + -self.clicked_dif