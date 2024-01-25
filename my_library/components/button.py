from my_library import Component
from my_library.components import Sprite


class Button(Component):
    sprite: Sprite
    is_pointed: bool

    def start(self) -> None:
        self.sprite = self.object.get_component(Sprite)
        if self.sprite is None:
            print(f'The object {self.object.name} do not have a Sprite.')
            self.sprite = self.object.add_component(Sprite)
            print(f'Sprite has been added successfully.')
