from GameScene import GameScene

import pygame

from GameObject.PlayerGameObject import PlayerGameObject
from GameObject.ScoreGameObject import ScoreGameObject
from GameObject.PipePairGameObject import PipePairGameObject


class PauseScene(GameScene):
    def __init__(self):
        super(PauseScene, self).__init__()

    def draw(self, display: pygame.display) -> None:
        # fill the screen with a color to wipe away anything from last frame
        display.fill("grey")

        PlayerGameObject.instance.draw(display)
        ScoreGameObject.instance.draw(display)

        for key in PipePairGameObject.object_list:
            PipePairGameObject.object_list[key].draw(display)
