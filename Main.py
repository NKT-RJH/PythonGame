import pygame
import pygame.locals
from pygame.locals import *

import Method
import ResourceManager as RM

fps = 60
fpsClock = pygame.time.Clock()
resolution = [960,540]
screen = pygame.display.set_mode(resolution,RESIZABLE)

Method.Play("My Game")

while True:
    for event in pygame.event.get():
        Method.Exit(event)
        
        if event.type == pygame.KEYDOWN:
            screen = Method.SetScreen(event, resolution)
            
    screen.blit(RM.background, (0,0))
    pygame.display.flip()
    fpsClock.tick(fps)