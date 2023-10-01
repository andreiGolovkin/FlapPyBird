from GameScene.StartingScene import StartingScene
from GameScene.GamingScene import GamingScene
from GameScene.PauseScene import PauseScene
import GameState


class SceneSelector:
    def __init__(self):
        self.current_scene = StartingScene()

    def update(self):
        if isinstance(self.current_scene, StartingScene):
            if GameState.left_mouse_clicked:
                self.current_scene = GamingScene()
        elif isinstance(self.current_scene, GamingScene):
            if GameState.right_mouse_clicked:
                self.current_scene = PauseScene()
        elif isinstance(self.current_scene, PauseScene):
            if GameState.right_mouse_clicked:
                self.current_scene = GamingScene()
