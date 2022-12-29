import os
import pygame
resources = os.path.join(os.getcwd(), "Resources")

backgroundX = 1280
backgroundY = 720
background = pygame.image.load(os.path.join(resources, "Background.jpg"))
background = pygame.transform.scale(background, (backgroundX,backgroundY))

player = pygame.image.load(os.path.join(resources, "2", "Idle2.png"))

playerSize = player.get_rect().size
playerX = backgroundX/2 - playerSize[0]/2
playerY = backgroundY - playerSize[1]

#split.py -n 6 C:\Users\RJH\Desktop\PythonGame\Resources\2\Idle2.png