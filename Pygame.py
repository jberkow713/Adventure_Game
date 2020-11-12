import pygame, sys
import pygame.locals
from pygame.locals import *


#test 1
# mycolor = pygame.Color(255, 0, 0, 128)
# mycolor == (255, 0, 0, 128)


# spamRect = pygame.Rect(10, 20, 250, 350)
# print(spamRect)

# #10 is initial x coordinate, 20 is initial y coordinate,
# # the next value is how far x coordinate goes from 10
# #last value is how far y goes from 20,
# #so it starts a corner at coordinate 10,20, goes to 260,20 top right
# #10, 370 bottom left, 260,370 bottom right
# # spamRect.right = 350

# # ALl values are in tuple form, (x coordinate, y coordinate)
# print(spamRect.bottom)
# print(spamRect.right)
# print(spamRect.bottomright)
# print(spamRect.bottomleft)
# print(spamRect.topleft)
# print(spamRect.topright)
# print(spamRect.center)
# print(spamRect.midright)


#Test2

# pygame.init()

# DISPLAYSURF = pygame.display.set_mode((500, 500),0,32)
# pygame.display.set_caption('Drawing')

# BLACK = ( 0, 0, 0)
# WHITE = (255, 255, 255)
# RED = (255, 0, 0)
# GREEN = ( 0, 255, 0)
# BLUE = ( 0, 0, 255)


# DISPLAYSURF.fill(BLUE)
# #displays points in list of (x, y )  coordinate tuples
# pygame.draw.polygon(DISPLAYSURF, GREEN, ((146, 0), (291, 122), (236, 277),\
#     (56, 277), (32, 297), (0, 106)))
# #draw line with coordinates as listed
# pygame.draw.line(DISPLAYSURF, WHITE, (60, 60), (120, 60), 4)
# pygame.draw.line(DISPLAYSURF, WHITE, (120, 60), (60, 150))
# pygame.draw.line(DISPLAYSURF, WHITE, (60, 120), (120, 120), 4)
# pygame.draw.circle(DISPLAYSURF, WHITE, (300, 50), 20, 0)
# #connect 2 points, use extra variable as color thickness
# pygame.draw.ellipse(DISPLAYSURF, RED, (300, 250, 40, 80), 13)
# pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 100, 50), 13)


# pixObj = pygame.PixelArray(DISPLAYSURF)
# pixObj[480][380] = BLACK
# pixObj[482][382] = BLACK
# pixObj[484][384] = BLACK
# pixObj[486][386] = BLACK
# pixObj[488][388] = BLACK

# del pixObj

# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
#     pygame.display.update()

#test3

pygame.init()
DISPLAYSURF = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Hello World!')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
# 2nd parameter in font is the fontsize
fontObj = pygame.font.Font('freesansbold.ttf', 32)
#render draws text in the font type, first argument is text, 2nd is like making edges nice, 
#3rd is color of text, 4th is background color
textSurfaceObj = fontObj.render('Hello world!', True, WHITE, BLUE)
#creates a rectangle object based on the SIZE of the textsurfaceobject, puts its left and top coordinates at 0,0
textRectObj = textSurfaceObj.get_rect()
#moves objects coordinates to the x,y coordinates specified here
textRectObj.center = (250, 250)

while True:
    #fills surface with Green variable color
    DISPLAYSURF.fill(GREEN)
    # take the image, the hello world image, blit it onto the textRectObj coordinates
    # you then take the hellow world , and the correctly sized rectangle object, and put the text onto the object, 
    # at the proper coordinates

    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
