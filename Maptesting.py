import pygame, sys
import pygame.locals
from pygame.locals import *

pygame.init()
#Pixel width by pixel height
Display_Surface = pygame.display.set_mode((400, 400))
pygame.display.set_caption('You have opened a new pygame window!')
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()


