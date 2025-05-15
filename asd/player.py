import pygame as pg


player_img_W = [pg.image.load(f'спрайты/гг диалог 1/ггсп/гг сзади/спина{i}.png') for i in range(0, 7)]
player_img_A = [pg.image.load(f'спрайты/гг диалог 1/ггсп/гг налево/гг налево{i}.png') for i in range(0, 7)]
player_img_S = [pg.image.load(f'спрайты/гг диалог 1/ггсп/гг вперед/ггх{i}.png') for i in range(0, 6)]
player_img_D = [pg.image.load(f'спрайты/гг диалог 1/ггсп/гг направо/гг{i}.png') for i in range(0, 7)]

class Player(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load('спрайты/гг диалог 1/ггсп/гг направо/гг0.png')
        self.rect = self.image.get_rect(center=(x, y))
        self.vector = 0
        self.jump_time = None

    def move_W(self):
        self.vector = -6.5
        self.jump_time = pg.time.get_ticks()
        frame_duration = 150  # Задержка между кадрами в миллисекундах
        current_time = pg.time.get_ticks()
        frame_index = (current_time // frame_duration) % len(player_img_W)
        self.image = player_img_W[frame_index]

    def move_A(self):
        self.vector = -6.5
        self.jump_time = pg.time.get_ticks()
        frame_duration = 150  # Задержка между кадрами в миллисекундах
        current_time = pg.time.get_ticks()
        frame_index = (current_time // frame_duration) % len(player_img_A)
        self.image = player_img_A[frame_index]


    def move_S(self):
        self.vector = -6
        self.jump_time = pg.time.get_ticks()
        frame_duration = 150  # Задержка между кадрами в миллисекундах
        current_time = pg.time.get_ticks()
        frame_index = (current_time // frame_duration) % len(player_img_S)
        self.image = player_img_S[frame_index]


    def move_D(self):
        self.vector = -6
        self.jump_time = pg.time.get_ticks()
        frame_duration = 150  # Задержка между кадрами в миллисекундах
        current_time = pg.time.get_ticks()
        frame_index = (current_time // frame_duration) % len(player_img_D)
        self.image = player_img_D[frame_index]

    def update(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_w] or keys[pg.KSCAN_W] or keys[pg.K_UP]:
            self.move_W()
            self.rect.y += self.vector

        if keys[pg.K_a] or keys[pg.KSCAN_A] or keys[pg.K_LEFT]:
            self.move_A()
            self.rect.x += self.vector

        if keys[pg.K_s] or keys[pg.KSCAN_S] or keys[pg.K_DOWN]:
            self.move_S()
            self.rect.y -= self.vector

        if keys[pg.K_d] or keys[pg.KSCAN_D] or keys[pg.K_RIGHT]:
            self.move_D()
            self.rect.x -= self.vector

        '''if keys[pg.K_SPACE]:
            self.mush_put()

'''
class APlayer(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load('спрайты/гг диалог 1/ггсп/гг на арене.png')
        self.rect = self.image.get_rect(center=(x, y))
        self.vector = 0
        self.jump_time = None

    def update(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_w] or keys[pg.KSCAN_W] or keys[pg.K_UP]:
            self.vector = -6
            self.rect.y += self.vector

        if keys[pg.K_a] or keys[pg.KSCAN_A] or keys[pg.K_LEFT]:
            self.vector = -6
            self.rect.x += self.vector

        if keys[pg.K_s] or keys[pg.KSCAN_S] or keys[pg.K_DOWN]:
            self.vector = -6
            self.rect.y -= self.vector

        if keys[pg.K_d] or keys[pg.KSCAN_D] or keys[pg.K_RIGHT]:
            self.vector = -6
            self.rect.x -= self.vector