from GameObject import GameObject
from GameObject.DigitGameObject import DigitGameObject
from GameObject.PositionMode import PositionMode
import GameState
import pygame


class ScoreGameObject(GameObject):
    instance = None

    def __init__(self):
        super(ScoreGameObject, self).__init__("score")
        ScoreGameObject.instance = self

        self.score = 0

        self.digits = []
        self.add_digit()

        self.set_position_mode(PositionMode.UP_CENTRE)
        self.move_to(GameState.screen_width / 2, 20)

        self.update_digits()

    def increase_score(self) -> None:
        self.score += 1
        self.update_digits()

    def add_digit(self):
        digit = DigitGameObject(f"digit_{len(self.digits)}")
        digit.scale(4, 4)
        self.digits.append(digit)
        self.resize_to_fit_digits()

    def update_digits(self) -> None:
        """
        updates the digits to correspond to the current score.
        :return:
        """
        current_score = self.score
        selector = 0

        while current_score >= 1:
            if selector >= len(self.digits):
                self.add_digit()
            digit = current_score % 10
            current_score = int(current_score / 10)
            self.digits[selector].set_digit(digit)
            selector = selector + 1

    def draw(self, display: pygame.display) -> None:
        for digit in self.digits:
            digit.draw(display)

    def resize_to_fit_digits(self):
        new_width = 0
        new_height = 0
        for digit in self.digits:
            new_height = max(new_height, digit.collision_box.height)
            new_width = new_width + digit.collision_box.width
        self.resize(new_width, new_height)

    def update_position(self) -> None:
        super().update_position()

        section = self.collision_box.width / len(self.digits)
        for index, digit in enumerate(self.digits):
            current_section = (section + 5) * (len(self.digits) - 1 - index)
            digit.move_to(self.collision_box.x + current_section, self.collision_box.y)
