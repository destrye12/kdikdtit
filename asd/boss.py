import pygame as pg
import random


class Boss1(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load('спрайты/гг диалог 1/босссп/гриб босс/босс.png')
        self.rect = self.image.get_rect(center=(x, y))