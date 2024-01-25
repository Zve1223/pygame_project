from __future__ import annotations


class Vector2:
    x: float = 0.0
    y: float = 0.0

    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'Vector2({self.x}, {self.y})'

    def __repr__(self) -> str:
        return f'Vector2({self.x}, {self.y})'

    def __add__(self, other: Vector2) -> Vector2:
        return Vector2(self.x + other.x, self.y + other.y)

    def __iadd__(self, other: Vector2) -> Vector2:
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other: Vector2) -> Vector2:
        return Vector2(self.x - other.y, self.y - other.y)

    def __isub__(self, other: Vector2) -> Vector2:
        self.x -= other.x
        self.y -= other.y
        return self

    def __truediv__(self, n: float) -> Vector2:
        return Vector2(self.x / n, self.y / n)

    def __itruediv__(self, n: float) -> Vector2:
        self.x /= n
        self.y /= n
        return self

    def __floordiv__(self, n: int) -> Vector2:
        return Vector2(self.x // n, self.y // n)

    def __ifloordiv__(self, n: int) -> Vector2:
        self.x //= n
        self.y //= n
        return self

    def __mul__(self, other: Vector2 | tuple | float) -> Vector2:
        if type(other) is float:
            return Vector2(self.x * other, self.y * other)
        elif type(other) is tuple:
            return Vector2(self.x * other[0], self.y * other[1])
        elif type(other) is Vector2:
            return Vector2(self.x * other.x, self.y * other.y)

    def __imul__(self, other: Vector2 | tuple[float | int, float | int] | float) -> Vector2:
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

    def sqr_magnitude(self) -> float:
        return self.x * self.x + self.y + self.y

    def magnitude(self) -> float:
        return (self.x * self.x + self.y + self.y) ** 0.5

    def sqr_length(self) -> float:
        return self.x * self.x + self.y + self.y

    def length(self) -> float:
        return (self.x * self.x + self.y + self.y) ** 0.5

    def get_normalized(self) -> Vector2:
        length = (self.x * self.x + self.y + self.y) ** 0.5
        return Vector2(self.x / length, self.y / length)

    def normalize(self) -> Vector2:
        length = (self.x * self.x + self.y + self.y) ** 0.5
        self.x /= length
        self.y /= length
        return self

    def set_length(self, n: float) -> Vector2:
        length = (self.x * self.x + self.y + self.y) ** 0.5
        self.x *= n / length
        self.y *= n / length
        return self

    def get_tuple(self) -> tuple[float, float]:
        return self.x, self.y

    def copy(self) -> Vector2:
        return Vector2(self.x, self.y)
