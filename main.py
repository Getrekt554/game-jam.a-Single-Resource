import pygame
from button import *
from window import *

pygame.init()
screen = pygame.display.set_mode((1024,768))
clock = pygame.time.Clock()
run = True   


exitButton = Button(screen, (screen.get_width() - 50, 0), 50, 45, (255,0,0), (190,0,0))

windows = []

for i in range(2):
    windows.append(Window(screen, (300, 300 + (100 * i)), 350, 350, i, "default"))

while run:
    for window in windows:
        window.dragging(windows)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if exitButton.clickable() and pygame.mouse.get_just_released()[0]:
        run = False
            
    screen.fill((0,0,0))
    pygame.display.set_caption(str(clock.get_fps()))

    for newWindow in reversed(windows):
        newWindow.render()


    #top bar and exit button
    pygame.draw.rect(screen, (200,200,200), pygame.Rect(0, 0, screen.get_width(), 45))
    exitButton.draw()

    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()