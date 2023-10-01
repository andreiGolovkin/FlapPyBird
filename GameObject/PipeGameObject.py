from GameObject import GameObject
import pygame


class PipeGameObject(GameObject):
    object_list = {}
    object_list_by_name = {}

    def __init__(self, name):
        super(PipeGameObject, self).__init__(name)
        PipeGameObject.object_list[self.get_id()] = self

        if self.name in PipeGameObject.object_list_by_name:
            raise NameError(f'Game Object with name \'{self.name}\' already registered')
        else:
            PipeGameObject.object_list_by_name[self.name] = self

        self.collision_box.x = 20
        self.collision_box.y = 20
        self.collision_box.width = 20
        self.collision_box.height = 40

    def draw(self, display: pygame.display):
        pygame.draw.rect(display, "red", self.collision_box)
