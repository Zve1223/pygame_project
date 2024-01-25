from my_library.types import *
from my_library.constants import *
from my_library.utilities import *
from my_library.input import *
from my_library.time import *

from my_library.vector2 import Vector2
from my_library.components.transform import Transform
from my_library.component import Component
from my_library.game_object import GameObject
from my_library.hierarchy import Hierarchy

from my_library.components import *

from my_library.level import Level
from my_library.levels import level0

import pygame


pygame.init()


hierarchy = Hierarchy()

levels: tuple[Level, ...] = (
    Level('Menu', level0.declare_variables),
)

current_level = levels[0]
screen: pygame.Surface = pygame.display.set_mode(WIN_SIZE)
