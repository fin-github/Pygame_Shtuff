import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((500, 400))
pygame.display.set_caption('Are You Ready?')

DOWN = 1
UP = 2
current_light = 0

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
LIGHT_GREEN = (0, 255, 0, 50)
BLUE = (0, 0, 128)
YELLOW = (255, 255, 0)
LIGHT_YELLOW = (255, 255, 0, 50)
RED = (255, 0, 0)
LIGHT_RED = (255, 0, 0, 50)

def change_light(direction):
    global current_light
    current_light = (current_light + direction)%3
    lights_array = [False, False, False]
    lights_array[current_light] = True
    draw_lights(lights_array)

def draw_lights(lights_array):
    new_surf = DISPLAYSURF.convert_alpha()
    light_colors = [RED, YELLOW, GREEN]
    off_colors = [LIGHT_RED, LIGHT_YELLOW, LIGHT_GREEN]
    for light in range(3):
        if(not lights_array[light]):
            light_colors[light] = off_colors[light]
    pygame.draw.circle(new_surf, light_colors[0], (72, 35), 16)
    pygame.draw.circle(new_surf, BLACK, (72, 35), 16, 3)
    pygame.draw.circle(new_surf, light_colors[1], (72, 74), 16)
    pygame.draw.circle(new_surf, BLACK, (72, 74), 16, 3)
    pygame.draw.circle(new_surf, light_colors[2], (72, 114), 16)
    pygame.draw.circle(new_surf, BLACK, (72, 114), 16, 3)

    DISPLAYSURF.blit(new_surf, (0,0))

DISPLAYSURF.fill(WHITE)
traffic_light = pygame.image.load("Traffic_Light.jpg")
DISPLAYSURF.blit(traffic_light, pygame.Rect(0, 0, 700, 550))
draw_lights([False, False, False])

while True: # main game loop
    for event in pygame.event.get():
        if(event.type == QUIT):
            pygame.quit()
            sys.exit()
        elif(event.type == KEYDOWN):
            key_map = pygame.key.get_pressed()
            if(key_map[K_RIGHT]):
                change_light(DOWN)
            elif(key_map[K_LEFT]):
                change_light(UP)
            elif(key_map[K_DOWN]):
                change_light(DOWN)
            elif(key_map[K_UP]):
                change_light(UP)
            elif(key_map[K_SPACE]):
                draw_lights([True, True, True])
        elif(event.type == MOUSEBUTTONDOWN):
            print pygame.mouse.get_pos()
    pygame.display.update()
