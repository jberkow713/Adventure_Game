import pygame, sys
import pygame.locals
from pygame.locals import *

pygame.init()
#Pixel width by pixel height
WIDTH = 1000
HEIGHT = 1000
XMARGIN = 50
YMARGIN = 50
Display_Surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('You have opened a new pygame window!')

WHITE = (255, 255, 255)
Display_Surface.fill(WHITE)
Board = pygame.draw.rect(Display_Surface, (128,255, 255), (XMARGIN, YMARGIN, (WIDTH - 2 * XMARGIN), (HEIGHT-2*YMARGIN)))



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

#The idea:
'''
Open 2 consoles when you enter the Adventure game. One is for the input commands, picking up items, directions, etc..
One is for showing where the player is on the map.
The map will be an infinite Pygame loop, and each world will be written out and created in pygame, so that when you enter a 
new world, in the case of this game, basically it means when you use magic as a direction,
the map will clear and the new world map will load. 
So the player will always be at the position of where he or she is on the map...
So the player moves along the map, when some key command is triggered, such as the Users_choice command, which is a 
directional command in the Adventure game. 

For the pygame, I have to create each map separately, which I can test. Each map will consist of rooms, that fit on the grid,
and in between the rooms, the player will follow a specific line, N, S, E, W, Fly(special color line maybe...),
So I will load some image, maybe LINK, and blit him to a specific part of the starting map. 
Everytime a command is triggered, Link will move along a specific line, from one room to another.
However, the player will only move in Pygame, if he is able to move in the actual game, meaning there has to be a link 
between the rooms...so I need another trigger that first says something like "You have entered a valid direction, you move "x",
and that trigger, will trigger Link to move in Pygame. That way, he can only move between valid rooms.

This is the general idea, and I can work from here
'''



