import pygame
from GameState import GameState

from GameObject.ScoreGameObject import ScoreGameObject


def stop_game(event: pygame.event.Event):
    GameState.running = False


def register_mouse_press(event: pygame.event.Event):
    GameState.mouse_pressed = True

    if event.button == 1: # left click
        GameState.left_mouse_clicked = True
    elif event.button == 3: # right click
        GameState.right_mouse_clicked = True


def register_mouse_release(event: pygame.event.Event):
    GameState.mouse_pressed = False


def increase_score(event: pygame.event.Event):
    ScoreGameObject.instance.increase_score()


events_register = {
    pygame.QUIT: stop_game,

    # inputs
    pygame.MOUSEBUTTONDOWN: register_mouse_press,  # mouse press
    pygame.MOUSEBUTTONUP: register_mouse_release,  # mouse release

    pygame.KEYDOWN: increase_score
}
