import pygame as pg
from pygame.sprite import Sprite

class Player(Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pg.Surface((32, 64))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)