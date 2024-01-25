import pygame.cursors
from pygame import Color
from math import pi as PI
from my_library.types import *


# Settings

MAX_FPS = 144
WIN_SIZE = (720, 720)


# Level IDs

LEVEL_0: LevelId = LevelId(0)
LEVEL_1: LevelId = LevelId(1)
LEVEL_2: LevelId = LevelId(2)
LEVEL_3: LevelId = LevelId(3)


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

LEFT_TOP:      Alignment = Alignment((0.0, 0.0))
MIDDLE_TOP:    Alignment = Alignment((0.5, 0.0))
RIGHT_TOP:     Alignment = Alignment((1.0, 0.0))
LEFT_CENTER:   Alignment = Alignment((0.0, 0.5))
MIDDLE_CENTER: Alignment = Alignment((0.5, 0.5))
RIGHT_CENTER:  Alignment = Alignment((1.0, 0.5))
LEFT_BOTTOM:   Alignment = Alignment((0.0, 1.0))
MIDDLE_BOTTOM: Alignment = Alignment((0.5, 1.0))
RIGHT_BOTTOM:  Alignment = Alignment((1.0, 1.0))


# Cursors

DEFAULT_CURSOR = pygame.cursors.tri_left
POINTED_CURSOR = pygame.cursors.broken_x


# Mouse buttons

LEFT_BUTTON:       MouseButton = MouseButton(pygame.BUTTON_LEFT)
RIGHT_BUTTON:      MouseButton = MouseButton(pygame.BUTTON_RIGHT)
MIDDLE_BUTTON:     MouseButton = MouseButton(pygame.BUTTON_MIDDLE)
WHEEL_UP_BUTTON:   MouseButton = MouseButton(pygame.BUTTON_WHEELUP)
WHEEL_DOWN_BUTTON: MouseButton = MouseButton(pygame.BUTTON_WHEELDOWN)


# Spaces

LOCAL:  Space = Space(0)
GLOBAL: Space = Space(1)


# Keys

K_ESC:                  Key = Key(1)
K_1:                    Key = Key(2)
K_2:                    Key = Key(3)
K_3:                    Key = Key(4)
K_4:                    Key = Key(5)
K_5:                    Key = Key(6)
K_6:                    Key = Key(7)
K_7:                    Key = Key(8)
K_8:                    Key = Key(9)
K_9:                    Key = Key(10)
K_0:                    Key = Key(11)
K_DASH:                 Key = Key(12)
K_EQUALS:               Key = Key(13)
K_BACKSPACE:            Key = Key(14)
K_TAB:                  Key = Key(15)
K_Q:                    Key = Key(16)
K_W:                    Key = Key(17)
K_E:                    Key = Key(18)
K_R:                    Key = Key(19)
K_T:                    Key = Key(20)
K_Y:                    Key = Key(21)
K_U:                    Key = Key(22)
K_I:                    Key = Key(23)
K_O:                    Key = Key(24)
K_P:                    Key = Key(25)
K_LEFT_SQUARE_BRACKET:  Key = Key(26)
K_RIGHT_SQUARE_BRACKET: Key = Key(27)
K_ENTER:                Key = Key(28)
K_RIGHT_CTRL:           Key = Key(29)
K_CTRL:                 Key = Key(29)
K_A:                    Key = Key(30)
K_S:                    Key = Key(31)
K_D:                    Key = Key(32)
K_F:                    Key = Key(33)
K_G:                    Key = Key(34)
K_H:                    Key = Key(35)
K_J:                    Key = Key(36)
K_K:                    Key = Key(37)
K_L:                    Key = Key(38)
K_SEMICOLON:            Key = Key(39)
K_QUOTE:                Key = Key(40)
K_APOSTROPHE:           Key = Key(41)
K_SHIFT:                Key = Key(42)
K_SLASH:                Key = Key(43)
K_Z:                    Key = Key(44)
K_X:                    Key = Key(45)
K_C:                    Key = Key(46)
K_V:                    Key = Key(47)
K_B:                    Key = Key(48)
K_N:                    Key = Key(49)
K_M:                    Key = Key(50)
K_COMMA:                Key = Key(51)
K_POINT:                Key = Key(52)
K_DIVIDE:               Key = Key(53)
K_RIGHT_SHIFT:          Key = Key(54)
K_MULTIPLY:             Key = Key(55)
K_PRINT_SCREEN:         Key = Key(55)
K_RIGHT_ALT:            Key = Key(56)
K_ALT:                  Key = Key(56)
K_SPACE:                Key = Key(57)
K_PAUSE:                Key = Key(69)
K_NUM_LOCK:             Key = Key(69)
K_SCROLL_LOCK:          Key = Key(70)
K_HOME:                 Key = Key(71)
K_UP:                   Key = Key(72)
K_PAGE_UP:              Key = Key(73)
K_MINUS:                Key = Key(74)
K_LEFT:                 Key = Key(75)
K_CLEAR:                Key = Key(76)
K_RIGHT:                Key = Key(77)
K_PLUS:                 Key = Key(78)
K_END:                  Key = Key(79)
K_DOWN:                 Key = Key(80)
K_PAGE_DOWN:            Key = Key(81)
K_INSERT:               Key = Key(82)
K_DELETE:               Key = Key(83)
K_LEFT_WINDOWS:         Key = Key(91)
K_RIGHT_WINDOWS:        Key = Key(92)
K_MENU:                 Key = Key(93)


# Key conditions

KEY_UNPRESSED: KeyCondition = KeyCondition(0)
KEY_DOWN:      KeyCondition = KeyCondition(1)
KEY_PRESSED:   KeyCondition = KeyCondition(2)
KEY_UP:        KeyCondition = KeyCondition(3)
