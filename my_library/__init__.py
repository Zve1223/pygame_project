import pygame
from constants import MAX_FPS
from object import Object
from hierarchy import Hierarchy
from component import Component
from constants import WIN_SIZE


screen = pygame.display.set_mode(WIN_SIZE)
DT = 1.0 / MAX_FPS
FDT = 1.0 / 30.0
