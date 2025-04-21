
import pygame

pygame.init()
WIDTH=HEIGHT= 500

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Red Ball")

WHITE = (255,255,255)
RED = (255,0,0)

r = 25
x,y = WIDTH//2,HEIGHT//2
step = 10
running = True
while running:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x-r-step>= 0:
        x -= step
    if keys[pygame.K_RIGHT] and x+r +step<= WIDTH:
        x +=step
    if keys[pygame.K_UP] and y-r-step >= 0:
        y -= step
    if keys[pygame.K_DOWN] and y+r+step <= HEIGHT:
        y += step

    screen.fill(WHITE)
    pygame.draw.circle(screen,RED,(x,y),r)
    pygame.display.update()

pygame.quit()
