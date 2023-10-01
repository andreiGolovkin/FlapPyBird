from GameObject import GameObject
from GameObject.PipeGameObject import PipeGameObject
import GameState
import pygame

from GameObject.PositionMode import PositionMode


class PipePairGameObject(GameObject):
    object_list = {}
    object_list_by_name = {}

    def __init__(self) -> None:
        super(PipePairGameObject, self).__init__(f"pipe_pair_{len(self.object_list.keys())+1}")
        PipePairGameObject.object_list[self.get_id()] = self

        if self.name in PipePairGameObject.object_list_by_name:
            raise NameError(
                f'Game Object with name \'{f"{self.name}"}\' already registered')
        else:
            PipePairGameObject.object_list_by_name[self.name] = self

        self.upper_pipe = PipeGameObject()
        self.lower_pipe = PipeGameObject()

        self.upper_pipe.set_position_mode(PositionMode.DOWN_CENTRE)
        self.lower_pipe.set_position_mode(PositionMode.UP_CENTRE)

        self.space_gap = 100
        self.move_to(GameState.screen_width / 2, GameState.screen_height / 2)

    def update_position(self) -> None:
        super().update_position()

        self.lower_pipe.move_to(self.position.x, self.position.y + self.space_gap/2)
        self.upper_pipe.move_to(self.position.x, self.position.y - self.space_gap/2)

    def update(self) -> None:
        self.lower_pipe.update()

    def draw(self, display: pygame.display) -> None:
        self.upper_pipe.draw(display)
        self.lower_pipe.draw(display)
