import pygame
from TextureHandler.TextureTable import metadata
import GameState


class TextureHandler:
    """
    This module is responsible for preparing the textures for the further use.
    """

    @classmethod
    def prepare_textures(cls):
        images = TextureHandler.load()
        TextureHandler.crop(images)

    @classmethod
    def load(cls) -> dict:
        images = {}
        for texture_name in metadata.keys():
            images[texture_name] = pygame.image.load(metadata[texture_name]["file"])

        return images

    @classmethod
    def crop(cls, images):
        for image_name in images.keys():
            if "crop" in metadata[image_name].keys():
                for crop_name in metadata[image_name]["crop"].keys():
                    crop_data = metadata[image_name]["crop"][crop_name]
                    crop = images[image_name].subsurface(crop_data)
                    GameState.texture_sheet[f"{image_name}_{crop_name}"] = crop
            else:
                GameState.texture_sheet[f"{image_name}"] = images[image_name]
