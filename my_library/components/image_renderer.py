from pygame import Surface, Rect
from my_library.component import Component
from .. import Vector2
from .. import Alignment
from .. import LEFT_TOP, GLOBAL
from .. import screen


class ImageRenderer(Component):
    image: Surface | None = None
    image_size: Vector2 | None = None
    alignment: Alignment = LEFT_TOP

    def set_image(self, image: Surface) -> None:
        self.image = image
        self.image_size = Vector2(*self.image.get_size())

    def set_alignment(self, alignment: Alignment) -> None:
        self.alignment = alignment

    def get_rect(self) -> Rect:
        size = self.image_size * self.transform.get_scale(GLOBAL)
        position = self.transform.get_pos(GLOBAL) + size * self.alignment
        return Rect(position.x, position.y, size.x, size.y)

    def update(self) -> None:
        if self.image is not None and self.image_size is not None:
            screen.blit(self.image, self.get_rect())
