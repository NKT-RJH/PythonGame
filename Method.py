import ctypes
import sys
import pygame
import pygame.locals
from pygame.locals import *

def Play(name):
    pygame.init()
    pygame.display.set_caption(name)

def Exit(event):
    if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()