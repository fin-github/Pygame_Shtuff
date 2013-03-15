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

    def update_board_surface(self):
        self.surface.fill(BLACK)
        for square in self.squares:
            square_surf = square.get_square_surface()
            self.surface.blit(square_surf, square.position)
        return self.surface

    def draw_board(self):
        board_surf = self.update_board_surface()
        MAIN_SURF.blit(board_surf, self.position)

    def check_for_click(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.board_rect.collidepoint([mouse_x, mouse_y]):
            mouse_x -= self.position[0]
            mouse_y -= self.position[1]
            col = mouse_x / (self.square_width + 5)
            row = mouse_y / (self.square_width + 5)
            self.squares[(self.board_width * row) + col].click_action()
    
class Square():

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

    def click_action(self):
        if self.holder:
            self.surface.fill(RED)
        else:
            self.surface.fill(GREEN)
        self.holder = not self.holder
        PIECE_1 = pygame.image.load("Quarto_Pieces/Piece_1.png")
        PIECE_1 = pygame.transform.scale(PIECE_1, (self.width, self.width))
        self.surface.blit(PIECE_1, (0, 0))

class Piece_Holder():

    def __init__(self, position, board):
        self.board = board
        self.position = position
        self.surface = pygame.Surface((110, (55 * (board.total_squares / 2)) + 5))
        self.surface.fill(WHITE)
        pygame.draw.rect(self.surface, BLACK, (0, 0, 110, (55 * (board.total_squares / 2)) + 5), 5)

        pieces = []
        for x in range(board.total_squares):
            raw_piece = pygame.image.load("Quarto_Pieces/Piece_"+str(x)+".png")
            sized_piece = pygame.transform.scale(raw_piece, (50, 50))
            pieces.append(sized_piece)
            self.surface.blit(sized_piece, ((x % 2) * 55, ((x / 2) * 55) + 5))
        

    def draw_holder(self):
        MAIN_SURF.blit(self.surface, self.position)


my_board = Board((300, 50), 4, 100)
my_piece_holder = Piece_Holder((10, 10), my_board)
#PIECE_1 = pygame.image.load("Quarto_Pieces/Piece_1.jpg")
#PIECE_1 = pygame.transform.scale(PIECE_1, (100, 100))


while True: # main game loop
    MAIN_SURF.fill(WHITE)
    my_board.draw_board()
    my_piece_holder.draw_holder()
    
    for event in pygame.event.get():
        if(event.type == QUIT):
            pygame.quit()
            sys.exit()
        elif(event.type == KEYDOWN):
            key_map = pygame.key.get_pressed()
        elif(event.type == MOUSEBUTTONDOWN):
            my_board.check_for_click()
    pygame.display.update()
