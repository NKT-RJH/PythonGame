import os
from turtle import back
import pygame

resources = os.path.join(os.getcwd(), "Resources")

background = pygame.image.load(os.path.join(resources, "Background.jpg"))
background = pygame.transform.scale(background, (1920,1080))