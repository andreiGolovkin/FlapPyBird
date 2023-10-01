import pygame
from Geometry.Point import Point
from GameObject.PositionMode import PositionMode, update_position


class GameObject:
    object_list = {}
    object_list_by_name = {}

    def __init__(self, name):
        GameObject.object_list[self.get_id()] = self

        self.position = Point(0, 0)
        self.position_mode = PositionMode.UP_LEFT

        self.name = name
        if self.name in GameObject.object_list_by_name:
            raise NameError(f'Game Object with name \'{self.name}\' already registered')
        else:
            GameObject.object_list_by_name[self.name] = self

        self.texture = None
        self.collision_box = pygame.Rect(0, 0, 10, 10)

    def update(self):
        pass

    def update_position(self) -> None:
        current_point_pos = self.position.as_tuple()
        new_rect_pos_x, new_rect_pos_y = update_position[self.position_mode](self.collision_box, current_point_pos)
        self.collision_box.x = new_rect_pos_x
        self.collision_box.y = new_rect_pos_y

    def set_position_mode(self, new_mode: PositionMode) -> None:
        self.position_mode = new_mode
        self.update_position()

    def move_to(self, x: float, y: float) -> None:
        """
        Moves the object to the provided coordinates on the screen.

        :param x: (float) x coordinate of the new object position
        :param y: (float) y coordinate of the new object position
        :return: None
        """
        self.position.x = x
        self.position.y = y

        self.update_position()

    def move_by(self, x_offset: float, y_offset: float) -> None:
        """
        Moves the object by the provided offsets on the screen.

        :param x_offset: (float) x coordinate of the new object position
        :param y_offset: (float) y coordinate of the new object position
        :return: None
        """
        self.position.add(x_offset, y_offset)
        self.update_position()

    def move_by_vector(self, vector: Point):
        self.position.add_point(vector)
        self.update_position()

    def resize(self, width: int, height: int) -> None:
        """
        Resizes the game object's image on the screen.

        :param width: new width of the object
        :param height: new height of the object
        :return:
        """
        self.collision_box.width = width
        self.collision_box.height = height
        self.update_size()
        self.update_position()

    def scale(self, scale_x: float, scale_y: float) -> None:
        """
        Resizes the game object's image on the screen by the given multiplier.

        :param scale_x: multiplier of the object by width
        :param scale_y: multiplier of the object by height
        :return:
        """
        self.collision_box.width *= scale_x
        self.collision_box.height *= scale_y
        self.update_size()
        self.update_position()

    def update_size(self) -> None:
        """
        Updates the size of all texture to the size of the collision box.

        :return:
        """
        if isinstance(self.texture, pygame.Surface):
            self.texture = pygame.transform.scale(self.texture, (self.collision_box.width, self.collision_box.height))

    def draw(self, display: pygame.display) -> None:
        pass

    def draw_texture(self, display: pygame.display):
        display.blit(self.texture, self.collision_box)

    def draw_collision_box(self, display: pygame.display, color) -> None:
        pygame.draw.rect(display, color, self.collision_box)

    def get_id(self) -> int:
        return hash(self)
