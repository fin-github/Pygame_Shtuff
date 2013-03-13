import pygame, sys
from pygame.locals import *

pygame.init()
MAIN_SURF = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Quarto')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
LIGHT_GREEN = (0, 100, 0)
BLUE = (0, 0, 128)
YELLOW = (255, 255, 0)
LIGHT_YELLOW = (100, 100, 0)
RED = (255, 0, 0)
LIGHT_RED = (100, 0, 0)

class Board():

    def __init__(self, position, board_width, square_width):
        self.position = position
        self.total_squares = board_width * board_width
        self.square_width = square_width
        self.squares = []
        for square_num in range(self.total_squares):
            new_square = Square(square_num, self.position, self.square_width)
            self.squares.append(new_square)
        width = (board_width * square_width) + (5 * (board_width - 1))
        self.surface = pygame.Surface((width, width))

    def set_square(self, square_number, piece):
        pass

    def get_square(self, square_number):
        pass

    def get_board_surface(self):
        for square in self.squares:
            square_surf = square.get_square_surface()
            self.surface.blit(square_surf, square.position)
        self.surface.fill(BLACK)
        return self.surface

    def draw_board(self):
        board_surf = self.get_board_surface()
        MAIN_SURF.blit(board_surf, self.position)
    
class Square():

    def __init__(self, square_number, board_position, width):
        self.square_num = square_number
        self.width = width
        #Do some math here!!
        self.position = (0,0)

    def get_val(self):
        pass

    def set_val(self):
        pass

    def get_location(self):
        return (self.x, self.y)

    def get_square_surface(self):
        pass

def right_arrow_pressed():
    print "Right Pressed!"

def left_arrow_pressed():
    print "Left Pressed!"

def down_arrow_pressed():
    print "Down Pressed!"

def up_arrow_pressed():
    print "Up Pressed!"

MAIN_SURF.fill(WHITE)
my_board = Board((100,50), 4, 100)
my_board.draw_board()

while True: # main game loop
    #MAIN_SURF.fill(WHITE)
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
            #mouse_click()
            pass
    pygame.display.update()
