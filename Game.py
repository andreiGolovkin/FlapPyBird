import pygame

import GameScene
from TextureHandler import TextureHandler
from GameState import GameState
from GameObject import GameObject
from GameObject.PlayerGameObject import PlayerGameObject
from GameObject.ScoreGameObject import ScoreGameObject
from Events import events_register
from GameScene.SceneSelector import SceneSelector


class Game:
    """
    This module is responsible for the controlling of the basic logic of the game flow.
    """

    def __init__(self):
        self.screen = None
        self.clock = None

        self.scene_selector = SceneSelector()

        TextureHandler.prepare_textures()

    def run(self) -> None:
        """
        This method is controlling the basic game lifecycle.
        :return:
        None
        """
        self.init()

        while GameState.running:
            self.handle_events()
            self.scene_selector.update()

            scene = self.scene_selector.current_scene

            scene.update()

            scene.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)

        self.destroy()

    def init(self):
        pygame.init()

        self.screen = pygame.display.set_mode(GameState.screen_size)
        self.clock = pygame.time.Clock()

        PlayerGameObject()
        ScoreGameObject()

    def update(self):
        # fill the screen with a color to wipe away anything from last frame
        self.screen.fill("grey")

        self.draw()

        # flip() the display to put your work on screen
        pygame.display.flip()

        self.clock.tick(60)  # limits FPS to 60

    def destroy(self):
        pygame.quit()

    def handle_events(self):
        GameState.left_mouse_clicked = False
        GameState.right_mouse_clicked = False
        for event in pygame.event.get():
            if event.type in events_register:
                events_register[event.type](event)

    def draw(self):
        for key in GameObject.object_list:
            GameObject.object_list[key].update()
