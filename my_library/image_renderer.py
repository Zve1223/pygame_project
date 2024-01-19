from pygame import Surface, Rect
import my_library
from my_library.object import Object
from my_library.component import Component
from my_library.vector2 import Vector2
from my_library.constants import Alignment, LEFT_TOP, GLOBAL


class ImageRenderer(Component):
    image: Surface | None
    image_size: Vector2 | None
    alignment: Alignment

    def __init__(self, parent: Object) -> None:
        super(ImageRenderer, self).__init__(parent)
        self.image = None
        self.image_size = None
        self.alignment: Alignment = LEFT_TOP

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
        if self.image is not None and self.image_size is not None:
            my_library.screen.blit(self.image, self.rect)
