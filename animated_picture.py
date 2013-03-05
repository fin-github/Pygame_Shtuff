import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((500, 400))
pygame.display.set_caption('Are You Ready?')

def right_arrow_pressed():
    print "Right Pressed!"

def left_arrow_pressed():
    print "Left Pressed!"

def down_arrow_pressed():
    print "Down Pressed!"

def up_arrow_pressed():
    print "Up Pressed!"

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
YELLOW = (153, 153, 0)
RED = (255, 0, 0)
LIGHT_YELLOW = (255, 255, 102)

traffic_light = pygame.image.load("Traffic_Light.jpg")
DISPLAYSURF.blit(traffic_light, pygame.Rect(0, 0, 700, 550))

while True: # main game loop
    for event in pygame.event.get():
        if(event.type == QUIT):
            pygame.quit()
            sys.exit()
        elif(event.type == KEYDOWN):
            key_map = pygame.key.get_pressed()
            if(key_map[K_RIGHT]):
                right_arrow_pressed()
            elif(key_map[K_LEFT]):
                left_arrow_pressed()
            elif(key_map[K_DOWN]):
                down_arrow_pressed()
            elif(key_map[K_UP]):
                up_arrow_pressed()
    pygame.display.update()
