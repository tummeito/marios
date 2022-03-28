import pygame as pg
from pygame.sprite import Sprite, Group

class Tile(Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pg.Surface((size, size))
        self.image.fill((255, 0 ,0))
        self.rect = self.image.get_rect(topleft = pos)

    def draw(self): pass