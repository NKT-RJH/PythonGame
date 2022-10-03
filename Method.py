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

def SetScreen(event, resolution):
    if event.key == ord('f'):
                user32 = ctypes.windll.user32
                screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
                if pygame.display.get_window_size() == screensize:
                    return pygame.display.set_mode(resolution,RESIZABLE)
                else:
                    user32 = ctypes.windll.user32
                    return pygame.display.set_mode(screensize,FULLSCREEN)