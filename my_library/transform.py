from __future__ import annotations

import my_library
from my_library.vector2 import Vector2
from my_library.constants import Space, LOCAL, GLOBAL


class Transform:
    position: Vector2 = Vector2()
    angle: float = 0.0
    scale: Vector2 = Vector2(1.0, 1.0)
    object: my_library.Object | None = None

    def __init__(self, position: Vector2 = Vector2(0.0, 0.0),
                 angle: float = 0.0,
                 scale: Vector2 = Vector2(1.0, 1.0)) -> None:
        self.position = position
        self.angle = angle
        self.scale = scale

    def __str__(self) -> str:
        return f'Transform({self.position}, {self.angle}, {self.scale})'

    def __repr__(self) -> str:
        return f'Transform({self.position}, {self.angle}, {self.scale})'

    def translate(self, x: float, y: float, space: Space = LOCAL) -> None:
        if space == LOCAL and self.object is not None:
            return
        else:
            self.position += Vector2(x, y)

    def rotate(self, angle: float) -> None:
        self.angle += angle

    def get_pos(self, space: Space = LOCAL) -> Vector2:
        if space == GLOBAL and self.object.parent is not None:
            return self.position + self.object.parent.transform.get_pos(GLOBAL)
        else:
            return self.position

    def get_scale(self, space: Space = LOCAL) -> Vector2:
        if space == GLOBAL and self.object.parent is not None:
            return self.scale * self.object.parent.transform.get_scale(GLOBAL)
        else:
            return self.scale

    def copy(self) -> Transform:
        return Transform(self.position, self.angle, self.scale)
