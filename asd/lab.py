import pygame as pg


class Lab(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load(f'спрайты/гг диалог 1/лабсп/стена6.png')
        self.rect = self.image.get_rect(center=(x, y))
