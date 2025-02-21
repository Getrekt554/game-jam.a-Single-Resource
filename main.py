import pygame
from button import *
from window import *

pygame.init()
screen = pygame.display.set_mode((1024,768), pygame.FULLSCREEN)
clock = pygame.time.Clock()
run = True   


exitButton = Button(screen, (screen.get_width() - 50, 0), 50, 45, (255,0,0))

windows = []

for i in range(2):
    windows.append(Window(screen, (300, 300 + (100 * i)), 500, 350, i))

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if exitButton.clickable() and pygame.mouse.get_just_released()[0]:
        run = False
            
    screen.fill((0,0,0))
    pygame.display.set_caption(str(clock.get_fps()))

    for newWindow in reversed(windows):
        if newWindow.run:
            pygame.draw.rect(newWindow.surface, (0,0,0), pygame.Rect(100,100,50,50))
            newWindow.screen.blit(newWindow.surface, newWindow.pos)
            newWindow.draw()
            newWindow.dragging(windows)

    #top bar and exit button
    pygame.draw.rect(screen, (200,200,200), pygame.Rect(0, 0, screen.get_width(), 45))
    exitButton.draw()

    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()