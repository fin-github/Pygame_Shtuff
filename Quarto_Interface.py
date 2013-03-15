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

    def check_for_mouse(self, dragging_piece):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.board_rect.collidepoint([mouse_x, mouse_y]):
            mouse_x -= self.position[0]
            mouse_y -= self.position[1]
            col = mouse_x / (self.square_width + 5)
            row = mouse_y / (self.square_width + 5)
            bad_drag = self.squares[(self.board_width * row) + col].click_action(dragging_piece)
            if(bad_drag):
                return False
            else:
                return True
        else:
            return False
    
class Square():

    EMPTY = 0

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
        self.piece = Square.EMPTY

    def get_val(self):
        pass

    def set_val(self):
        pass

    def get_location(self):
        return self.position

    def get_square_surface(self):
        return self.surface

    def click_action(self, piece_num):
        if(self.piece == Square.EMPTY):
            raw_piece = pygame.image.load("Quarto_Pieces/Piece_"+str(piece_num)+".png")
            self.piece = pygame.transform.scale(raw_piece, (100, 100))
            self.surface.blit(self.piece, (0, 0))
            return False
        else:
            return True

class Piece_Holder():

    NO_CLICK = 7
    DONE_MOVING = -2
    RETURN_STEPS = 30

    def __init__(self, position, board):
        self.board = board
        self.position = position
        self.surface = pygame.Surface((110, (55 * (board.total_squares / 2)) + 5))
        pieces = []
        for square in range(board.total_squares):
            pieces.append(Holder_Square(square, self))
        self.squares = pieces
        self.holder_rect = pygame.Rect(position[0], position[1], 110, (55 * (board.total_squares / 2)) + 5)
        self.moving_piece = Piece_Holder.DONE_MOVING
        self.moving_piece_loc = (0, 0)


    def update_holder_surface(self):
        self.surface.fill(WHITE)
        pygame.draw.rect(self.surface, BLACK, (0, 0, 110, (55 * (self.board.total_squares / 2)) + 5), 5)
        for square in self.squares:
            square_surf = square.get_square_surface()
            self.surface.blit(square_surf, square.position)
        return self.surface
        

    def draw_holder(self):
        self.surface = self.update_holder_surface()
        MAIN_SURF.blit(self.surface, self.position)


    def check_for_click(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.holder_rect.collidepoint([mouse_x, mouse_y]):
            mouse_x -= self.position[0]
            mouse_y -= self.position[1]
            col = mouse_x / (55)
            row = mouse_y / (55)
            clicked_piece = self.squares[(row * 2) + col].click_action()
            if(clicked_piece == Holder_Square.EMPTY):
                return (Piece_Holder.NO_CLICK, 0)
            else:
                return (clicked_piece, (row * 2) + col)
        else:
            return (Piece_Holder.NO_CLICK, 0)

    def put_piece_back(self, piece, location):
        self.moving_piece = piece
        self.moving_piece_loc = location
        destination_x, destination_y = self.squares[piece].position
        final_destination = (destination_x + self.position[0], destination_y + self.position[1])
        delta_x = location[0] - final_destination[0]
        delta_y = location[1] - final_destination[1]
        x_vals = []
        y_vals = []
        for step in range(Piece_Holder.RETURN_STEPS):
            x_vals.append(delta_x / Piece_Holder.RETURN_STEPS)
            y_vals.append(delta_y / Piece_Holder.RETURN_STEPS)
        for x in range(delta_x % Piece_Holder.RETURN_STEPS):
            x_vals[x] += 1
        for y in range(delta_y % Piece_Holder.RETURN_STEPS):
            y_vals[y] += 1
        return (x_vals, y_vals)

    def piece_returned(self):
        self.squares[self.moving_piece].returned()
        self.moving_piece = Piece_Holder.DONE_MOVING

class Holder_Square():

    EMPTY = -1

    def __init__(self, square_number, piece_holder):
        self.square_num = square_number
        self.holder = piece_holder
        self.position = ((self.square_num % 2) * 55, ((self.square_num / 2) * 55) + 5)
        self.surface = pygame.Surface((52, 52))
        raw_piece = pygame.image.load("Quarto_Pieces/Piece_"+str(self.square_num)+".png")
        self.primary_piece = pygame.transform.scale(raw_piece, (50, 50))
        self.piece = self.primary_piece
        
    def get_piece(self):
        return self.piece

    def set_piece(self, piece):
        self.piece = piece

    def get_square_surface(self):
        self.surface.fill(WHITE)
        pygame.draw.rect(self.surface, BLACK, (0, 0, 52, 52), 5)
        if (self.piece != Holder_Square.EMPTY):
            self.surface.blit(self.piece, (1, 1))
        return self.surface

    def click_action(self):
        place_holder = self.piece
        self.piece = Holder_Square.EMPTY
        return place_holder

    def returned(self):
        self.piece = self.primary_piece


def move_piece_back():
    pass

my_board = Board((300, 50), 4, 100)
my_piece_holder = Piece_Holder((10, 10), my_board)
dragging_piece = False
piece_moving = False
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
            if(not piece_moving):
                piece_clicked, piece_num = my_piece_holder.check_for_click()
                if (piece_clicked != Piece_Holder.NO_CLICK):
                    dragging_piece = True
        elif(event.type == MOUSEBUTTONUP):
            if(dragging_piece):
                dragging_piece = False
                piece_dropped_on_board = my_board.check_for_mouse(piece_num)
                if(not piece_dropped_on_board):
                    piece_moving = True
                    piece_path = my_piece_holder.put_piece_back(piece_num, pygame.mouse.get_pos())
                    piece_location = pygame.mouse.get_pos()

    if(dragging_piece):
        MAIN_SURF.blit(piece_clicked, pygame.mouse.get_pos())
    elif(piece_moving):
        if(len(piece_path[0]) == 0):
            piece_moving = False
            my_piece_holder.piece_returned()
        else:
            current_change = (piece_path[0].pop(0), piece_path[1].pop(0))
            new_location = (piece_location[0] - current_change[0], piece_location[1] - current_change[1])
            piece_location = new_location
            MAIN_SURF.blit(piece_clicked, piece_location)
    pygame.display.update()
