import pygame
from constants import *
from my_utilities import Object, ObjectContainer, objects
from my_utilities import create_button


def level_0_loop() -> LevelId:
    def start() -> None:
        start_menu.hide()
        print('Start pressed')

    clock = pygame.time.Clock()

    background = Object('Background', './textures/Background.jpg')
    background.resize(max(WIN_SIZE), max(WIN_SIZE))
    background.set_alignment(MIDDLE_CENTER)
    background.move(WIN_SIZE[0] / 2, WIN_SIZE[1] / 2)

    start_button = create_button('Start_Button', MIDDLE_BOTTOM)
    start_button.move(0, -4)

    exit_button = create_button('Exit_Button', MIDDLE_TOP)
    exit_button.set_function(LEFT_BUTTON, exit)
    exit_button.move(0, 4)

    start_menu = ObjectContainer(MIDDLE_CENTER)
    start_menu.add_objects([start_button, exit_button])

    level_menu = ObjectContainer(MIDDLE_CENTER)

    for n in range(3):
        level_button = create_button('Level_Button', MIDDLE_BOTTOM)
        level_button.set_name(f'Level_{n}')
        level_button.set_function(LEFT_BUTTON, start)
        level_button.move(0, 72 - n * 72)
        level_menu.add_object(level_button)

    objects.start_objects()

    while True:
        clock.tick(MAX_FPS)
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    exit()
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_ESCAPE:
                            return LEVEL_0
                case pygame.MOUSEMOTION:
                    objects.check_mouse_move(mouse_pos)
                case pygame.MOUSEBUTTONDOWN:
                    objects.check_mouse_down(event.button)
                case pygame.MOUSEBUTTONUP:
                    objects.check_mouse_up(event.button)

        objects.update_objects()

        objects.draw_objects()

        pygame.display.flip()
