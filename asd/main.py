import pygame as pg
from boss import Boss1
from asd.player import APlayer
from player import Player
from npc import Npc1, Npc2
from lab import Lab

pg.init()
pg.font.init()
pg.mixer.init()


W = 1500
H = 800
room = 0
font = pg.font.Font('спрайты/шрифт.ttf', 32)
keys = pg.key.get_pressed()
pil = pg.image.load
pss = pg.surface.Surface
sound_door = pg.mixer.Sound('спрайты/гг диалог 1/домсп/открытие двери.mp3')
labf_img = pil('спрайты/гг диалог 1/лабсп/фон лабиринта.png')
labf = pss((1500, 800))
tropa_img = pil('спрайты/гг диалог 1/босссп/тропа.png')
tropa = pss((1500, 800))
home_img = pil('спрайты/гг диалог 1/домсп/дом.png')
home = pss((1500, 800))
clock = pg.time.Clock()
bg_img = pil('спрайты/гг диалог 1/фон.png')
bg = pss((1500, 800))
homi_img = pil('спрайты/гг диалог 1/домсп/дом внутри.png')
home_inside = pss((1500, 800))
arena_img = pil('спрайты/гг диалог 1/босссп/арена.png')
arena = pss((1500, 800))
grt_img = pil('спрайты/гг диалог 1/босссп/гриб босс/гриб.png')
grt = pss((1500, 800))
player = Player(1470, 650)
aplayer = APlayer(0, 0)
boss1 = Boss1(565, 220)
npc1 = Npc1(950, 620)
npc2 = Npc2(300, 650)
lab = Lab(750, 400)
all_sprite = pg.sprite.Group(player)
screen = pg.display.set_mode((W, H))

def upd():
    if (player.rect.bottom > 815):
        player.rect.bottom = 815
    if player.rect.top < 0:
        player.rect.top = 0
    if player.rect.left < -15:
        player.rect.left = -15
    if player.rect.right > 1535:
        player.rect.right = 1535
    if 3.1 <= room < 4:
        if aplayer.rect.left < 589:
            aplayer.rect.left = 589
        if aplayer.rect.right > 790:
            aplayer.rect.right = 790
        if aplayer.rect.top < 450:
            aplayer.rect.top = 450
        if aplayer.rect.bottom > 610:
            aplayer.rect.bottom = 610
        tropa.blit(tropa_img, (0, 0))
        screen.blit(tropa, (0, 0))
    clock.tick(60)
    all_sprite.draw(screen)
    all_sprite.update()
    pg.display.update()


run = True

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False


    if room == 0:

        all_sprite = pg.sprite.Group(player)
        bg.blit(bg_img, (0, 0))
        screen.blit(bg, (0, 0))
        home.blit(home_img, (110, -120))
        screen.blit(home_img, (110, -120))
        if player.rect.top < 400:
            player.rect.top = 400

        if player.rect.right >= 1530:
            room = 3
            player.rect.x = 637 #корды на 3 комнату
            player.rect.y = 740

        if 440 < player.rect.x < 800 and player.rect.y <= 548:
            player.rect.y = 548
        if 620 < player.rect.x < 785 and 610 > player.rect.y > 600:
            player.rect.y = 600

        if 600 <= player.rect.x <= 650 and 480 <= player.rect.y <= 550:
            room = 1
            player.rect.x = 965
            player.rect.y = 610
            sound_door.play()


    if room == 1:

        if player.rect.top < 600:
            player.rect.top = 600
        if 100 < player.rect.x < 386 and player.rect.y == 690:
            player.rect.y = 690

        if 1000 < player.rect.x < 1100 and player.rect.y == 600:
            room = 0
            player.rect.x = 665
            player.rect.y = 570
            sound_door.play()

        pg.draw.rect(homi_img, 'brown', (415, 645, 10, 10))
        pg.draw.rect(homi_img, 'brown', (980, 645, 45, 7))
        home_inside.blit(homi_img, (0, 0))
        screen.blit(home_inside, (0, 0))
        all_sprite = pg.sprite.Group(npc1, npc2, player)

        if player.rect.x < 384 and 592 < player.rect.y < 690:
            player.rect.x = 384
            text = font.render(f'чувак на тебе гриб! схавай! вставляет', False, 'white', 'black')
            screen.blit(text, (50, 500))


    if room == 2:

        labf.blit(labf_img, (0, 0))
        screen.blit(labf, (0, 0))
        all_sprite = pg.sprite.Group(lab, player)
        labhit = pg.sprite.spritecollide( player, all_sprite, False)

        if labhit:
            print('12')


    if room == 3:   #грибы с триггером босса

        tropa.blit(tropa_img, (0, 0))
        screen.blit(tropa, (0, 0))
        '''grt.blit(grt_img, (0, 0))
        screen.blit(grt, (0, 0))'''
        if player.rect.left < 569:
            player.rect.left = 569
        if player.rect.right > 805:
            player.rect.right = 805
        if player.rect.top < 425:
            player.rect.top = 425

        #trigger
        if 645 < player.rect.x < 670 and 475 < player.rect.y < 500:
            aplayer.rect.x = player.rect.x
            aplayer.rect.y = player.rect.y
            room = 3.1

    if room == 3.1:
        all_sprite = pg.sprite.Group(boss1, aplayer)
        if aplayer.rect.bottom > 610:
            room = 3.2

    if room == 3.2:
        boss1.image = pil('спрайты/гг диалог 1/босссп/гриб босс/тень босса.png')
        all_sprite = pg.sprite.Group(boss1, aplayer)
        if aplayer.rect.bottom > 610:
            room = 3.3


    upd()

pg.quit()