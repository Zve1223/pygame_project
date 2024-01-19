import pygame

import my_library.constants
from my_library.vector2 import Vector2
from my_library.transform import Transform
from my_library.component import Component
from my_library.object import Object
from my_library.hierarchy import Hierarchy
from my_library.image_renderer import ImageRenderer


screen: pygame.Surface = pygame.display.set_mode(my_library.constants.WIN_SIZE)
