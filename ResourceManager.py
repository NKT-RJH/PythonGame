import os
import pygame
import PIL

resources = os.path.join(os.getcwd(), "Resources")

background = pygame.image.load(os.path.join(resources, "Background.jpg"))
background = pygame.transform.scale(background, (1920,1080))

player = pygame.image.load(os.path.join(resources, "2", "Idle2.png"))

playerSize = player.get_rect().size
playerX = 1920/2 - playerSize[0]/2
playerY = 1080 - playerSize[1]

#split.py -n 6 C:\Users\RJH\Desktop\PythonGame\Resources\2\Idle2.png