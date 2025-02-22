import pygame

class game:
    def __init__(self, surface):
        self.surface = surface
        self.playerx = 0
        self.playery = 0

    def draw(self):
        pygame.draw.circle(self.surface, "red", (self.playerx, self.playery), 100)
    
    def update(self):
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] == 1:
            self.playery -= 1
        if keys[pygame.K_s] == 1:
            self.playery += 1
        if keys[pygame.K_a] == 1:
            self.playerx -= 1
        if keys[pygame.K_d] == 1:
            self.playerx += 1
