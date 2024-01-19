from __future__ import annotations
from object import Object
from transform import Transform


class Component:
    parent: Object
    transform: Transform
    components: list[Component, ...]

    def __init__(self, parent: Object) -> None:
        self.parent = parent
        self.transform = parent.transform
        self.components = parent.components

    def awake(self) -> None:
        pass

    def start(self) -> None:
        pass

    def update(self) -> None:
        pass

    def fixed_update(self) -> None:
        pass
