import pygame, sys
import pygame.locals
from pygame.locals import *
from Player import Player




# pygame.init()
# #Pixel width by pixel height
# BLACK = ( 0, 0, 0)
# WHITE = (255, 255, 255)
# RED = (255, 0, 0)
# GREEN = ( 0, 255, 0)
# BLUE = ( 0, 0, 255)

# WIDTH = 1000
# HEIGHT = 1000
# XMARGIN = 50
# YMARGIN = 50
# Big_Gap = XMARGIN*4
# Small_Gap = XMARGIN*2 
# DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption('You have opened a new pygame window!')

# WHITE = (255, 255, 255)
# DISPLAYSURF.fill(WHITE)
# World 1
# Board = pygame.draw.rect(DISPLAYSURF, (128,255, 255), (XMARGIN, YMARGIN, (WIDTH - 2 * XMARGIN), (HEIGHT-2*YMARGIN)))
# pygame.draw.line(DISPLAYSURF, BLUE, (200, 900), (200, 800), 4)
# pygame.draw.rect(DISPLAYSURF, RED, (150, 700, 100,100))
# pygame.draw.line(DISPLAYSURF, BLUE, (200, 700), (200, 600), 4)
# pygame.draw.rect(DISPLAYSURF, RED, (150, 500, 100,100))
# pygame.draw.line(DISPLAYSURF, BLUE, (250, 750), (350, 750), 4)
# pygame.draw.rect(DISPLAYSURF, RED, (350, 700, 100,100))
# pygame.draw.line(DISPLAYSURF, BLUE, (400, 700), (400, 600), 4)
# pygame.draw.rect(DISPLAYSURF, RED, (350, 500, 100,100))
# pygame.draw.line(DISPLAYSURF, BLUE, (400, 500), (400, 400), 4)
# pygame.draw.rect(DISPLAYSURF, RED, (350, 300, 100,100))
# pygame.draw.line(DISPLAYSURF, BLUE, (450, 350), (550, 350), 4)
# pygame.draw.rect(DISPLAYSURF, RED, (550, 300, 100,100))

# #World 2

# Board = pygame.draw.rect(DISPLAYSURF, (128,255, 255), (XMARGIN, YMARGIN, (WIDTH - 2 * XMARGIN), (HEIGHT-2*YMARGIN)))
# pygame.draw.rect(DISPLAYSURF, RED, (150, 800, 100,100))
# pygame.draw.line(DISPLAYSURF, BLUE, (250, 850), (350, 850), 4)
# pygame.draw.rect(DISPLAYSURF, RED, (350, 800, 100,100))
# pygame.draw.line(DISPLAYSURF, GREEN, (200, 800), (200, 700), 15)
# pygame.draw.rect(DISPLAYSURF, RED, (150, 600, 100,100))
# pygame.draw.line(DISPLAYSURF, BLUE, (250, 650), (350, 650), 4)
# pygame.draw.rect(DISPLAYSURF, RED, (350, 600, 100,100))
# pygame.draw.line(DISPLAYSURF, BLUE, (400, 600), (400, 500), 4)
# pygame.draw.rect(DISPLAYSURF, RED, (350, 400, 100,100))
# pygame.draw.line(DISPLAYSURF, BLUE, (400, 400), (400, 300), 4)
# pygame.draw.rect(DISPLAYSURF, RED, (350, 200, 100,100))
# pygame.draw.line(DISPLAYSURF, BLUE, (400, 200), (400, 100), 4)
# pygame.draw.rect(DISPLAYSURF, RED, (200, 50, 400,50))







# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
#     pygame.display.update()

#The idea:
'''
Put map program inside Adventure.py...so once program starts, open the map window.

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


def Show_Map():

    

    pygame.init()
    BLACK = ( 0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = ( 0, 255, 0)
    BLUE = ( 0, 0, 255)

    WIDTH = 1000
    HEIGHT = 1000
    XMARGIN = 50
    YMARGIN = 50
    Big_Gap = XMARGIN*4
    Small_Gap = XMARGIN*2 
    FPS = .15 # frames per second setting

    if player.room.world == 1:

        fpsClock = pygame.time.Clock()

        DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('You have entered World 1!')

        WHITE = (255, 255, 255)
        DISPLAYSURF.fill(WHITE)
    # World 1
        Board = pygame.draw.rect(DISPLAYSURF, (128,255, 255), (XMARGIN, YMARGIN, (WIDTH - 2 * XMARGIN), (HEIGHT-2*YMARGIN)))
        pygame.draw.line(DISPLAYSURF, BLUE, (200, 900), (200, 800), 4)
        pygame.draw.rect(DISPLAYSURF, RED, (150, 700, 100,100))
        pygame.draw.line(DISPLAYSURF, BLUE, (200, 700), (200, 600), 4)
        pygame.draw.rect(DISPLAYSURF, RED, (150, 500, 100,100))
        pygame.draw.line(DISPLAYSURF, BLUE, (250, 750), (350, 750), 4)
        pygame.draw.rect(DISPLAYSURF, RED, (350, 700, 100,100))
        pygame.draw.line(DISPLAYSURF, BLUE, (400, 700), (400, 600), 4)
        pygame.draw.rect(DISPLAYSURF, RED, (350, 500, 100,100))
        pygame.draw.line(DISPLAYSURF, BLUE, (400, 500), (400, 400), 4)
        pygame.draw.rect(DISPLAYSURF, RED, (350, 300, 100,100))
        pygame.draw.line(DISPLAYSURF, BLUE, (450, 350), (550, 350), 4)
        pygame.draw.rect(DISPLAYSURF, RED, (550, 300, 100,100))
        pygame.display.update()
        fpsClock.tick(FPS)
        pygame.quit()
 
    elif player.room.world == 2:

        fpsClock = pygame.time.Clock()

        DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('You have entered World 2!')

        WHITE = (255, 255, 255)
        DISPLAYSURF.fill(WHITE)

        Board = pygame.draw.rect(DISPLAYSURF, (128,255, 255), (XMARGIN, YMARGIN, (WIDTH - 2 * XMARGIN), (HEIGHT-2*YMARGIN)))
        pygame.draw.rect(DISPLAYSURF, RED, (150, 800, 100,100))
        pygame.draw.line(DISPLAYSURF, BLUE, (250, 850), (350, 850), 4)
        pygame.draw.rect(DISPLAYSURF, RED, (350, 800, 100,100))
        pygame.draw.line(DISPLAYSURF, GREEN, (200, 800), (200, 700), 15)
        pygame.draw.rect(DISPLAYSURF, RED, (150, 600, 100,100))
        pygame.draw.line(DISPLAYSURF, BLUE, (250, 650), (350, 650), 4)
        pygame.draw.rect(DISPLAYSURF, RED, (350, 600, 100,100))
        pygame.draw.line(DISPLAYSURF, BLUE, (400, 600), (400, 500), 4)
        pygame.draw.rect(DISPLAYSURF, RED, (350, 400, 100,100))
        pygame.draw.line(DISPLAYSURF, BLUE, (400, 400), (400, 300), 4)
        pygame.draw.rect(DISPLAYSURF, RED, (350, 200, 100,100))
        pygame.draw.line(DISPLAYSURF, BLUE, (400, 200), (400, 100), 4)
        pygame.draw.rect(DISPLAYSURF, RED, (200, 50, 400,50))
        

        

        

        