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

    def __init__(self, position, text, check=False, color=BLACK,
                 size=50, text_size=16):
        #Initialize main variables
        self.position = position
        self.color = color
        self.size = size
        self.checked = check

        #Create text and text surface
        button_font = pygame.font.Font('freesansbold.ttf', text_size)
        self.text_surface = button_font.render(text, True, self.color)
        text_rect = self.text_surface.get_rect()

        #Create button surface and draw rectangles
        self.button_surface = pygame.Surface((size, size))
        pygame.draw.rect(self.button_surface, self.color,
                         self.button_surface.get_rect(), 3)
        self.checked_rect = self.button_surface.get_rect()
        self.checked_rect.inflate_ip(-10, -10)
        if(self.checked):
            pygame.draw.rect(self.button_surface, self.color, self.checked_rect)

        #Create main checkbox surface
        #Both text surface and button surface will be blitted here
        surface_width = self.size + 5 + text_rect.width
        surface_height = max(self.size, text_rect.height)
        self.surface = pygame.Surface((surface_width, surface_height))
        self.rect = self.surface.get_rect()
        self.rect.topleft = self.position

        self.update_surface()
        

    def check_for_click(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.click_action()
            return True
        else:
            return False

    def update_surface(self):
        self.surface.fill(WHITE)
        self.button_surface.fill(WHITE)
        #Redraw button rects
        pygame.draw.rect(self.button_surface, self.color,
                         self.button_surface.get_rect(), 3)
        if(self.checked):
            pygame.draw.rect(self.button_surface, self.color, self.checked_rect)
        self.surface.blit(self.button_surface, (0, 0))

        #do some math and redraw text
        rect = self.surface.get_rect()
        y = rect.centery
        y -= ((self.text_surface.get_rect()).height)/2
        self.surface.blit(self.text_surface, (self.size + 5, y))
        

    def get_surface(self):
        return self.surface

    def click_action(self):
        self.checked = not self.checked
        self.update_surface()
        MAIN_SURF.blit(self.surface, self.position)

    def draw_surface(self):
        MAIN_SURF.blit(self.surface, self.position)

check_boxes = []
colors = [BLACK, GREEN, BLUE, YELLOW, RED]
for x in range(6):
    check_boxes.append(Checkbox((50, 50 + (x * 75)), "Box "+str(x+1),
                                check=False, color=colors[x%5], text_size=32))

while True: # main game loop
    MAIN_SURF.fill(WHITE)
    for event in pygame.event.get():
        if(event.type == QUIT):
            pygame.quit()
            sys.exit()
        elif (event.type == KEYDOWN):
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        elif (event.type == MOUSEBUTTONDOWN):
            for box in check_boxes:
                box.check_for_click()

    for box in check_boxes:
        box.draw_surface()
    pygame.display.update()
