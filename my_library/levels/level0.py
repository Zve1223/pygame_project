from my_library import *
from my_library.scripts import *


def declare_variables() -> None:
    ball = GameObject('Ball')
    ball.add_component(ImageRenderer)
    renderer = ball.get_component(ImageRenderer)
    renderer.set_image(load_image('./textures/ball.png'))
    ball.add_component(BallController)
    # self.background.resize(max(WIN_SIZE), max(WIN_SIZE))
    # self.background.set_alignment(MIDDLE_CENTER)
    # self.background.move(WIN_SIZE[0] / 2, WIN_SIZE[1] / 2)

    # self.start_button = create_button('Start_Button', MIDDLE_BOTTOM)
    # self.start_button.move(0, -4)

    # self.exit_button = create_button('Exit_Button', MIDDLE_TOP)
    # self.exit_button.set_function(LEFT_BUTTON, exit)
    # self.exit_button.move(0, 4)

    # self.start_menu = ObjectContainer(MIDDLE_CENTER)
    # self.start_menu.add_objects([self.start_button, self.exit_button])

    # self.level_menu = ObjectContainer(MIDDLE_CENTER)

    # for n in range(3):
    #     level_button = create_button('Level_Button', MIDDLE_BOTTOM)
    #     level_button.set_name(f'Level_{n}')
    #     level_button.set_function(LEFT_BUTTON, start)
    #     level_button.move(0, 72 - n * 72)
    #     self.level_menu.add_object(level_button)
