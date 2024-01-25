from __future__ import annotations

from ..types import Space
from ..vector2 import Vector2
from ..constants import LOCAL, GLOBAL
from ..component import Component


class Transform(Component):
    position: Vector2 = Vector2(0.0, 0.0)
    angle: float = 0.0
    scale: Vector2 = Vector2(1.0, 1.0)

    def __str__(self) -> str:
        return f'Transform({self.position}, {self.angle}, {self.scale})'

    def __repr__(self) -> str:
        return f'Transform({self.position}, {self.angle}, {self.scale})'

    def translate(self, x: float, y: float, space: Space = LOCAL) -> None:
        if space == LOCAL and self.game_object is not None:
            return
        else:
            self.position += Vector2(x, y)

    def rotate(self, angle: float) -> None:
        self.angle += angle

    def get_pos(self, space: Space = LOCAL) -> Vector2:
        if space == GLOBAL and type(self.game_object.parent) is not Hierarchy:
            return self.position + self.game_object.parent.transform.get_pos(GLOBAL)
        else:
            return self.position

    def get_scale(self, space: Space = LOCAL) -> Vector2:
        if space == GLOBAL and type(self.game_object.parent) is not Hierarchy:
            return self.scale * self.game_object.parent.transform.get_scale(GLOBAL)
        else:
            return self.scale
