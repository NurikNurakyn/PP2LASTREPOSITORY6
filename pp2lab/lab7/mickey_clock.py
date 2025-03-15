'''import pygame as py
import datetime as dt
import math
import tkinter as tk

py.init()
screen = py.display.set_mode([800, 600])

#images which I cut
img = py.image.load('images/mickeyclock_withothands.jpg')
minute_hand = py.image.load('images/hour_hand.png')
second_hand = py.image.load('images/minute_hand.png')

py.display.set_icon(img)
py.display.set_caption("Clock of Mickey")

#sound of clock
py.mixer.init()
py.mixer.music.load("music/zvuk-strelok-chasov-1-min-24125.mp3")
py.mixer.music.play()


minutes_hand = py.transform.scale(minute_hand, (500, 500))
seconds_hand = py.transform.scale(second_hand, (700, 700))

def draw_clock():
    screen.fill((255, 255, 255))
    screen.blit(img, (0,0))
    now = dt.datetime.now()
    hour = now.hour % 12
    minute = now.minute

    minute_angle = - (minute * 6)
    second_angle =

    center_x, center_y = 400, 300

    rotated_hour = py.transform.rotate(minutes_hand, minute_angle)
    rotated_minute = py.transform.rotate(seconds_hand, second_angle)

    hour_rect = rotated_hour.get_rect(center=(center_x, center_y))
    minute_rect = rotated_minute.get_rect(center=(center_x, center_y))

    screen.blit(rotated_minute, minute_rect.topleft)
    screen.blit(rotated_hour, hour_rect.topleft)

running = True
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    draw_clock()
    py.display.flip()
    py.time.delay(1000)

py.quit()
'''
import pygame as py
import datetime as dt
import math
import tkinter as tk

py.init()
screen = py.display.set_mode([800, 600])

#images which I cut
img = py.image.load('images/mickeyclock_withothands.jpg')
minute_hand = py.image.load('images/hour_hand.png')
second_hand = py.image.load('images/minute_hand.png')


py.display.set_icon(img)
py.display.set_caption("Clock of Mickey")

#sound of clock
py.mixer.init()
py.mixer.music.load("music/zvuk-strelok-chasov-1-min-24125.mp3")
py.mixer.music.play()


minutes_hand = py.transform.scale(minute_hand, (500, 500))
seconds_hand = py.transform.scale(second_hand, (700, 700))

center_x, center_y = 400, 300

def draw_clock():
    screen.fill((255, 255, 255))
    screen.blit(img, (0, 0))

    now = dt.datetime.now()
    minute = now.minute
    second = now.second

    minute_angle = - (minute * 6)
    second_angle = - (second * 6)

    rotated_minute = py.transform.rotate(minute_hand, minute_angle)
    rotated_second = py.transform.rotate(second_hand, second_angle)

    minute_rect = rotated_minute.get_rect(center=(center_x, center_y))
    second_rect = rotated_second.get_rect(center=(center_x, center_y))

    screen.blit(rotated_minute, minute_rect.topleft)
    screen.blit(rotated_second, second_rect.topleft)

running = True
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    draw_clock()
    py.display.flip()
    py.time.delay(1000)

py.quit()
