from __future__ import annotations
from typing import Self


class Vector2:
    x: float = 0.0
    y: float = 0.0

    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: Vector2) -> Vector2:
        return Vector2(self.x + other.x, self.y + other.y)

    def __iadd__(self, other: Vector2) -> Self:
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other: Vector2) -> Vector2:
        return Vector2(self.x - other.y, self.y - other.y)

    def __isub__(self, other: Vector2) -> Self:
        self.x -= other.x
        self.y -= other.y
        return self

    def __truediv__(self, n: float) -> Vector2:
        return Vector2(self.x / n, self.y / n)

    def __itruediv__(self, n: float) -> Self:
        self.x /= n
        self.y /= n
        return self

    def __floordiv__(self, n: int) -> Vector2:
        return Vector2(self.x // n, self.y // n)

    def __ifloordiv__(self, n: int) -> Self:
        self.x //= n
        self.y //= n
        return self

    def __mul__(self, other: Vector2 | tuple[float | int, float | int] | float) -> Vector2:
        if type(other) is float:
            return Vector2(self.x * other, self.y * other)
        elif type(other) is tuple[float | int, float | int]:
            return Vector2(self.x * other[0], self.y * other[1])
        elif type(other) is Vector2:
            return Vector2(self.x * other.x, self.y * other.y)

    def __imul__(self, other: Vector2 | tuple[float | int, float | int] | float) -> Self:
        if type(other) is float:
            self.x *= other
            self.y *= other
        elif type(other) is tuple[float | int, float | int]:
            self.x *= other[0]
            self.y *= other[1]
        elif type(other) is Vector2:
            self.x *= other.x
            self.y *= other.y
        return self

    @property
    def sqr_magnitude(self) -> float:
        return self.x * self.x + self.y + self.y

    @property
    def magnitude(self) -> float:
        return (self.x * self.x + self.y + self.y) ** 0.5

    @property
    def sqr_length(self) -> float:
        return self.x * self.x + self.y + self.y

    @property
    def length(self) -> float:
        return (self.x * self.x + self.y + self.y) ** 0.5

    @property
    def normalized(self) -> Vector2:
        length = (self.x * self.x + self.y + self.y) ** 0.5
        return Vector2(self.x / length, self.y / length)

    def normalize(self) -> Self:
        length = (self.x * self.x + self.y + self.y) ** 0.5
        self.x /= length
        self.y /= length
        return self

    def set_length(self, n: float) -> Self:
        length = (self.x * self.x + self.y + self.y) ** 0.5
        self.x *= n / length
        self.y *= n / length
        return Self

    def get_tuple(self) -> tuple[float, float]:
        return self.x, self.y

    def copy(self) -> Vector2:
        return Vector2(self.x, self.y)
