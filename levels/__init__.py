from my_library.level import Level
import levels.level0
import levels.level1
import levels.level2
import levels.level3


levels: tuple[Level, ...] = (
    Level('Menu', levels.level0.declare_variables),
)

current_level = levels[0]
