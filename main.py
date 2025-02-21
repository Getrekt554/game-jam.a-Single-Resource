import pygame
from button import *
from window import *

pygame.init()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
run = True   


exitButton = Button(screen, (screen.get_width() - 50, 0), 50, 45, (255,255,255))

newWindow = window(screen, (300, 300), 500, 350)

while run:
    mouse_state = pygame.mouse.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN and mouse_state[0]:
            if exitButton.clickable() and exitButton.mode == 'down':
                run = False
        elif event.type == pygame.MOUSEBUTTONUP and mouse_state[0] and exitButton.mode == 'up' and exitButton.clickable():
            run = False
    
    screen.fill((0,0,0))
    pygame.display.set_caption(str(clock.get_fps()))
    clock.tick(60)

    pygame.draw.rect(screen, (200,200,200), pygame.Rect(0, 0, screen.get_width(), 45))

    newWindow.draw()

    exitButton.draw()

    pygame.display.flip()
    
pygame.quit()