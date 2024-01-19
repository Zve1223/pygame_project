from my_library import FDT
from object import Object


class Hierarchy:
    def __init__(self) -> None:
        self.fixed_update_timer = 0.0
        self.objects: list[Object, ...] = []

    def start(self) -> None:
        for object in self.objects:
            object.start()

    def update(self) -> None:
        for object in self.objects:
            object.update()

    def fixed_update(self) -> None:
        for _ in range(self.fixed_update_timer // FDT):
            for object in self.objects:
                object.fixed_update()
        self.fixed_update_timer %= FDT
