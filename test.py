import pygame, sys
from pygame.locals import *
import pygame.examples.glcube

pygame.init()
MAIN_SURF = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Quarto')

while True: # main game loop
    pygame.examples.glcube.main()
    
    for event in pygame.event.get():
        if(event.type == QUIT):
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
