import imp
import pygame
import pygame.locals
import ctypes
import os
import sys
from pygame.locals import *

import Setting
import Function as F

Setting.Play("My Game", F.resolution)

# 현재 위치 정의
current_path = os.path.dirname(__file__)

# 이미지 폴더 위치 정의
resources = os.path.join(current_path, "Resources")

# 불러올 이미지 로드
background = pygame.image.load(os.path.join(resources, "Background.png"))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == ord('f'):
                screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
                if pygame.display.get_window_size() == screensize:
                    F.screen = pygame.display.set_mode(F.resolution,RESIZABLE)
                else:
                    user32 = ctypes.windll.user32
                    F.screen = pygame.display.set_mode(screensize,FULLSCREEN)
            
    F.screen.fill((255,255,255))
    pygame.display.flip()
    F.fpsClock.tick(F.fps)