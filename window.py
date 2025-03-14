import pygame
from button import *
from game import *

class Window:
    def __init__(self, screen, pos, width, height, index, app):
        
        self.screen = screen
        self.pos = pygame.Vector2(pos)  # Use Vector2 for direct manipulation
        self.width = width
        self.height = height
        self.surface = pygame.Surface((width, height))
        self.exit = Button(self.screen, (self.pos.x + self.width - 31, self.pos.y), 31, 31, "red", "red")
        
        self.window_topper = pygame.image.load("resources/window_topper.png")
        self.window_topper = pygame.transform.scale(self.window_topper, (int(self.window_topper.get_width() * (self.width / self.window_topper.get_width())), int(self.window_topper.get_height() * ((self.height / 16) / self.window_topper.get_height()))))
        self.dragged = False
        self.clicked_dif = pygame.Vector2(0, 0)
        self.run = True
        self.index = index
        self.just_moved_to_top = False  # Prevent unnecessary reordering
        self.app = app
        self.game = game(self.surface)

    def render(self):
        if not self.run:
            return
        
        self.surface.fill((250, 250, 250))
        self.exit.pos = (self.pos.x + self.width - 31, self.pos.y)
        self.exit.draw()
        if self.index == 0:
            self.game.update()
        self.game.draw()
        self.screen.blit(self.surface, self.pos)
        self.screen.blit(self.window_topper, self.pos)

    def dragging(self, windows):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_just_pressed()[0]
        mouse_released = pygame.mouse.get_just_released()[0]

        # Check if mouse is in the window title bar and pressed
        if self.pos.x <= mouse_pos[0] <= self.pos.x + self.width - 31 and self.pos.y <= mouse_pos[1] <= self.pos.y + 31:
            if mouse_pressed:
                self.dragged = True
                self.clicked_dif = pygame.Vector2(mouse_pos) - self.pos

                # Move to top only if it wasn't just moved
                if not self.just_moved_to_top:
                    self.push_to_top(windows)
                    self.just_moved_to_top = True  # Prevent reordering in the same drag

        # Release dragging
        if mouse_released:
            self.dragged = False
            self.just_moved_to_top = False  # Reset flag

        # Move window if dragging
        if self.dragged:
            self.pos = pygame.Vector2(mouse_pos) - self.clicked_dif
        
        if self.exit.clickable() and pygame.mouse.get_just_released()[0]:
            self.run = False

    def push_to_top(self, windows):
        if self in windows:
            windows.remove(self)
        windows.insert(0, self)

        # Update indices
        for i, window in enumerate(windows):
            window.index = i  


