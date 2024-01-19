from pygame import Surface, Rect
from my_library import screen
from object import Object
from component import Component
from vector2 import Vector2
from constants import Alignment, LEFT_TOP, GLOBAL


class ImageRenderer(Component):
    image: Surface | None
    image_size: Vector2 | None
    alignment: Alignment

    def __init__(self, parent: Object, image: Surface | None = None, alignment: Alignment = LEFT_TOP) -> None:
        super(ImageRenderer, self).__init__(parent)
        self.image = image
        if self.image is not None:
            self.image_size = Vector2(*self.image.get_size())
        else:
            self.image_size = None
        self.alignment: Alignment = alignment

    def set_image(self, image: Surface) -> None:
        self.image = image
        self.image_size = Vector2(*image.get_size())

    def set_alignment(self, alignment: Alignment) -> None:
        self.alignment = alignment

    @property
    def rect(self) -> Rect:
        size = self.image_size * self.transform.get_scale(GLOBAL)
        position = self.transform.get_pos(GLOBAL) + size * self.alignment
        return Rect(position.x, position.y, size.x, size.y)

    def update(self) -> None:
        screen.blit(self.image, self.rect)
