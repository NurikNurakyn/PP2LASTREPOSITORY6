"""import pygame as py
import time
import random

py.init()
def our_snake(snake_block, snake_list):
    for x in snake_list:
        py.draw.rect(screen, BLACK, [x[0], x[1], snake_block, snake_block])


WIDTH = 800 #Ширина игрового экрана
HEIGHT = 600 #Длина игрового экрана
x = 400 #Стартовые координаты змеи по оси х
y = 300 #Стартовые координаты змеи по оси у
x_step = 0 #шаг за определенное время с time по оси х
y_step = 0 #шаг за определенное время с time по оси у
x1 = random.randint(5, 595) #рандомные координаты появления яблоки
y1 = random.randint(5, 595) #рандомные координаты появления яблоки

WHITE = (0, 0, 0) #белый
RED = (224, 0, 0) #красный
BLACK = (255, 255, 255) #черный
GREEN = (0, 204, 100) #немного черноватый зеленый
YELLOW = (235, 204, 52) #делтый
snake_speed = 7 #скорость изменения координат змеи

screen = py.display.set_mode((WIDTH, HEIGHT))
background = py.image.load("images/background_snake.jpg")
py.display.set_caption("Snake")
icon = py.image.load("images/snake_icon.png")
py.display.set_icon(icon)

t = py.time.Clock() #для скорости игры и фпс стабильной

font_style = py.font.SysFont(None, 50)

def mess(msg, color):
    m = font_style.render(msg, True, color)
    screen.blit(m, [WIDTH / 3, HEIGHT / 3])

snake_lenght_list = [] #сохраняем длину змеи
snake_lenght = 1
fx = random.randrange(0, WIDTH - snake_speed)
fy = random.randrange(0, HEIGHT - snake_speed)
running = True
def game():
    while running:
        screen.blit(background, (0, 0))

        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
            if event.type == py.KEYDOWN:
                if event.key == py.K_RIGHT:
                    x_step = snake_speed
                    y_step = 0
                elif event.key == py.K_LEFT:
                    x_step = -snake_speed
                    y_step = 0
                elif event.key == py.K_UP:
                    x_step = 0
                    y_step = -snake_speed
                elif event.key == py.K_DOWN:
                    x_step = 0
                    y_step = snake_speed
                elif event.key == py.K_r:
                    game()
                elif event.key == py.K_q:
                    running = False

        if x >= 800 or x <= 0 or y >= 600 or y <= 0:
            running = False

        snake_Head = [x1, y1]
        snake_lenght_list.append(snake_Head)

        if len(snake_lenght_list) > snake_lenght:
            del snake_lenght_list[0]

        for segment in snake_lenght_list[:-1]:
            if segment == snake_Head:
                running = False

        our_snake(snake_speed, snake_lenght_list)
        py.display.update()

        if x1 == fx and y1 == fy:
            fx = random.randrange(0, WIDTH - snake_speed)
            fy = random.randrange(0, HEIGHT - snake_speed)
            snake_lenght += 1

        x += x_step
        y += y_step

        mess("You lose", RED)
        py.draw.rect(screen, RED, [x, y, 15, 15]) #наша змейка
        py.draw.rect(screen, YELLOW, [fx, fy, 20, 20]) #наша еда
        py.display.update()
        t.tick(30) #фпс в секунду

    py.quit()

game()"""
import pygame as py
import time
import random

py.init()


def game():
    WIDTH = 800 #Ширина игрового экрана
    HEIGHT = 600 #Длина игрового экрана
    x = 400 #Стартовые координаты змеи по оси х
    y = 300 #Стартовые координаты змеи по оси у
    x_step = 0 #шаг за определенное время с time по оси х
    y_step = 0 #шаг за определенное время с time по оси у
    x1 = random.randint(5, 595) #рандомные координаты появления яблоки
    y1 = random.randint(5, 595) #рандомные координаты появления яблоки

    WHITE = (0, 0, 0) #белый
    RED = (224, 0, 0) #красный
    BLACK = (255, 255, 255) #черный
    GREEN = (0, 204, 100) #немного черноватый зеленый
    YELLOW = (235, 204, 52) #делтый
    snake_speed = 7 #скорость изменения координат змеи

    screen = py.display.set_mode((WIDTH, HEIGHT))
    background = py.image.load("images/background_snake.jpg")
    py.display.set_caption("Snake")
    icon = py.image.load("images/snake_icon.png")
    py.display.set_icon(icon)

    def our_snake(snake_block, snake_list):
        for x in snake_list:
            py.draw.rect(screen, BLACK, [x[0], x[1], snake_block, snake_block])

    t = py.time.Clock() #для скорости игры и фпс стабильной

    font_style = py.font.SysFont(None, 50)

    def mess(msg, color):
        m = font_style.render(msg, True, color)
        screen.blit(m, [WIDTH / 3, HEIGHT / 3])

    snake_lenght_list = [] #сохраняем длину змеи
    snake_lenght = 1
    fx = random.randrange(0, WIDTH - snake_speed)
    fy = random.randrange(0, HEIGHT - snake_speed)
    running = True

    while running:
        screen.blit(background, (0, 0))

        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
            if event.type == py.KEYDOWN:
                if event.key == py.K_RIGHT:
                    x_step = snake_speed
                    y_step = 0
                elif event.key == py.K_LEFT:
                    x_step = -snake_speed
                    y_step = 0
                elif event.key == py.K_UP:
                    x_step = 0
                    y_step = -snake_speed
                elif event.key == py.K_DOWN:
                    x_step = 0
                    y_step = snake_speed
                elif event.key == py.K_r:
                    game()
                elif event.key == py.K_q:
                    running = False

        if x >= 800 or x <= 0 or y >= 600 or y <= 0:
            running = False

        snake_Head = [x, y]
        snake_lenght_list.append(snake_Head)

        if len(snake_lenght_list) > snake_lenght:
            del snake_lenght_list[0]

        for segment in snake_lenght_list[:-1]:
            if segment == snake_Head:
                running = False

        our_snake(snake_speed, snake_lenght_list)
        py.display.update()

        if x == fx and y == fy:
            fx = random.randrange(0, WIDTH - snake_speed)
            fy = random.randrange(0, HEIGHT - snake_speed)
            snake_lenght += 1

        x += x_step
        y += y_step

        mess("You lose", RED)
        py.draw.rect(screen, RED, [x, y, 15, 15]) #наша змейка
        py.draw.rect(screen, YELLOW, [fx, fy, 20, 20]) #наша еда
        py.display.update()
        t.tick(30) #фпс в секунду

    py.quit()

game()
