x = 750
y = 0
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
import pygame, sys
import pygame.locals
from pygame.locals import *
from Player import Player

import getpass
from texttest import text_box



# import pygame
# pygame.init()
# screen = pygame.display.set_mode((100,100))

# # wait for a while to show the window.
# import time
# time.sleep(2)



def World1draw(FPS):
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
       
    
    pygame.init() 
        
    DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('YOU ARE CURRENTLY IN WORLD 1')
    DISPLAYSURF.fill(WHITE)
    
    Board = pygame.draw.rect(DISPLAYSURF, (128,255, 255), (XMARGIN, YMARGIN, (WIDTH - 2 * XMARGIN), (HEIGHT-2*YMARGIN)))
    
    pygame.draw.rect(DISPLAYSURF, RED, (150, 900, 100,50))
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

    
    fontObj = pygame.font.Font('freesansbold.ttf', 16)
    fontObj2 = pygame.font.Font('freesansbold.ttf', 14)
    Room1 = fontObj.render('FOYER', True, BLACK, RED)
    Room2 = fontObj.render('OVERLOOK', True, BLACK, RED)
    Room3 = fontObj.render('NARROW', True, BLACK, RED)
    Room3a = fontObj.render('PASSAGE', True, BLACK, RED)
    Room4 = fontObj.render('TREASURE', True, BLACK, RED)
    Room4a = fontObj.render('ROOM', True, BLACK, RED)
    Room5 = fontObj.render('CAVE EXIT', True, BLACK, RED)
    Room6 = fontObj2.render('ENCHANTED', True, BLACK, RED)
    Room6a = fontObj2.render('FOREST', True, BLACK, RED)
    Room7 = fontObj2.render('OUTSIDE', True, BLACK, RED)
    
    DISPLAYSURF.blit(Room7, (170, 920))
    DISPLAYSURF.blit(Room1, (170, 740))
    DISPLAYSURF.blit(Room2, (155, 540))
    DISPLAYSURF.blit(Room3, (365, 730))
    DISPLAYSURF.blit(Room3a, (365, 745))
    DISPLAYSURF.blit(Room4, (355, 530))
    DISPLAYSURF.blit(Room4a, (370, 545))
    DISPLAYSURF.blit(Room5, (355, 340))
    DISPLAYSURF.blit(Room6, (555, 330))
    DISPLAYSURF.blit(Room6a, (570, 345)) 
    
                        
    pygame.display.update() 
    
    fpsClock = pygame.time.Clock()
    fpsClock.tick(FPS)
    
    # Room1 = fontObj.render('FOYER', True, BLACK, GREEN)
    
    pygame.quit()
    
# World1draw(.2)

def World2draw(FPS):

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

    pygame.init() 
    DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('YOU ARE CURRENTLY IN WORLD 2!')
    DISPLAYSURF.fill(WHITE)

    Board = pygame.draw.rect(DISPLAYSURF, (128,255, 255), (XMARGIN, YMARGIN, (WIDTH - 2 * XMARGIN), (HEIGHT-2*YMARGIN)))
    pygame.draw.rect(DISPLAYSURF, RED, (150, 800, 100,100))
    pygame.draw.line(DISPLAYSURF, BLUE, (250, 850), (350, 850), 4)
    pygame.draw.rect(DISPLAYSURF, RED, (350, 800, 100,100))
    pygame.draw.line(DISPLAYSURF, BLUE, (200, 800), (200, 700), 4)
    pygame.draw.rect(DISPLAYSURF, RED, (150, 400, 100,100))
    pygame.draw.line(DISPLAYSURF, GREEN, (200, 600), (200, 500), 15)
    pygame.draw.rect(DISPLAYSURF, RED, (150, 600, 100,100))
    pygame.draw.line(DISPLAYSURF, BLUE, (250, 450), (350, 450), 4)
    pygame.draw.rect(DISPLAYSURF, RED, (350, 400, 100,100))
    pygame.draw.line(DISPLAYSURF, BLUE, (400, 400), (400, 300), 4)
    pygame.draw.rect(DISPLAYSURF, RED, (350, 200, 100,100))
    pygame.draw.line(DISPLAYSURF, BLUE, (400, 200), (400, 100), 4)
    pygame.draw.rect(DISPLAYSURF, RED, (200, 50, 400,50))

    fontObj = pygame.font.Font('freesansbold.ttf', 16)
    fontObj2 = pygame.font.Font('freesansbold.ttf', 14)


    Room1 = fontObj.render('MAGICAL', True, BLACK, RED)
    Room1a = fontObj.render('ENTRANCE', True, BLACK, RED)
    Room1b = fontObj.render("WIZARD'S", True, BLACK, RED)
    Room1c = fontObj.render('LAIR', True, BLACK, RED)
    Room2 = fontObj.render('CAULDRON', True, BLACK, RED)
    Room2a = fontObj.render('ROOM', True, BLACK, RED)
    Room3 = fontObj.render('CLOUD', True, BLACK, RED)
    Room3a = fontObj.render('FORTRESS', True, BLACK, RED)
    Room4 = fontObj2.render('MYSTERIOUS', True, BLACK, RED)
    Room4a = fontObj2.render('SHACK', True, BLACK, RED)
    Room6 = fontObj.render('OGRE', True, BLACK, RED)
    Room6a = fontObj.render('FORTRESS', True, BLACK, RED)
    Room7 = fontObj.render("OGRE KING'S LAIR", True, BLACK, RED)


    DISPLAYSURF.blit(Room1, (160, 830))
    DISPLAYSURF.blit(Room1a, (151, 850))
    DISPLAYSURF.blit(Room1b, (360, 830))
    DISPLAYSURF.blit(Room1c, (380, 850))
    DISPLAYSURF.blit(Room2, (152, 630))
    DISPLAYSURF.blit(Room2a, (180, 650))
    DISPLAYSURF.blit(Room3, (175, 430))
    DISPLAYSURF.blit(Room3a, (156, 450))
    DISPLAYSURF.blit(Room4, (355, 430))
    DISPLAYSURF.blit(Room4a, (374, 450))
    DISPLAYSURF.blit(Room6, (376, 230))
    DISPLAYSURF.blit(Room6a, (356, 250))
    DISPLAYSURF.blit(Room7, (325, 60))


    pygame.display.update() 
        
    fpsClock = pygame.time.Clock()
    fpsClock.tick(FPS)
        
    pygame.quit()

