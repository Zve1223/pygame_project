from my_library import Component, Input, GLOBAL


class BallController(Component):
    def update(self) -> None:
        if Input.get_key_down(Input.KeyCode.W):
            self.game_object.transform.translate(0, 1, GLOBAL)
            print(self.game_object.transform.position)
