from __future__ import annotations

from my_library.time import Time
from my_library.object import Object


class Hierarchy:
    name: str
    objects: list[Object, ...]

    def __init__(self, name: str) -> None:
        self.name = name
        self.objects = []

    def __str__(self) -> str:
        objects = "\n\t".join(map(str, self.objects))
        return f'{self.name}(\n\t{objects}\n)'

    def __repr__(self) -> str:
        objects = "\n\t".join(map(str, self.objects))
        return f'{self.name}(\n\t{objects}\n)'

    def add_object(self, object: Object) -> Hierarchy:
        self.objects.append(object)
        return self

    def delete_object(self, required: Object) -> None:
        for object in self.objects:
            if object is required:
                object.delete()
                return
        for object in self.objects:
            found = object.find(required)
            if found is not None:
                found.delete()
                return

    def clear(self) -> None:
        for object in self.objects:
            object.delete()

    def start(self) -> None:
        for object in self.objects:
            object.start()

    def update(self) -> None:
        for object in self.objects:
            object.update()

    def late_update(self) -> None:
        for object in self.objects:
            object.late_update()

    def fixed_update(self) -> None:
        for _ in range(int(Time.fixed_update_timer / Time.fixed_delta_time)):
            for object in self.objects:
                object.fixed_update()
        Time.fixed_update_timer %= Time.fixed_delta_time
