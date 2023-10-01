from GameObject import GameObject
import GameState
from Geometry.Point import Point
import pygame
import math

from GameObject.PositionMode import PositionMode


class PlayerGameObject(GameObject):
    instance: GameObject = None

    def __init__(self):
        super(PlayerGameObject, self).__init__("player")
        PlayerGameObject.instance = self

        self.speed_vector: Point = Point(0, 0)
        self.acceleration_vector: Point = Point(0, 0.5)

        self.texture: pygame.Surface = GameState.texture_sheet["bird"]

        self.set_position_mode(PositionMode.CENTRE)

        self.resize(70, 40)
        self.move_to(80, GameState.screen_height / 2)

    def draw(self, display: pygame.display):
        pygame.draw.rect(display, "white", self.collision_box)

        self.draw_texture(display)

    def draw_texture(self, display: pygame.display):
        angle_factor = (min(max(self.speed_vector.y, -10), 10) + 10) / 20
        angle = -((60 * angle_factor) - 30)
        rotated_image = pygame.transform.rotate(self.texture, angle)
        rect = rotated_image.get_rect()
        rect.center = self.collision_box.center
        display.blit(rotated_image, rect)

    def update(self):
        if GameState.left_mouse_clicked:
            self.jump()

        self.speed_vector.add_point(self.acceleration_vector)
        self.move_by_vector(self.speed_vector)

    def jump(self):
        self.speed_vector.y = -10

    def move_by_vector(self, vector: Point):
        self.position.add_point(vector)
        if self.collision_box.height / 2 >= self.position.y:
            self.position.y = self.collision_box.height / 2
            self.speed_vector.y = 0
        self.update_position()
