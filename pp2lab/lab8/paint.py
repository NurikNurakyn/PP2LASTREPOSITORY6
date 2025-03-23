import pygame

#Инициализация Pygame
pygame.init()

#Настройки окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint App")

#Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
current_color = BLACK

#Переменные
clock = pygame.time.Clock()
drawing = False
last_pos = None
tool = "pen"  #Доступные инструменты: 'pen', 'rectangle', 'circle', 'eraser'
start_pos = None

#Очистка экрана
screen.fill(WHITE)

#Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #Нажатие мышки
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            last_pos = event.pos
            start_pos = event.pos
        #Отпускаем мышку
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            #Рисуем прямоугольник который повляется с места нажатия мышки до места отпускания
            if tool == "rectangle":
                rect_width = abs(event.pos[0] - start_pos[0])
                rect_height = abs(event.pos[1] - start_pos[1])
                rect_x = min(event.pos[0], start_pos[0])
                rect_y = min(event.pos[1], start_pos[1])
                pygame.draw.rect(screen, current_color, (rect_x, rect_y, rect_width, rect_height), 2)
            #Рисуем круг который повляется с места нажатия мышки до места отпускания
            elif tool == "circle":
                radius = int(((event.pos[0] - start_pos[0]) ** 2 + (event.pos[1] - start_pos[1]) ** 2) ** 0.5)
                pygame.draw.circle(screen, current_color, start_pos, radius, 2)
        #Рисуем с зажатой мышкой
        elif event.type == pygame.MOUSEMOTION and drawing:
            if tool == "pen":
                pygame.draw.line(screen, current_color, last_pos, event.pos, 2)
                last_pos = event.pos
            elif tool == "eraser":
                pygame.draw.line(screen, WHITE, last_pos, event.pos, 10)
                last_pos = event.pos

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:  #Ручка
                tool = "pen"
            elif event.key == pygame.K_2:  #Прямоугольник
                tool = "rectangle"
            elif event.key == pygame.K_3:  #Круг
                tool = "circle"
            elif event.key == pygame.K_4:  #ЛАстик
                tool = "eraser"
            elif event.key == pygame.K_c:  #Очистка экрана
                screen.fill(WHITE)
            elif event.key == pygame.K_r:
                current_color = (255, 0, 0)  #Красный
            elif event.key == pygame.K_g:
                current_color = (0, 255, 0)  #Зеленый
            elif event.key == pygame.K_b:
                current_color = (0, 0, 255)  #Синий

    pygame.display.update()
    clock.tick(60)

pygame.quit()
