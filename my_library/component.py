from __future__ import annotations

from .game_object import GameObject


class Component:
    game_object: GameObject
    transform: GameObject.transform
    components: list[Component, ...]

    def __init__(self, game_object: GameObject) -> None:
        self.game_object = game_object
        self.components = game_object.components

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
