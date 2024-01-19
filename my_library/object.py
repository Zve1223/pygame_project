from __future__ import annotations
from component import Component
from transform import Transform


class Object:
    name: str = 'GameObject'
    transform: Transform = Transform()
    components: list[Component] = []
    parent: Object | None = None
    children: list[Object] = []

    def __init__(self, name: str = 'GameObject') -> None:
        self.name: str = name

        self.awake()

    def awake(self) -> None:
        for component in self.components:
            component.awake()
        for child in self.children:
            child.awake()

    def start(self) -> None:
        for component in self.components:
            component.start()
        for child in self.children:
            child.start()

    def update(self) -> None:
        for component in self.components:
            component.update()
        for child in self.children:
            child.update()

    def fixed_update(self) -> None:
        for component in self.components:
            component.fixed_update()
        for child in self.children:
            child.fixed_update()
