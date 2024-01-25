from pygame import Surface
from ..component import Component
from ..components import ImageRenderer


class Sprite(Component):
    image_renderer: ImageRenderer
    frames: list[Surface, ...]
    current_frame: int

    def start(self) -> None:
        self.image_renderer = self.game_object.get_component(ImageRenderer)
        if self.image_renderer is None:
            print(f'The object {self.game_object.name} do not have a ImageRenderer.')
            self.image_renderer = self.game_object.add_component(ImageRenderer)
            print(f'ImageRenderer has been added successfully.')

        self.current_frame = 0

    def add_frame(self, frame: Surface) -> None:
        self.frames.append(frame)

    def remove_frame(self, frame_number: int) -> None:
        self.frames.pop(frame_number)
        if self.current_frame == frame_number:
            self.current_frame = 0

    def set_frame(self, frame_number: int) -> None:
        self.current_frame = frame_number
        self.image_renderer.set_image(self.frames[self.current_frame])
