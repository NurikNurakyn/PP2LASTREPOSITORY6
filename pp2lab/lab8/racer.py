import pygame
import sys
import random
import time

# Инициализация Pygame
pygame.init()

# Размеры окна
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game")

# Фон
background = pygame.image.load("images_for_racer/AnimatedStreet.png")

# Загрузка изображений
player_img = pygame.image.load("images_for_racer/Player.png")
enemy_img = pygame.image.load("images_for_racer/Enemy.png")

pygame.mixer.music.load("sounds_for_racer/background.wav")
pygame.mixer.music.play(-1)

def main_menu():
    font = pygame.font.SysFont("Cambria", 30)
    points_font = pygame.font.SysFont("Cambria", 20)
    BLACK = (0, 0, 0)
    running = True
    car_y = 600  # Начальная позиция машины
    while running:
        screen.blit(background, (0, 0))
        screen.blit(player_img, (150, car_y))

        # Анимация движения машины
        car_y -= 5
        if car_y < -100:
            car_y = 600

        # Тексты меню
        game_name = font.render("Racing Game", True, BLACK)
        menu1 = points_font.render("New Game (Press ENTER)", True, BLACK)
        menu2 = points_font.render("Exit (Press ESCAPE)", True, BLACK)

        screen.blit(game_name, (100, 50))
        screen.blit(menu1, (50, 250))
        screen.blit(menu2, (50, 300))

        pygame.display.update()
        pygame.time.delay(50)  # Замедление анимации

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return  # Начать игру
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

def pause():
    pause = True
    pygame.mixer.music.pause()
    while pause:
        pause_font = pygame.font.SysFont("Century",20)
        pause_text = pause_font.render("PAUSE(Press P to Resume)",True,(0,0,0))
        screen.blit(pause_text,(50,250))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pygame.mixer.music.unpause()
                    pause = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit
                    quit()

def gameloop():
    # Начальные параметры
    BASE_SPEED = 5  #базовая скорость врагов
    SCORE = 0
    COINS_COLLECTED = 0
    FPS = 60
    TURBO_ACTIVE = False  #будущая ультимативная способность за монеты
    TURBO_TIME = 0
    # Координаты игрока
    player_x = 160
    player_y = 520
    player_speed = 5  #cкорость игрока
    pygame.mixer.music.load("sounds_for_racer/background.wav") #музыка заднего фона
    pygame.mixer.music.play(-1)

    # Цвета
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)

    # Шрифты
    font = pygame.font.SysFont("Verdana", 60)
    font_small = pygame.font.SysFont("Verdana", 20)
    game_over = font.render("Game Over", True, BLACK)

    # Координаты врага
    enemy_x = random.randint(40, SCREEN_WIDTH - 40)
    enemy_y = -100

    # Координаты монеты
    coin_x = random.randint(40, SCREEN_WIDTH - 40)
    coin_y = random.randint(50, SCREEN_HEIGHT - 150)

    # Игровой цикл
    clock = pygame.time.Clock()

    running = True
    while running:
        # Проверка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_p:
                    pause()

        # Движение игрока
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player_x > 0:
            player_x -= player_speed
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and player_y < SCREEN_HEIGHT - 50:
            player_y += player_speed
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and player_y > 0:
            player_y -= player_speed
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player_x < SCREEN_WIDTH - 50:
            player_x += player_speed


        #Активация турбо-режима
        if keys[pygame.K_SPACE] and COINS_COLLECTED >= 10 and not TURBO_ACTIVE:
            COINS_COLLECTED -= 10
            TURBO_ACTIVE = True
            TURBO_TIME = pygame.time.get_ticks() #получить время в миллисекундах
            player_speed = 20  # Временно увеличиваем скорость игрока

        #Выключение турбо-режима через 1 секунду
        if TURBO_ACTIVE and pygame.time.get_ticks() - TURBO_TIME > 1000: #Проверяем прошла ли секунда
            TURBO_ACTIVE = False
            player_speed = 5  # Возвращаем обычную скорость игрока

        #Увеличение сложност
        speed_multiplier = min(1+ (SCORE//5)*0.1, 3)  # Машины ускоряются когда счетчик больше 5 каждый раз и до x3 максимум
        SPEED = BASE_SPEED * speed_multiplier

        # Движение врага
        enemy_y += SPEED
        if enemy_y > SCREEN_HEIGHT:
            SCORE += 1
            enemy_y = -random.randint(50, 150) #Для более плавного появления будто едет сверху вниз
            enemy_x = random.randint(40, SCREEN_WIDTH - 40)

            # Псле каждых 10 машин уменьшаем интервал появления и игра становиться немного сложнее
            if SCORE % 10 == 0:
                enemy_y = -random.randint(10, 50)

        #проверка столкновения(Здесь берем прямоугольники для того чтобы точно рассчитать столкновение машин)
        player_rect = pygame.Rect(player_x, player_y, 50, 100)
        enemy_rect = pygame.Rect(enemy_x, enemy_y, 50, 100)

        #Действия после столкновения
        if player_rect.colliderect(enemy_rect):
            pygame.mixer.Sound('sounds_for_racer/crash.wav').play()
            time.sleep(0.5)
            screen.fill(RED)
            screen.blit(game_over, (30, 250))
            pygame.display.update()
            time.sleep(2)
            running = False

        #Проверка сбора монеты
        coin_rect = pygame.Rect(coin_x, coin_y, 20, 20)
        if player_rect.colliderect(coin_rect):
            COINS_COLLECTED += 1
            coin_x = random.randint(40, SCREEN_WIDTH - 40)
            coin_y = random.randint(50, SCREEN_HEIGHT - 150)

        #показать на экране дорогу и машины с игроком
        screen.blit(background, (0, 0))
        screen.blit(player_img, (player_x, player_y))
        screen.blit(enemy_img, (enemy_x, enemy_y))

        #монетв
        pygame.draw.circle(screen, YELLOW, (coin_x, coin_y), 10)

        #отображение счёта
        scores = font_small.render(f"Score: {SCORE}", True, BLACK)
        screen.blit(scores, (10, 10))
        coins_text = font_small.render(f"Coins: {COINS_COLLECTED}", True, BLACK)
        screen.blit(coins_text, (10, 40))
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()
main_menu()
gameloop()
#