"""
This module holds the data that is shared across the whole application
"""

running: bool = True
mouse_pressed: bool = False
left_mouse_clicked: bool = False
right_mouse_clicked: bool = False

screen_width: int = 1280
screen_height: int = 720

screen_size: tuple = (screen_width, screen_height)

texture_sheet: dict = {}
