from __future__ import annotations
from my_library.transform import Transform


class Component:
    parent: ()
    transform: Transform
    components: list[Component, ...]

    def __init__(self, parent) -> None:
        self.parent = parent
        self.transform = parent.transform
        self.components = parent.components

    def __str__(self) -> str:
        return self.__class__.__name__

    def __repr__(self) -> str:
        return self.__class__.__name__

    def awake(self) -> None:
        pass

    def start(self) -> None:
        pass

    def update(self) -> None:
        pass

    def late_update(self) -> None:
        pass

    def fixed_update(self) -> None:
        pass

    def delete(self) -> None:
        pass
