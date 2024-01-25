import os
import pygame
from pygame import Color, Surface


def load_image(file_path: str, color_key: Color | int | None = None) -> Surface:
    if not os.path.isfile(file_path):
        print(f'Файл с изображением "{file_path}" не найден')
        exit()

    image = pygame.image.load(file_path)

    if color_key is not None:
        image = image.convert()
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()

    return image
