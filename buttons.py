import pygame, sys
from pygame.locals import *

pygame.init()
MAIN_SURF = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Buttons!')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
YELLOW = (153, 153, 0)
RED = (255, 0, 0)

class Checkbox():

    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

    def __init__(self, position, text, text_position=Chekcbox.RIGHT,
                 color=BLACK, size=50, text_clickable=True, text_size=16):
        self.position = position
        self.text = text
        self.text_position = text_position
        self.color = color
        self.size = size
        self.text_clickable = text_clickable
        self.text_size = text_size
        
        button_font = pygame.font.Font('freesansbold.ttf', self.text_size)
        self.button_text_surface = button_font.render(self.text, True, self.color)
        button_text_rect = self.button_text_surface.get_rect()

        surface_width = self.size + 5 + button_text_rect.width
        surface_height = max(self.size, button_text_rect.height)
        self.surface = pygame.Surface((surface_width, surface_height))
        self.rect = self.surface.get_rect()
        self.rect.topleft = self.position
        

    def check_for_click(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return True
        else:
            return False

    def update_surface(self):
        self.surface.fill(WHITE)
        rect = self.surface.get_rect()
        y = rect.centery
        

    def get_surface(self):
        pass

    def click_action(self):
        self.update_surface()
        MAIN_SURF.blit(self.surface, self.position)

while True: # main game loop
    MAIN_SURF.fill(WHITE)
    for event in pygame.event.get():
        if(event.type == QUIT):
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    pygame.display.update()