def Choose_Map_Speed():

    choices = ["1", "2", "3", "4"]
    
    Choices = False
    while Choices == False:

        text_box("The higher the map display setting value, the longer the map will display", 2)      
        #Getpass makes it so this input is not displayed
        Map_speed = getpass.getpass("Please choose 1,2,3, or 4 for Map Display Settings \n\n")
        if Map_speed == 'q':
            Map_quit = True
            break
        elif Map_speed not in choices:
            print("That is not a valid speed")
        elif Map_speed in choices:
            Choices = True
    
    Speeds = [.33, .2, .15, .05]
    path_dict = dict(zip(choices, Speeds))

    for key, value in path_dict.items():
        if Map_speed == key:
            FPS = value
    
    return(FPS) 

# Map_speed = Choose_Map_Speed()

# World1draw(Map_speed)

#so we need player's room, and we need the starting coordinates of that room,
# and we need the direction the player has selected, to alter the position of link, 
# based on starting coordinates...
# so if starting coordinates = 200,500:
# if direction = north, blit on 250,500
# if direction or (users_choice) = south, then blit on 250,600,
# if diretion = east, blit on 300, 550,
# if direction = west, blit on 200, 550, 
# if the room is cauldron room and chooses fly, blit on north path,
# if the room is cloud fortress and chooses fly, blit on south path

# so general idea, coordinates (x, y)
# north, blit on (x+50, y)
# south, blit on (x+50, y+100)
# east, blit on (x+100, y+50)
#west, blit on (x, y+50)

# so we need to check players room , like if it equals Foyer, starting coords = x, y
# then it checks if users_choice = whatever, blit link at the corresponding coordinates, and walk him certain 
#way, there will be 4 if , elif statements, one for each direction
#fly case will have to be written separately

#could make a dictionary, where each room name is a key, and each value corresponds to list of x, y coordinates,
# then check to see if player.room.name = key in dictionary, players coordinates = value[0], value[1]
# then adjust the value based on north, west, east, south, 
# player_coords can be the value from the dictionary, corresponding to the room, so a 
# list representing [x-coord value, y-coord value], so based on the direction, do stuff to values in list
#if north, list[0]= list[0]+50, list[1] = list[1]...
#append the new values to a new list, to get links (starting coordinates)
# if south, east, west, etc

#then you need some sort of loop that walks him maybe 10 coordinate along x or y axis at a time, till he reaches
# his final destination, each will be 100 in length total, then you exit the loop, so youre sort of blitting him
# onto 10 different spots, starting at the (starting coordinates) and going in the direction
# when he hits the end of the while loop, you exit the pygame window

# so make the function the same for world 1 and world 2, you just have one giant dictionary of all the rooms
# when you run the function inside world 1, it will only pick up coordinates for names of rooms in world 1, 
# and same for world 2, so function will be exactly the same for each world, aside from flying directions

