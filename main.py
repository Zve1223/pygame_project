import pygame
import levels

pygame.init()

while True:
    levels.current_level = levels.current_level.launch()
