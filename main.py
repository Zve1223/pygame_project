import pygame
from my_library import levels

pygame.init()

while True:
    levels.current_level = levels.levels[levels.current_level.launch()]
