import pygame


class GameObject:
    object_list = {}
    object_list_by_type = {}

    def __init__(self, object_type):
        GameObject.object_list[self.get_id()] = self

        self.type = object_type
        if self.type in GameObject.object_list_by_type:
            GameObject.object_list_by_type[self.type].append(self)
        else:
            GameObject.object_list_by_type[self.type] = [self]
        self.texture = None
        self.collision_box = pygame.Rect(10, 10, 10, 10)

    def update(self):
        pass

    def draw(self, display: pygame.display):
        pygame.draw.rect(display, "red", self.collision_box)

    def get_id(self) -> int:
        return hash(self)
