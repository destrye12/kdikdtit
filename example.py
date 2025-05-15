import pygame
import sys

pygame.init()

# Настройки экрана
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

# Жёлтый цвет, с которым будем проверять касание
YELLOW = (255, 255, 0)

# Создаём поверхность с жёлтым прямоугольником
background = pygame.Surface(screen.get_size())
background.fill((0, 0, 0))
pygame.draw.rect(background, YELLOW, (150, 100, 100, 100))  # жёлтый квадрат

# Спрайт - синий квадрат
sprite_size = 30
sprite = pygame.Surface((sprite_size, sprite_size))
sprite.fill((0, 0, 255))
sprite_rect = sprite.get_rect()
sprite_rect.topleft = (0, 0)

def is_touching_yellow(surface, rect):
    # Проверяем несколько точек по краям спрайта на жёлтый цвет
    points_to_check = [
        rect.topleft,
        rect.topright,
        rect.bottomleft,
        rect.bottomright,
        rect.center
    ]
    for point in points_to_check:
        if 0 <= point[0] < surface.get_width() and 0 <= point[1] < surface.get_height():
            color = surface.get_at(point)[:3]  # получаем RGB без альфа
            if color == YELLOW:
                return True
    return False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            sprite_rect.topleft = event.pos

    screen.blit(background, (0, 0))
    screen.blit(sprite, sprite_rect)

    if is_touching_yellow(background, sprite_rect):
        pygame.display.set_caption("Касание жёлтого цвета!")
    else:
        pygame.display.set_caption("")

    pygame.display.flip()
    clock.tick(60)
