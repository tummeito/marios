import pygame as pg
from tiles import Tile
from pygame.sprite import Group


class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.level_data = level_data

    def draw(self): pass
