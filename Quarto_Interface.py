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
        self.board_width = board_width
        self.square_width = square_width
        self.squares = []
        for square_num in range(self.total_squares):
            new_square = Square(square_num, self)
            self.squares.append(new_square)
        width = (board_width * square_width) + (5 * (board_width - 1))
        self.surface = pygame.Surface((width, width))
        self.board_rect = pygame.Rect(position[0], position[1], width, width)

    def set_square(self, square_number, piece):
        pass

    def get_square(self, square_number):
        pass

    def get_board_surface(self):
        self.surface.fill(BLACK)
        for square in self.squares:
            square_surf = square.get_square_surface()
            self.surface.blit(square_surf, square.position)
        return self.surface

    def draw_board(self):
        board_surf = self.get_board_surface()
        MAIN_SURF.blit(board_surf, self.position)

    def check_for_click(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.board_rect.collidepoint([mouse_x, mouse_y]):
            mouse_x -= self.position[0]
            mouse_y -= self.position[1]
            col = mouse_x / (self.square_width + 5)
            row = mouse_y / (self.square_width + 5)
            self.squares[(self.board_width * row) + col].on_click()
    
class Square():

    print "TEST"

    def __init__(self, square_number, board):
        self.square_num = square_number
        self.board = board
        self.width = self.board.square_width
        row = self.square_num / self.board.board_width
        col = self.square_num % self.board.board_width
        self.position = ((self.width + 5) * col, (self.width + 5) * row)
        self.surface = pygame.Surface((self.width, self.width))
        self.surface.fill(GREEN)
        self.holder = True

    def get_val(self):
        pass

    def set_val(self):
        pass

    def get_location(self):
        return self.position

    def get_square_surface(self):
        return self.surface

    def on_click(self):
        if self.holder:
            self.surface.fill(RED)
        else:
            self.surface.fill(GREEN)
        self.holder = not self.holder
    
def right_arrow_pressed():
    print "Right Pressed!"

def left_arrow_pressed():
    print "Left Pressed!"

def down_arrow_pressed():
    print "Down Pressed!"

def up_arrow_pressed():
    print "Up Pressed!"

my_board = Board((50,50), 4, 100)

while True: # main game loop
    MAIN_SURF.fill(WHITE)
    my_board.draw_board()
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
        elif(event.type == MOUSEBUTTONDOWN):
            my_board.check_for_click()
    pygame.display.update()
