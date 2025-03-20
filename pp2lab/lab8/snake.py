import pygame
import random

pygame.init() #инициация пайгейм

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #окно игры
pygame.display.set_caption('Snake') #название окна
clock = pygame.time.Clock() # для стабилизации фпс и скорости игры
snake_position = 10 # размер змейки
font_style = pygame.font.SysFont("Century",25) #вид текста когда проигрываем ,шрифт
score_font = pygame.font.SysFont("Arial",35) #вид текста счетчика уровня и еды
pygame.mixer.init()

eat_sound = pygame.mixer.Sound("sounds/5e9cc940c9e1cc1.mp3")  #звук еды
game_over_sound = pygame.mixer.Sound("sounds/8d3b1fa30e92ead.mp3")  #звук проигрыша
game_over_sound.set_volume(0.1)
def score_apple(score, level): #функция для текста счетчика
    value = score_font.render(f"Score: {score}    Level: {level}", True, (255,255,255)) #рендер рисует текст со счетом
    screen.blit(value, [10,10])  # позиция счетчика

def our_snake(snake, snake_list): #функция самой змейки
    for x in snake_list: #лист имеет все позиции части змейки
        pygame.draw.rect(screen, (200,0,50), [x[0],x[1], snake,snake]) #отрисовываем части змейки в каждой позиции

def message(msg, color): #когда проигрываем
    mesg = font_style.render(msg,True, color) # вид текста
    screen.blit(mesg,[WIDTH/6, HEIGHT/3]) #положение текста

def generate_food(snake_list): #создание еды
    while True:
        fx = round(random.randrange(0,WIDTH-snake_position)/10.0)*10 #положение еды в координате х(раунд и умножение и деление на 10 для того чтобы еда появлялся в правильной позиции чтобы змейка и еда были в одной позиции)
        fy = round(random.randrange(0,HEIGHT-snake_position)/10.0)*10 #положение еды в координате у
        if [fx, fy] not in snake_list: #чтобы еда не появилось в нашем теле
            return fx, fy

def gameLoop(): #настройки и цикл самой игры
    pygame.mixer.music.load("sounds/60da2b0c2e41b44.mp3")  # фоновая музыка
    pygame.mixer.music.play(-1)  # бесконечный повтор
    game_over = False #проверка завершения игры
    game_close = False #проверка проигрыша
    x1 = WIDTH / 2 #позиция змейки в начале игры
    y1 = HEIGHT / 2 #позиция змейки в начале игры
    x1_change = 0 #изменение координат змейки
    y1_change = 0 #изменение координат змейки
    snake_length = [] #сохраняем здесь тело(длину) змейки
    length = 1 #начальная длина
    level = 1 #начальный уровень
    speed = 10 #скорость изменения позиции змейки
    fx,fy = generate_food(snake_length) #рандомная генерация еды

    while not game_over: #пока игра не завершится
        while game_close: #пока не проиграем
            pygame.mixer.music.stop()  #фоновая музыка в паузе
            pygame.mixer.Sound.play(game_over_sound)  #звук проигрыша

            screen.fill((0 ,200,100)) #цвет заднего фона
            message("You lose! Tap E for exit or R for restart",(255,255,255)) #параметры функции мессейдж
            pygame.display.update() #обновляем экран
            for event in pygame.event.get(): #событии
                if event.type==pygame.QUIT: #закрытие окна
                    game_over=True
                    game_close=False
                if event.type==pygame.KEYDOWN: #событие с клавишами
                    if event.key==pygame.K_e: #если нажимаем е игра заканчивается и окно закрывается
                        game_over=True
                        game_close=False
                    if event.key ==pygame.K_r: #если нажимаем r(к) игра возобновляется и функция геймлуп начинается с самого начало

                        gameLoop()

        for event in pygame.event.get(): #событии
            if event.type == pygame.QUIT: #закрытие окна
                game_over=True
            if event.type == pygame.KEYDOWN: #событие с клавишами
                if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and x1_change == 0: #проверка нажатие a или стрелки влево ← и чтобы змейка не повернулся назад на 180 градусов
                    x1_change = -snake_position #здесь получается -10 и это изменение позиции по оси х
                    y1_change = 0 #чтобы змейка не двигалась по оси у
                elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and x1_change ==0:
                    x1_change = snake_position
                    y1_change = 0
                elif (event.key == pygame.K_UP or event.key == pygame.K_w) and y1_change==0: #роверка нажатия w или стрелки вверх ↑  и чтобы змейка не двигалась вниз
                    y1_change = -snake_position #изменение позиции змейки по оси у
                    x1_change = 0 #чтобы змейка не пошел по оси х
                elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and y1_change == 0:
                    y1_change =snake_position
                    x1_change = 0

        if x1 >=WIDTH or x1<0 or y1>=HEIGHT or y1<0: #проверка если змейка выходит за границы окна игра заканчивается
            pygame.mixer.Sound.play(game_over_sound)
            game_close = True

        x1 += x1_change #изменение позиции змейки по оси х
        y1 += y1_change #измененная позиция змейки по оис у
        screen.fill((0,200,100)) #после каждой изменении позиции задний фон оставалась зеленой без этого каждая позиция где была змейка будет красной
        pygame.draw.rect(screen,(255,255,0),[fx,fy,snake_position,snake_position])  #рисует еду

        snake_head = [x1,y1] #список с текущими координатами головы змейки
        snake_length.append(snake_head) #добавляем новую часть тело змейке в список частей тел

        if len(snake_length) >length: #чтобы змейка увеличивалась с хвоста а не с головы
            del snake_length[0]

        for x in snake_length[:-1]: #проверка положения змейки если любая его часть будет внутри змейки игра заканчивается точнее если мы столкнемся с самим собой
            if x == snake_head:
                pygame.mixer.Sound.play(game_over_sound)
                game_close = True

        our_snake(snake_position,snake_length) #параметры функции измененные
        score_apple(length-1,level) #параметры функции измененные
        pygame.display.update() #обновление экрана

        if x1 == fx and y1 == fy: #если наши координаты и координаты еды будут равны мы сьедаем еду
            fx,fy =generate_food(snake_length) #создает новую еду в новом положении
            length +=1 #длина увеличивается
            pygame.mixer.Sound.play(eat_sound) #звук сьедания еда
            if length %3 == 0: #после каждой 3 еды игра становится сложнее
                level +=1
                speed +=2

        clock.tick(speed) #скорость игры и фпс

    pygame.quit() #закрытие игры после его окончания
    quit()

gameLoop()

