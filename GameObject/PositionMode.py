from enum import Enum, auto
import pygame


class PositionMode(Enum):
    UP_LEFT = auto()
    UP_RIGHT = auto()
    UP_CENTRE = auto()
    CENTRE_LEFT = auto()
    CENTRE_RIGHT = auto()
    CENTRE = auto()
    DOWN_LEFT = auto()
    DOWN_RIGHT = auto()
    DOWN_CENTRE = auto()


def up_left(rect: pygame.Rect, new_pos: tuple) -> tuple:
    return new_pos


def up_right(rect: pygame.Rect, new_pos: tuple) -> tuple:
    pos_x, pos_y = new_pos
    pos_x = pos_x - rect.width
    return pos_x, pos_y


def up_centre(rect: pygame.Rect, new_pos: tuple) -> tuple:
    pos_x, pos_y = new_pos
    pos_x = pos_x - (rect.width / 2)
    return pos_x, pos_y


def centre_left(rect: pygame.Rect, new_pos: tuple) -> tuple:
    pos_x, pos_y = new_pos
    pos_y = pos_y - (rect.height / 2)
    return pos_x, pos_y


def centre_right(rect: pygame.Rect, new_pos: tuple) -> tuple:
    pos_x, pos_y = new_pos
    pos_y = pos_y - (rect.height / 2)
    pos_x = pos_x - rect.width
    return pos_x, pos_y


def centre(rect: pygame.Rect, new_pos: tuple) -> tuple:
    pos_x, pos_y = new_pos
    pos_y = pos_y - (rect.height / 2)
    pos_x = pos_x - (rect.width / 2)
    return pos_x, pos_y


def down_left(rect: pygame.Rect, new_pos: tuple) -> tuple:
    pos_x, pos_y = new_pos
    pos_y = pos_y - rect.height
    return pos_x, pos_y


def down_right(rect: pygame.Rect, new_pos: tuple) -> tuple:
    pos_x, pos_y = new_pos
    pos_y = pos_y - rect.height
    pos_x = pos_x - rect.width
    return pos_x, pos_y


def down_centre(rect: pygame.Rect, new_pos: tuple) -> tuple:
    pos_x, pos_y = new_pos
    pos_y = pos_y - rect.height
    pos_x = pos_x - (rect.width / 2)
    return pos_x, pos_y


update_position = {
    PositionMode.UP_LEFT: up_left,
    PositionMode.UP_RIGHT: up_right,
    PositionMode.UP_CENTRE: up_centre,
    PositionMode.CENTRE_LEFT: centre_left,
    PositionMode.CENTRE_RIGHT: centre_right,
    PositionMode.CENTRE: centre,
    PositionMode.DOWN_LEFT: down_left,
    PositionMode.DOWN_RIGHT: down_right,
    PositionMode.DOWN_CENTRE: down_centre
}
