import pygame ,sys, random, os
# from character import Character
# from bullet import Bullet
# from bg import Bg
# from enemy import Enemy
# from bonus import Bonus
# from max_level import *
# from resourcePath import resource_path

# Inicializa Pygame con la resolución de pantalla nativa
pygame.init()
display_info = pygame.display.Info()
WIDTH, HEIGHT = display_info.current_w, display_info.current_h
SIDE_BLOCK = WIDTH * 0.05
# CELL_NUM = 24
# WIDTH_CELL_NUM = 20
# WIDTH = SIDE_BLOCK * WIDTH_CELL_NUM
# HEIGHT = SIDE_BLOCK * CELL_NUM
FRAMERATE = 30
