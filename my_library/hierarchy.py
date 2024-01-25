from __future__ import annotations

from .time import *
from .game_object import GameObject


class Hierarchy:
    name: str
    game_objects: list[GameObject, ...]

    def __init__(self) -> None:
        self.name = 'Hierarchy'
        self.game_objects = []

    def __str__(self) -> str:
        objects = "\n\t".join(map(str, self.game_objects))
        return f'{self.name}(\n\t{objects}\n)'

    def __repr__(self) -> str:
        objects = "\n\t".join(map(str, self.game_objects))
        return f'{self.name}(\n\t{objects}\n)'

    def add_object(self, object: GameObject) -> Hierarchy:
        self.game_objects.append(object)
        return self

    def find_object(self, name: str) -> GameObject | None:
        for game_object in self.game_objects:
            if game_object.name == name:
                return game_object
        for game_object in self.game_objects:
            found = game_object.find(name)
            if found is not None:
                return found
        return None

    def delete_object(self, name: str) -> None:
        for game_object in self.game_objects:
            if game_object.name == name:
                game_object.delete()
                return
        for game_object in self.game_objects:
            found = game_object.find(name)
            if found is not None:
                found.delete()
                return

    def clear(self) -> None:
        for game_object in self.game_objects:
            game_object.delete()

    def start(self) -> None:
        for game_object in self.game_objects:
            game_object.start()

    def update(self) -> None:
        for game_object in self.game_objects:
            game_object.update()

    def late_update(self) -> None:
        for game_object in self.game_objects:
            game_object.late_update()

    def fixed_update(self) -> None:
        for _ in range(int(Time.fixed_update_timer / Time.fixed_delta_time)):
            for game_object in self.game_objects:
                game_object.fixed_update()
        Time.fixed_update_timer %= Time.fixed_delta_time
