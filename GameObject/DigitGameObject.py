from GameObject import GameObject
from GameState import GameState
import pygame


class DigitGameObject(GameObject):
    def __init__(self, name: str):
        super(DigitGameObject, self).__init__(name)
        self.set_digit(0)

    def draw(self, display: pygame.display) -> None:
        self.draw_texture(display)

    def set_digit(self, digit: int) -> None:
        self.texture = GameState.texture_sheet[f"digits_{digit}"]
        self.update_size()
