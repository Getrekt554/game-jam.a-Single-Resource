import pygame
from button import *

pygame.init()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
run = True   


exitButton = Button(screen, (screen.get_width() - 50, 0), 50, 45, (255,255,255))

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    screen.fill((0,0,0))
    pygame.display.set_caption(str(clock.get_fps()))
    clock.tick(60)

    pygame.draw.rect(screen, (200,200,200), pygame.Rect(0, 0, screen.get_width(), 45))


    exitButton.draw()
    if exitButton.clickable() and pygame.mouse.get_just_released()[0]:
        run = False

    pygame.display.flip()
    
pygame.quit()