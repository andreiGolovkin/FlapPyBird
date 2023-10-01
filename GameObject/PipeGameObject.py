from GameObject import GameObject
import pygame
import GameState


class PipeGameObject(GameObject):
    object_list = {}
    object_list_by_name = {}

    def __init__(self):
        super(PipeGameObject, self).__init__(f"pipe_{len(self.object_list.keys())+1}")
        PipeGameObject.object_list[self.get_id()] = self

        if self.name in PipeGameObject.object_list_by_name:
            raise NameError(f'Game Object with name \'{f"pipe_{len(self.object_list.keys())+1}"}\' already registered')
        else:
            PipeGameObject.object_list_by_name[f"pipe_{len(self.object_list.keys())+1}"] = self

        self.collision_box.x = 20
        self.collision_box.y = 20
        self.collision_box.width = 20
        self.collision_box.height = GameState.screen_height

    def draw(self, display: pygame.display):
        pygame.draw.rect(display, "red", self.collision_box)

    @classmethod
    def draw_all(cls, display: pygame.display):
        for pipe_id in cls.object_list:
            cls.object_list[pipe_id].draw(display)
