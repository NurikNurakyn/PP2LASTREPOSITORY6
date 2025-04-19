import pygame
import random
import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="PhoneBook",
        user="postgres",
        password="Fdrj19525",
        host="localhost",
        port="5432"
    )

def get_or_create_user(username):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    result = cur.fetchone()
    if result:
        user_id = result[0]
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()

    cur.execute("SELECT level, score FROM user_scores WHERE user_id = %s", (user_id,))
    score_data = cur.fetchone()
    if not score_data:
        cur.execute("INSERT INTO user_scores (user_id) VALUES (%s)", (user_id,))
        conn.commit()
        level, score = 1, 0
    else:
        level, score = score_data

    cur.close()
    conn.close()
    return user_id, level, score

def save_game_state(user_id, level, score):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE user_scores 
        SET level = %s, score = %s 
        WHERE user_id = %s
    """, (level, score, user_id))
    conn.commit()
    cur.close()
    conn.close()


pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()
snake_position = 10
font_style = pygame.font.SysFont("Century", 25)
score_font = pygame.font.SysFont("Cambria", 35)

pygame.mixer.init()
eat_sound = pygame.mixer.Sound("sounds_for_snake/5e9cc940c9e1cc1.mp3")
game_over_sound = pygame.mixer.Sound("sounds_for_snake/8d3b1fa30e92ead.mp3")
game_over_sound.set_volume(0.1)

def score_apple(score, level):
    value = score_font.render(f"Score: {score}    Level: {level}", True, (255,255,255))
    screen.blit(value, [10,10])

def our_snake(snake, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, (200,0,50), [x[0],x[1], snake,snake])

def message(msg, color):
    mesg = font_style.render(msg,True, color)
    screen.blit(mesg,[WIDTH/6, HEIGHT/3])

def generate_food(snake_list, walls):
    while True:
        food_weight = random.randint(1,3)
        food_size = (food_weight - 1)*5
        fx = round(random.randrange(0,WIDTH-snake_position)/10.0)*10
        fy = round(random.randrange(100,HEIGHT-snake_position)/10.0)*10
        food_rect = pygame.Rect(fx, fy, food_size + 10, food_size + 10)
        if all(abs(fx - x[0]) >= food_size or abs(fy - x[1]) >= food_size for x in snake_list):
            if not any(food_rect.colliderect(w) for w in walls):
                return fx, fy, food_weight, pygame.time.get_ticks()

def draw_walls(walls):
    for wall in walls:
        pygame.draw.rect(screen, (0,0,0), wall)

def get_walls(level):
    if level == 1:
        return []
    elif level == 2:
        return [pygame.Rect(300, 200, 200, 10)]
    elif level == 3:
        return [pygame.Rect(200, 150, 400, 10), pygame.Rect(200, 450, 400, 10)]
    return []

def pause():
    paused = True
    pygame.mixer.music.pause()
    while paused:
        pause_font = pygame.font.SysFont("Century",40)
        pause_text = pause_font.render("PAUSE(Press P to Resume)",True,(0,0,0))
        screen.blit(pause_text,(140,240))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pygame.mixer.music.unpause()
                    paused = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

def main_menu():
    global user_speed, user_level
    running = True
    user_speed = 5
    user_level = 1
    while running:
        screen.fill((200, 250, 200))  # постоянный фон (не менять!)
        game_name_font = pygame.font.SysFont("Cambria", 40)
        points_font = pygame.font.SysFont("Cambria", 30)

        game_name = game_name_font.render("Snake (Beta version:0.0.1)", True, (25, 69, 4))
        menu1 = points_font.render("New Game (Press ENTER)", True, (0,0,0))
        menu2 = points_font.render("Exit (Press ESCAPE)", True, (0,0,0))
        speed_text = points_font.render(f"Speed: {user_speed} (← →)", True, (0,0,0))
        level_text = points_font.render(f"Level: {user_level} (↑ ↓)", True, (0,0,0))

        screen.blit(game_name,[180,30])
        screen.blit(menu1, [10, 250])
        screen.blit(menu2, [10, 305])
        screen.blit(speed_text, [10, 360])
        screen.blit(level_text, [10, 410])

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    running = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_LEFT and user_speed > 0:
                    user_speed -= 1
                elif event.key == pygame.K_RIGHT and user_speed < 9:
                    user_speed += 1
                elif event.key == pygame.K_UP and user_level < 3:
                    user_level += 1
                elif event.key == pygame.K_DOWN and user_level > 1:
                    user_level -= 1

def gameLoop():
    pygame.mixer.music.load("sounds_for_snake/60da2b0c2e41b44.mp3")
    pygame.mixer.music.play(-1)
    game_over = False
    game_close = False

    x1 = WIDTH / 2
    y1 = HEIGHT / 2
    x1_change = 0
    y1_change = 0
    snake_length = []
    length = 1
    level = user_level
    score = 0
    speed = 5 + user_speed
    walls = get_walls(level)

    fx, fy, food_weight, food_timer = generate_food(snake_length, walls)

    while not game_over:
        while game_close:
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(game_over_sound)
            screen.fill((0, 200, 100))
            message("You lose! Tap E for exit or R for restart", (255, 255, 255))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause()
                if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and x1_change == 0:
                    x1_change = -snake_position
                    y1_change = 0
                elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and x1_change == 0:
                    x1_change = snake_position
                    y1_change = 0
                elif (event.key == pygame.K_UP or event.key == pygame.K_w) and y1_change == 0:
                    y1_change = -snake_position
                    x1_change = 0
                elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and y1_change == 0:
                    y1_change = snake_position
                    x1_change = 0

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            pygame.mixer.Sound.play(game_over_sound)
            game_close = True

        head_rect = pygame.Rect(x1, y1, snake_position, snake_position)
        if any(head_rect.colliderect(w) for w in walls):
            pygame.mixer.Sound.play(game_over_sound)
            game_close = True

        if pygame.time.get_ticks() - food_timer > 5000:
            fx, fy, food_weight, food_timer = generate_food(snake_length, walls)

        x1 += x1_change
        y1 += y1_change
        screen.fill((0, 200,100))
        draw_walls(walls)

        food_size = snake_position + (food_weight - 1) * 5
        pygame.draw.rect(screen, (255, 255, 0), [fx, fy, food_size, food_size])

        snake_head = [x1, y1]
        snake_length.append(snake_head)

        if len(snake_length) > length:
            del snake_length[0]

        for x in snake_length[:-1]:
            if x == snake_head:
                pygame.mixer.Sound.play(game_over_sound)
                game_close = True

        our_snake(snake_position, snake_length)
        score_apple(length - 1, level)
        pygame.display.update()

        for x in range(fx, fx + food_size, 5):
            for y in range(fy, fy + food_size, 5):
                if x1 == x and y1 == y:
                    fx, fy, food_weight, food_timer = generate_food(snake_length, walls)
                    length += food_weight
                    score += food_weight
                    pygame.mixer.Sound.play(eat_sound)
        clock.tick(speed)

    save_game_state(user_id, level, score)
    pygame.quit()
    quit()

username1 = input("Enter your username: ")
user_id, user_level, user_score = get_or_create_user(username1)

main_menu()
gameLoop()
