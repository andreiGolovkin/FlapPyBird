import pygame

from GameScene import GameScene
from GameObject.PlayerGameObject import PlayerGameObject
from GameObject.ScoreGameObject import ScoreGameObject


class StartingScene(GameScene):
    """
    Scene that is displayed in the beginning of the game.
    """
    def __init__(self):
        super(StartingScene, self).__init__()

    def draw(self, display: pygame.display):
        # fill the screen with a color to wipe away anything from last frame
        display.fill("grey")

        PlayerGameObject.instance.draw(display)
        ScoreGameObject.instance.draw(display)
