import pygame
from .time import *
from .types import LevelId
from .constants import MAX_FPS, LEVEL_0
from my_library.levels import hierarchy


class Level:
    name: str

    def __init__(self, name: str, declare_variables: ()) -> None:
        self.name = name
        self.__declare_variables = declare_variables

    def __declare_variables(self) -> None:
        pass

    def launch(self) -> LevelId:
        self.__declare_variables()
        hierarchy.start()
        while True:
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:
                        hierarchy.clear()
                        pygame.quit()
                        exit()
                    case pygame.KEYDOWN:
                        match event.key:
                            case pygame.K_ESCAPE:
                                return LEVEL_0
            self.__loop()

    def __loop(self) -> None:
        pygame.time.Clock().tick(MAX_FPS)
        start_time = now()
        hierarchy.fixed_update()
        hierarchy.update()
        hierarchy.late_update()
        pygame.display.flip()
        Time.delta_time = now() - start_time
        Time.fixed_update_timer += Time.delta_time


