import pygame
import random

# Константы игры
WIDTH, HEIGHT = 800, 600
FPS = 60
COLOR = (128, 219, 134)
t_size = 80

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Лови подарки!')

# Иконка игрового окна
icon = pygame.image.load("img/boxes_icon.jpg")
pygame.display.set_icon(icon)

# Загрузка изображений
img_background = pygame.image.load("img/background22.jpg")
img_box = pygame.image.load("img/img_box2.png")
img_cracker = pygame.image.load("img/img_fire1.png")
img_SC = pygame.image.load("img/SC_Win.jpg")
img_boom = pygame.image.load("img/Boom_lose.jpg")
box = pygame.transform.scale(img_box, (t_size, t_size))
cracker = pygame.transform.scale(img_cracker, (t_size, t_size))
background = pygame.transform.scale(img_background, (WIDTH, HEIGHT))
SC = pygame.transform.scale(img_SC, (WIDTH, HEIGHT))
boom = pygame.transform.scale(img_boom, (WIDTH, HEIGHT))

# Счетчики
boxes_caught = 0
crackers_caught = 0

# Время появления цели
target_time = 0
target_duration = 1000  # 1 секунда в миллисекундах

# Функция для выбора новой цели
def new_target():
    return random.choice([box, cracker]), random.randint(0, WIDTH - t_size), random.randint(0, HEIGHT - t_size)

# Изначальная цель
target_img, target_x, target_y = new_target()
target_visible = True

running = True
clock = pygame.time.Clock()

while running:
    screen.blit(background, (0,0))

    # Проверка условий победы и поражения
    if boxes_caught >= 15:
        screen.blit(SC, (0, 0))
        pygame.display.update()
        pygame.time.wait(5000)  # Ждем 5 секунд перед выходом
        running = False
    elif crackers_caught >= 3:
        screen.blit(boom, (0, 0))
        pygame.display.update()
        pygame.time.wait(5000)  # Ждем 5 секунд перед выходом
        running = False

    current_time = pygame.time.get_ticks()  # Получаем текущее время в миллисекундах

    # Проверка времени появления цели
    if current_time - target_time >= target_duration:
        target_visible = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_visible and target_x < mouse_x < target_x + t_size and target_y < mouse_y < target_y + t_size:
                if target_img == box:
                    boxes_caught += 1
                elif target_img == cracker:
                    crackers_caught += 1
                target_visible = False

    # Если цель невидима, создаем новую цель
    if not target_visible:
        target_img, target_x, target_y = new_target()
        target_time = current_time  # Сбрасываем таймер
        target_visible = True

    # Отображение текущей цели на экране
    if target_visible:
        screen.blit(target_img, (target_x, target_y))

    # Отображение счетчиков на экране
    font = pygame.font.Font(None, 36)
    text_boxes = font.render(f"Подарки: {boxes_caught}/15", True, (0, 0, 0))
    text_crackers = font.render(f"Хлопушки: {crackers_caught}/3", True, (0, 0, 0))

    screen.blit(text_boxes, (10, 10))
    screen.blit(text_crackers, (10, 40))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()










