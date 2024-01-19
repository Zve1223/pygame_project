import pygame
from time import time
from my_library.time import Time
from my_library.hierarchy import Hierarchy
from my_library.constants import MAX_FPS


class Level:
    name: str
    hierarchy: Hierarchy

    def __init__(self, name: str, declare_variables: ()) -> None:
        self.name = name
        self.hierarchy = Hierarchy(name)
        self.__declare_variables = declare_variables

    def __declare_variables(self) -> None:
        pass

    def launch(self) -> None:
        self.__declare_variables()
        self.hierarchy.start()
        while True:
            self.__loop()

    def __loop(self) -> None:
        print(self.hierarchy)
        pygame.time.Clock().tick(MAX_FPS)
        start_time = time()
        self.hierarchy.fixed_update()
        self.hierarchy.update()
        self.hierarchy.late_update()
        pygame.display.flip()
        Time.delta_time = time() - start_time
        Time.fixed_update_timer += Time.delta_time


