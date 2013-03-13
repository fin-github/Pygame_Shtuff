import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((500, 400))
pygame.display.set_caption('Are You Ready?')

NO_CHANGE = 0
DOWN = 1
UP = 2
current_light = 0
current_acc = 0
current_x = 0
current_theta = 0
current_vel = 0

acc = 0
ACC_INCREASE = 1
ACC_DECREASE = -1

vel_lim = 5
acc_lim = 1
friction_acc = .1
acc_step = .03

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
LIGHT_GREEN = (0, 100, 0)
BLUE = (0, 0, 128)
YELLOW = (255, 255, 0)
LIGHT_YELLOW = (100, 100, 0)
RED = (255, 0, 0)
LIGHT_RED = (100, 0, 0)

traffic_light = pygame.image.load("Traffic_Light.gif")
traffic_light = pygame.transform.scale(traffic_light, (139, 142))

def change_light(direction):
    global current_light
    current_light = (current_light + direction)%3
    lights_array = [False, False, False]
    lights_array[current_light] = True
    draw_lights(lights_array)

def draw_lights(lights_array):
    move_by = get_move_by()
    light_colors = [RED, YELLOW, GREEN]
    off_colors = [LIGHT_RED, LIGHT_YELLOW, LIGHT_GREEN]
    for light in range(3):
        if(not lights_array[light]):
            light_colors[light] = off_colors[light]
    pygame.draw.circle(DISPLAYSURF, light_colors[0], (72 - move_by, 35), 16)
    pygame.draw.circle(DISPLAYSURF, BLACK, (72 - move_by, 35), 16, 3)
    pygame.draw.circle(DISPLAYSURF, light_colors[1], (72 - move_by, 74), 16)
    pygame.draw.circle(DISPLAYSURF, BLACK, (72 - move_by, 74), 16, 3)
    pygame.draw.circle(DISPLAYSURF, light_colors[2], (72 - move_by, 114), 16)
    pygame.draw.circle(DISPLAYSURF, BLACK, (72 - move_by, 114), 16, 3)

def draw_light_holder():
    global current_x
    global traffic_light
    move_by = get_move_by()
    DISPLAYSURF.blit(traffic_light, (0 - move_by,0))
    pygame.draw.rect(DISPLAYSURF, WHITE, (108 - move_by, 136, 32, 7))
    change_light(NO_CHANGE)

def get_move_by():
    global current_x
    if (current_x > 50):
        move_by = current_x - 50
    elif (current_x < -50):
        move_by = current_x + 50
    else:
        move_by = 0
    return int(move_by)

def draw_wheel():
    global current_x
    global current_theta
    wheel = pygame.image.load("Wheel.png")
    wheel = pygame.transform.scale(wheel, (80, 80))
    wheel = rot_center(wheel, -1*current_theta)
    if(current_x > 50):
        DISPLAYSURF.blit(wheel, (400, 300))
        DISPLAYSURF.blit(wheel, (300, 300))
    elif(current_x < -50):
        DISPLAYSURF.blit(wheel, (100, 300))
        DISPLAYSURF.blit(wheel, (0, 300))
    else:
        DISPLAYSURF.blit(wheel, (int(250 + (current_x*3)), 300))
        DISPLAYSURF.blit(wheel, (int(150 + (current_x*3)), 300))
    
def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotozoom(image, angle, 1)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

def draw_background():
    global current_x
    DISPLAYSURF.fill(WHITE)
    #This will do more once we have an image or something to put in the back
    
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
                acc = ACC_INCREASE
            elif(key_map[K_UP]):
                acc = ACC_DECREASE
            elif(key_map[K_r]):
                draw_lights([True, False, False])
                current_light = 0
            elif(key_map[K_y]):
                draw_lights([False, True, False])
                current_light = 1
            elif(key_map[K_g]):
                draw_lights([False, False, True])
                current_light = 2
        elif(event.type == MOUSEBUTTONDOWN):
            print pygame.mouse.get_pos()
        elif(event.type == KEYUP):
            key_map = pygame.key.get_pressed()
            if(not key_map[K_DOWN]) or (not key_map[K_UP]):
                acc = NO_CHANGE
    if(acc == ACC_INCREASE):
        if (current_acc >= -acc_lim):
            current_acc -= acc_step
    elif(acc == ACC_DECREASE):
        if (current_acc <= acc_lim):
            current_acc += acc_step
    elif(acc == NO_CHANGE):
        if (current_vel > acc_step):
            current_acc = -friction_acc
        elif (current_vel < -acc_step):
            current_acc = friction_acc
        else:
            current_acc = 0
            current_vel = 0
    if((int(current_vel) >= vel_lim) and (current_acc < 0)) or ((int(current_vel) <= -vel_lim) and (current_acc > 0)) or (int(current_vel) in range(-vel_lim, vel_lim)):
        current_vel += current_acc
    current_x += current_vel
    current_theta += (current_vel * 5)
    draw_background()
    draw_light_holder()
    draw_wheel()
    pygame.display.update()
