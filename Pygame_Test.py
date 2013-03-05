import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Are You Ready?')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
YELLOW = (153, 153, 0)
LIGHT_YELLOW = (255, 255, 102)

titleFont = pygame.font.Font(
    'freesansbold.ttf', 50)
textSurfaceObj = titleFont.render('Are You Ready?', True, BLACK)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 60)

mouse_on_button = False

def right_arrow_pressed():
    print "Right Pressed!"

def left_arrow_pressed():
    print "Left Pressed!"

def down_arrow_pressed():
    print "Down Pressed!"

def up_arrow_pressed():
    print "Up Pressed!"

def check_mouse_pos():
    #mouse_x, mouse_y = pygame.mouse.get_pos()
    the_rect = (get_my_button(LIGHT_YELLOW))[1]
    if the_rect.collidepoint(pygame.mouse.get_pos()):
        back_color = YELLOW
    else:
        back_color = LIGHT_YELLOW
    button, buttons_rect = get_my_button(back_color)
    DISPLAYSURF.blit(button, buttons_rect)

def mouse_click():
    pass

def get_my_button(back_color):
    buttonFont = pygame.font.Font('freesansbold.ttf', 30)
    my_button = buttonFont.render('Let\'s Go!', True, BLACK, back_color)
    my_buttons_rect = my_button.get_rect()
    my_buttons_rect.center = (200, 200)
    return [my_button, my_buttons_rect]

while True: # main game loop
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
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
        elif(event.type == MOUSEMOTION):
            #check_mouse_pos()
            pass
        elif(event.type == MOUSEBUTTONDOWN):
            mouse_click()
    check_mouse_pos()
    pygame.display.update()
