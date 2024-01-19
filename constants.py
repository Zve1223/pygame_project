import pygame.cursors
from pygame import Color
from math import pi as PI

# Settings

MAX_FPS = 144
WIN_SIZE = (720, 720)

# Level IDs

LevelId = int
LEVEL_0 = 0
LEVEL_1 = 1
LEVEL_2 = 2
LEVEL_3 = 3

# Colors

BLACK = Color(0, 0, 0)
DARK_GREY = Color(63, 63, 63)
GREY = Color(127, 127, 127)
LIGHT_GREY = Color(191, 191, 191)
WHITE = Color(255, 255, 255)

RED = Color(255, 0, 0)
ORANGE = Color(255, 127, 63)
YELLOW = Color(255, 255, 0)
GREEN = Color(0, 255, 0)
LIGHT_BLUE = Color(127, 191, 255)
BLUE = Color(0, 0, 255)
PURPLE = Color(127, 63, 255)
PINK = Color(255, 127, 191)
BROWN = Color(127, 63, 0)


# Constants

PI = PI
DEG2RAD = PI / 180.0
SQRT_TWO = 2 ** 0.5
SQRT_THREE = 3 ** 0.5


# Alignments

Alignment = tuple[float, float]
LEFT_TOP, MIDDLE_TOP, RIGHT_TOP = (0.0, 0.0), (0.5, 0.0), (1.0, 0.0)
LEFT_CENTER, MIDDLE_CENTER, RIGHT_CENTER = (0.0, 0.5), (0.5, 0.5), (1.0, 0.5)
LEFT_BOTTOM, MIDDLE_BOTTOM, RIGHT_BOTTOM = (0.0, 1.0), (0.5, 1.0), (1.0, 1.0)


# Cursors

DEFAULT_CURSOR = pygame.cursors.tri_left
POINTED_CURSOR = pygame.cursors.broken_x


# Mouse buttons

LEFT_BUTTON = pygame.BUTTON_LEFT
RIGHT_BUTTON = pygame.BUTTON_RIGHT
MIDDLE_BUTTON = pygame.BUTTON_MIDDLE
WHEEL_UP_BUTTON = pygame.BUTTON_WHEELUP
WHEEL_DOWN_BUTTON = pygame.BUTTON_WHEELDOWN
MouseButton = LEFT_BUTTON | RIGHT_BUTTON | MIDDLE_BUTTON | WHEEL_UP_BUTTON | WHEEL_DOWN_BUTTON


# Spaces

LOCAL = 0
GLOBAL = 1
Space = LOCAL | GLOBAL

