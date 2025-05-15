import pygame as pg


class Npc1(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load('спрайты/гг диалог 1/домсп/нпс стойка.png')
        self.rect = self.image.get_rect(center=(x, y))


class Npc2(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load('спрайты/гг диалог 1/домсп/стол.png')
        self.rect = self.image.get_rect(center=(x, y))