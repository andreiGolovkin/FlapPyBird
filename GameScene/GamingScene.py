import pygame

from GameScene import GameScene
from GameObject.PlayerGameObject import PlayerGameObject
from GameObject.ScoreGameObject import ScoreGameObject


class GamingScene(GameScene):
    def __init__(self):
        super(GamingScene, self).__init__()

    def draw(self, display: pygame.display):
        # fill the screen with a color to wipe away anything from last frame
        display.fill("grey")

        PlayerGameObject.instance.draw(display)
        ScoreGameObject.instance.draw(display)

    def update(self):
        PlayerGameObject.instance.update()
        ScoreGameObject.instance.update()
