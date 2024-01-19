from levels.level0 import level_0_loop
from levels.level1 import level_1_loop
from levels.level2 import level_2_loop
from levels.level3 import level_3_loop


class Level:
    def __init__(self, level_loop: ()) -> None:
        self.start = level_loop


levels = (Level(level_0_loop), Level(level_1_loop), Level(level_2_loop), Level(level_3_loop))
current_level = 0
