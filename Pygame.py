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

# pygame.init()
# DISPLAYSURF = pygame.display.set_mode((500, 500))
# pygame.display.set_caption('Hello World!')

# WHITE = (255, 255, 255)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 128)
# # 2nd parameter in font is the fontsize
# fontObj = pygame.font.Font('freesansbold.ttf', 32)
# #render draws text in the font type, first argument is text, 2nd is like making edges nice, 
# #3rd is color of text, 4th is background color
# textSurfaceObj = fontObj.render('Hello world!', True, WHITE, BLUE)
# #creates a rectangle object based on the SIZE of the textsurfaceobject, puts its left and top coordinates at 0,0
# textRectObj = textSurfaceObj.get_rect()
# #moves objects coordinates to the x,y coordinates specified here
# textRectObj.center = (250, 250)

# while True:
#     #fills surface with Green variable color
#     DISPLAYSURF.fill(GREEN)
#     # take the image, the hello world image, blit it onto the textRectObj coordinates
#     # you then take the hellow world , and the correctly sized rectangle object, and put the text onto the object, 
#     # at the proper coordinates

#     DISPLAYSURF.blit(textSurfaceObj, textRectObj)
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
#     pygame.display.update()



#test 4 Sound
# soundObj = pygame.mixer.Sound('beeps.wav')
# soundObj.play()
# import time
# time.sleep(1) # wait and let the sound play for 1 second
# soundObj.stop()



# soundObj = pygame.mixer.Sound('beepingsound.wav')
# soundObj.play()
# # Loading and playing background music:
# pygame.mixer.music.load(backgroundmusic.mp3)
# pygame.mixer.music.play(-1, 0.0)
# # ...some more of your code goes here...
# pygame.mixer.music.stop()
    
#test 5


# FPS = 30 # frames per second, the general speed of the program
# WINDOWWIDTH = 640 # size of window's width in pixels
# WINDOWHEIGHT = 480 # size of windows' height in pixels
# REVEALSPEED = 8 # speed boxes' sliding reveals and covers
# BOXSIZE = 40 # size of box height & width in pixels
# GAPSIZE = 10 # size of gap between boxes in pixels
# BOARDWIDTH = 10 # number of columns of icons
# BOARDHEIGHT = 7 # number of rows of icons
# assert (BOARDWIDTH * BOARDHEIGHT) % 2 == 0, 'Board needs to have an even # number of boxes for pairs of matches.'
# XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)
# YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)

#  # R G B
# GRAY = (100, 100, 100)
# NAVYBLUE = ( 60, 60, 100)
# WHITE = (255, 255, 255)
# RED = (255, 0, 0)
# GREEN = ( 0, 255, 0)
# BLUE = ( 0, 0, 255)
# YELLOW = (255, 255, 0)
# ORANGE = (255, 128, 0)
# PURPLE = (255, 0, 255)
# CYAN = ( 0, 255, 255)

# BGCOLOR = NAVYBLUE
# LIGHTBGCOLOR = GRAY
# BOXCOLOR = WHITE
# HIGHLIGHTCOLOR = BLUE

# DONUT = 'donut'

# SQUARE = 'square'
# DIAMOND = 'diamond'
# LINES = 'lines'
# OVAL = 'oval'

# ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
# ALLSHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)
# assert len(ALLCOLORS) * len(ALLSHAPES) * 2 >= BOARDWIDTH * BOARDHEIGHT,

# # "Board is too big for the number of shapes/colors defined."

# def main():
#     global FPSCLOCK, DISPLAYSURF
#     pygame.init()
#     FPSCLOCK = pygame.time.Clock()
#     DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

#     mousex = 0 # used to store x coordinate of mouse event
#     mousey = 0 # used to store y coordinate of mouse event
#     pygame.display.set_caption('Memory Game')

#     mainBoard = getRandomizedBoard()
#     revealedBoxes = generateRevealedBoxesData(False)

#     firstSelection = None # stores the (x, y) of the first box clicked.

#     DISPLAYSURF.fill(BGCOLOR)
#     startGameAnimation(mainBoard)

#     while True: # main game loop
#         mouseClicked = False

#         DISPLAYSURF.fill(BGCOLOR) # drawing the window
#         drawBoard(mainBoard, revealedBoxes)

#         for event in pygame.event.get(): # event handling loop
#             if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
#                 pygame.quit()
#                 sys.exit()
#             elif event.type == MOUSEMOTION:
#                 mousex, mousey = event.pos
#             elif event.type == MOUSEBUTTONUP:
#                 mousex, mousey = event.pos
#                 mouseClicked = True

#                 boxx, boxy = getBoxAtPixel(mousex, mousey)

#             if boxx != None and boxy != None:
#  # The mouse is currently over a box.
#                 if not revealedBoxes[boxx][boxy]:
#                     drawHighlightBox(boxx, boxy)
#                 if not revealedBoxes[boxx][boxy] and mouseClicked:
#                     revealBoxesAnimation(mainBoard, [(boxx, boxy)])
#                     revealedBoxes[boxx][boxy] = True # set the box as
# # "revealed"
# if firstSelection == None: # the current box was the first
# box clicked
# firstSelection = (boxx, boxy)
# else: # the current box was the second box clicked
#  # Check if there is a match between the two icons.
# icon1shape, icon1color = getShapeAndColor(mainBoard, firstSelection[0], firstSelection[1])
# icon2shape, icon2color = getShapeAndColor(mainBoard, boxx, boxy)

# 97. if icon1shape != icon2shape or icon1color !=
# icon2color:
# 98. # Icons don't match. Re-cover up both selections.
# 99. pygame.time.wait(1000) # 1000 milliseconds = 1 sec
# 100. coverBoxesAnimation(mainBoard,
# [(firstSelection[0], firstSelection[1]), (boxx, boxy)])
# 101. revealedBoxes[firstSelection[0]][firstSelection
# [1]] = False
# 102. revealedBoxes[boxx][boxy] = False
# 103. elif hasWon(revealedBoxes): # check if all pairs found
# 104. gameWonAnimation(mainBoard)
# 105. pygame.time.wait(2000)
# 106.
# 107. # Reset the board
# 108. mainBoard = getRandomizedBoard()
# 109. revealedBoxes = generateRevealedBoxesData(False)
# 110.
# 111. # Show the fully unrevealed board for a second.
# 112. drawBoard(mainBoard, revealedBoxes)
# 113. pygame.display.update()
# 114. pygame.time.wait(1000)
# 115.
# 116. # Replay the start game animation.
# 117. startGameAnimation(mainBoard)
# 118. firstSelection = None # reset firstSelection variable
# 119.
# 120. # Redraw the screen and wait a clock tick.
# 121. pygame.display.update()
# 38 http://inventwithpython.com/pygame
# Email questions to the author: al@inventwithpython.com
# 122. FPSCLOCK.tick(FPS)
# 123.
# 124.
# 125. def generateRevealedBoxesData(val):
# 126. revealedBoxes = []
# 127. for i in range(BOARDWIDTH):
# 128. revealedBoxes.append([val] * BOARDHEIGHT)
# 129. return revealedBoxes
# 130.
# 131.
# 132. def getRandomizedBoard():
# 133. # Get a list of every possible shape in every possible color.
# 134. icons = []
# 135. for color in ALLCOLORS:
# 136. for shape in ALLSHAPES:
# 137. icons.append( (shape, color) )
# 138.
# 139. random.shuffle(icons) # randomize the order of the icons list
# 140. numIconsUsed = int(BOARDWIDTH * BOARDHEIGHT / 2) # calculate how many
# icons are needed
# 141. icons = icons[:numIconsUsed] * 2 # make two of each
# 142. random.shuffle(icons)
# 143.
# 144. # Create the board data structure, with randomly placed icons.
# 145. board = []
# 146. for x in range(BOARDWIDTH):
# 147. column = []
# 148. for y in range(BOARDHEIGHT):
# 149. column.append(icons[0])
# 150. del icons[0] # remove the icons as we assign them
# 151. board.append(column)
# 152. return board
# 153.
# 154.
# 155. def splitIntoGroupsOf(groupSize, theList):
# 156. # splits a list into a list of lists, where the inner lists have at
# 157. # most groupSize number of items.
# 158. result = []
# 159. for i in range(0, len(theList), groupSize):
# 160. result.append(theList[i:i + groupSize])
# 161. return result
# 162.
# 163.
# 164. def leftTopCoordsOfBox(boxx, boxy):
# 165. # Convert board coordinates to pixel coordinates
# 166. left = boxx * (BOXSIZE + GAPSIZE) + XMARGIN
# Chapter 3 – Memory Puzzle 39
# 167. top = boxy * (BOXSIZE + GAPSIZE) + YMARGIN
# 168. return (left, top)
# 169.
# 170.
# 171. def getBoxAtPixel(x, y):
# 172. for boxx in range(BOARDWIDTH):
# 173. for boxy in range(BOARDHEIGHT):
# 174. left, top = leftTopCoordsOfBox(boxx, boxy)
# 175. boxRect = pygame.Rect(left, top, BOXSIZE, BOXSIZE)
# 176. if boxRect.collidepoint(x, y):
# 177. return (boxx, boxy)
# 178. return (None, None)
# 179.
# 180.
# 181. def drawIcon(shape, color, boxx, boxy):
# 182. quarter = int(BOXSIZE * 0.25) # syntactic sugar
# 183. half = int(BOXSIZE * 0.5) # syntactic sugar
# 184.
# 185. left, top = leftTopCoordsOfBox(boxx, boxy) # get pixel coords from
# board coords
# 186. # Draw the shapes
# 187. if shape == DONUT:
# 188. pygame.draw.circle(DISPLAYSURF, color, (left + half, top + half),
# half - 5)
# 189. pygame.draw.circle(DISPLAYSURF, BGCOLOR, (left + half, top +
# half), quarter - 5)
# 190. elif shape == SQUARE:
# 191. pygame.draw.rect(DISPLAYSURF, color, (left + quarter, top +
# quarter, BOXSIZE - half, BOXSIZE - half))
# 192. elif shape == DIAMOND:
# 193. pygame.draw.polygon(DISPLAYSURF, color, ((left + half, top), (left
# + BOXSIZE - 1, top + half), (left + half, top + BOXSIZE - 1), (left, top +
# half)))
# 194. elif shape == LINES:
# 195. for i in range(0, BOXSIZE, 4):
# 196. pygame.draw.line(DISPLAYSURF, color, (left, top + i), (left +
# i, top))
# 197. pygame.draw.line(DISPLAYSURF, color, (left + i, top + BOXSIZE
# - 1), (left + BOXSIZE - 1, top + i))
# 198. elif shape == OVAL:
# 199. pygame.draw.ellipse(DISPLAYSURF, color, (left, top + quarter,
# BOXSIZE, half))
# 200.
# 201.
# 202. def getShapeAndColor(board, boxx, boxy):
# 203. # shape value for x, y spot is stored in board[x][y][0]
# 40 http://inventwithpython.com/pygame
# Email questions to the author: al@inventwithpython.com
# 204. # color value for x, y spot is stored in board[x][y][1]
# 205. return board[boxx][boxy][0], board[boxx][boxy][1]
# 206.
# 207.
# 208. def drawBoxCovers(board, boxes, coverage):
# 209. # Draws boxes being covered/revealed. "boxes" is a list
# 210. # of two-item lists, which have the x & y spot of the box.
# 211. for box in boxes:
# 212. left, top = leftTopCoordsOfBox(box[0], box[1])
# 213. pygame.draw.rect(DISPLAYSURF, BGCOLOR, (left, top, BOXSIZE,
# BOXSIZE))
# 214. shape, color = getShapeAndColor(board, box[0], box[1])
# 215. drawIcon(shape, color, box[0], box[1])
# 216. if coverage > 0: # only draw the cover if there is an coverage
# 217. pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, coverage,
# BOXSIZE))
# 218. pygame.display.update()
# 219. FPSCLOCK.tick(FPS)
# 220.
# 221.
# 222. def revealBoxesAnimation(board, boxesToReveal):
# 223. # Do the "box reveal" animation.
# 224. for coverage in range(BOXSIZE, (-REVEALSPEED) - 1, - REVEALSPEED):
# 225. drawBoxCovers(board, boxesToReveal, coverage)
# 226.
# 227.
# 228. def coverBoxesAnimation(board, boxesToCover):
# 229. # Do the "box cover" animation.
# 230. for coverage in range(0, BOXSIZE + REVEALSPEED, REVEALSPEED):
# 231. drawBoxCovers(board, boxesToCover, coverage)
# 232.
# 233.
# 234. def drawBoard(board, revealed):
# 235. # Draws all of the boxes in their covered or revealed state.
# 236. for boxx in range(BOARDWIDTH):
# 237. for boxy in range(BOARDHEIGHT):
# 238. left, top = leftTopCoordsOfBox(boxx, boxy)
# 239. if not revealed[boxx][boxy]:
# 240. # Draw a covered box.
# 241. pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top,
# BOXSIZE, BOXSIZE))
# 242. else:
# 243. # Draw the (revealed) icon.
# 244. shape, color = getShapeAndColor(board, boxx, boxy)
# 245. drawIcon(shape, color, boxx, boxy)
# 246. 
# Chapter 3 – Memory Puzzle 41
# 247.
# 248. def drawHighlightBox(boxx, boxy):
# 249. left, top = leftTopCoordsOfBox(boxx, boxy)
# 250. pygame.draw.rect(DISPLAYSURF, HIGHLIGHTCOLOR, (left - 5, top - 5,
# BOXSIZE + 10, BOXSIZE + 10), 4)
# 251.
# 252.
# 253. def startGameAnimation(board):
# 254. # Randomly reveal the boxes 8 at a time.
# 255. coveredBoxes = generateRevealedBoxesData(False)
# 256. boxes = []
# 257. for x in range(BOARDWIDTH):
# 258. for y in range(BOARDHEIGHT):
# 259. boxes.append( (x, y) )
# 260. random.shuffle(boxes)
# 261. boxGroups = splitIntoGroupsOf(8, boxes)
# 262.
# 263. drawBoard(board, coveredBoxes)
# 264. for boxGroup in boxGroups:
# 265. revealBoxesAnimation(board, boxGroup)
# 266. coverBoxesAnimation(board, boxGroup)
# 267.
# 268.
# 269. def gameWonAnimation(board):
# 270. # flash the background color when the player has won
# 271. coveredBoxes = generateRevealedBoxesData(True)
# 272. color1 = LIGHTBGCOLOR
# 273. color2 = BGCOLOR
# 274.
# 275. for i in range(13):
# 276. color1, color2 = color2, color1 # swap colors
# 277. DISPLAYSURF.fill(color1)
# 278. drawBoard(board, coveredBoxes)
# 279. pygame.display.update()
# 280. pygame.time.wait(300)
# 281.
# 282.
# 283. def hasWon(revealedBoxes):
# 284. # Returns True if all the boxes have been revealed, otherwise False
# 285. for i in revealedBoxes:
# 286. if False in i:
# 287. return False # return False if any boxes are covered.
# 288. return True
# 289.
# 290.
# 291. if __name__ == '__main__':
# 42 http://inventwithpython.com/pygame
# Email questions to the author: al@inventwithpython.com
# 292. main()


#test 6

import random 
import time

FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
FLASHSPEED = 500 # in milliseconds
FLASHDELAY = 200 # in milliseconds
BUTTONSIZE = 200
BUTTONGAPSIZE = 20
TIMEOUT = 4 # seconds before game over if no button is pushed.

#                R    G    B
WHITE        = (255, 255, 255)
BLACK        = (  0,   0,   0)
BRIGHTRED    = (255,   0,   0)
RED          = (155,   0,   0)
BRIGHTGREEN  = (  0, 255,   0)
GREEN        = (  0, 155,   0)
BRIGHTBLUE   = (  0,   0, 255)
BLUE         = (  0,   0, 155)
BRIGHTYELLOW = (255, 255,   0)
YELLOW       = (155, 155,   0)
DARKGRAY     = ( 40,  40,  40)
bgColor = BLACK

XMARGIN = int((WINDOWWIDTH - (2 * BUTTONSIZE) - BUTTONGAPSIZE) / 2)
YMARGIN = int((WINDOWHEIGHT - (2 * BUTTONSIZE) - BUTTONGAPSIZE) / 2)

# Rect objects for each of the four buttons
YELLOWRECT = pygame.Rect(XMARGIN, YMARGIN, BUTTONSIZE, BUTTONSIZE)
BLUERECT   = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN, BUTTONSIZE, BUTTONSIZE)
REDRECT    = pygame.Rect(XMARGIN, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)
GREENRECT  = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, BEEP1, BEEP2, BEEP3, BEEP4

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Simulate')

    BASICFONT = pygame.font.Font('freesansbold.ttf', 16)
    infoSurf = BASICFONT.render('Match the pattern by clicking on the button or using the Q, W, A, S keys.', 1, DARKGRAY)
    infoRect = infoSurf.get_rect()
    infoRect.topleft = (10, WINDOWHEIGHT - 25)

    # load the sound files
    BEEP1 = pygame.mixer.Sound('beep1.ogg')
    BEEP2 = pygame.mixer.Sound('beep2.ogg')
    BEEP3 = pygame.mixer.Sound('beep3.ogg')
    BEEP4 = pygame.mixer.Sound('beep4.ogg')

    # Initialize some variables for a new game
    pattern = [] # stores the pattern of colors
    currentStep = 0 # the color the player must push next
    lastClickTime = 0 # timestamp of the player's last button push
    score = 0
    # when False, the pattern is playing. when True, waiting for the player to click a colored button:
    waitingForInput = False

    while True: # main game loop
        clickedButton = None # button that was clicked (set to YELLOW, RED, GREEN, or BLUE)
        DISPLAYSURF.fill(bgColor)
        drawButtons()

        scoreSurf = BASICFONT.render('Score: ' + str(score), 1, WHITE)
        scoreRect = scoreSurf.get_rect()
        scoreRect.topleft = (WINDOWWIDTH - 100, 10)
        DISPLAYSURF.blit(scoreSurf, scoreRect)

        DISPLAYSURF.blit(infoSurf, infoRect)

        checkForQuit()
        for event in pygame.event.get(): # event handling loop
            if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                clickedButton = getButtonClicked(mousex, mousey)
            elif event.type == KEYDOWN:
                if event.key == K_q:
                    clickedButton = YELLOW
                elif event.key == K_w:
                    clickedButton = BLUE
                elif event.key == K_a:
                    clickedButton = RED
                elif event.key == K_s:
                    clickedButton = GREEN



        if not waitingForInput:
            # play the pattern
            pygame.display.update()
            pygame.time.wait(1000)
            pattern.append(random.choice((YELLOW, BLUE, RED, GREEN)))
            for button in pattern:
                flashButtonAnimation(button)
                pygame.time.wait(FLASHDELAY)
            waitingForInput = True
        else:
            # wait for the player to enter buttons
            if clickedButton and clickedButton == pattern[currentStep]:
                # pushed the correct button
                flashButtonAnimation(clickedButton)
                currentStep += 1
                lastClickTime = time.time()

                if currentStep == len(pattern):
                    # pushed the last button in the pattern
                    changeBackgroundAnimation()
                    score += 1
                    waitingForInput = False
                    currentStep = 0 # reset back to first step

            elif (clickedButton and clickedButton != pattern[currentStep]) or (currentStep != 0 and time.time() - TIMEOUT > lastClickTime):
                # pushed the incorrect button, or has timed out
                gameOverAnimation()
                # reset the variables for a new game:
                pattern = []
                currentStep = 0
                waitingForInput = False
                score = 0
                pygame.time.wait(1000)
                changeBackgroundAnimation()

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def terminate():
    pygame.quit()
    sys.exit()


def checkForQuit():
    for event in pygame.event.get(QUIT): # get all the QUIT events
        terminate() # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate() # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event) # put the other KEYUP event objects back


def flashButtonAnimation(color, animationSpeed=50):
    if color == YELLOW:
        sound = BEEP1
        flashColor = BRIGHTYELLOW
        rectangle = YELLOWRECT
    elif color == BLUE:
        sound = BEEP2
        flashColor = BRIGHTBLUE
        rectangle = BLUERECT
    elif color == RED:
        sound = BEEP3
        flashColor = BRIGHTRED
        rectangle = REDRECT
    elif color == GREEN:
        sound = BEEP4
        flashColor = BRIGHTGREEN
        rectangle = GREENRECT

    origSurf = DISPLAYSURF.copy()
    flashSurf = pygame.Surface((BUTTONSIZE, BUTTONSIZE))
    flashSurf = flashSurf.convert_alpha()
    r, g, b = flashColor
    sound.play()
    for start, end, step in ((0, 255, 1), (255, 0, -1)): # animation loop
        for alpha in range(start, end, animationSpeed * step):
            checkForQuit()
            DISPLAYSURF.blit(origSurf, (0, 0))
            flashSurf.fill((r, g, b, alpha))
            DISPLAYSURF.blit(flashSurf, rectangle.topleft)
            pygame.display.update()
            FPSCLOCK.tick(FPS)
    DISPLAYSURF.blit(origSurf, (0, 0))


def drawButtons():
    pygame.draw.rect(DISPLAYSURF, YELLOW, YELLOWRECT)
    pygame.draw.rect(DISPLAYSURF, BLUE,   BLUERECT)
    pygame.draw.rect(DISPLAYSURF, RED,    REDRECT)
    pygame.draw.rect(DISPLAYSURF, GREEN,  GREENRECT)


def changeBackgroundAnimation(animationSpeed=40):
    global bgColor
    newBgColor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    newBgSurf = pygame.Surface((WINDOWWIDTH, WINDOWHEIGHT))
    newBgSurf = newBgSurf.convert_alpha()
    r, g, b = newBgColor
    for alpha in range(0, 255, animationSpeed): # animation loop
        checkForQuit()
        DISPLAYSURF.fill(bgColor)

        newBgSurf.fill((r, g, b, alpha))
        DISPLAYSURF.blit(newBgSurf, (0, 0))

        drawButtons() # redraw the buttons on top of the tint

        pygame.display.update()
        FPSCLOCK.tick(FPS)
    bgColor = newBgColor


def gameOverAnimation(color=WHITE, animationSpeed=50):
    # play all beeps at once, then flash the background
    origSurf = DISPLAYSURF.copy()
    flashSurf = pygame.Surface(DISPLAYSURF.get_size())
    flashSurf = flashSurf.convert_alpha()
    BEEP1.play() # play all four beeps at the same time, roughly.
    BEEP2.play()
    BEEP3.play()
    BEEP4.play()
    r, g, b = color
    for i in range(3): # do the flash 3 times
        for start, end, step in ((0, 255, 1), (255, 0, -1)):
            # The first iteration in this loop sets the following for loop
            # to go from 0 to 255, the second from 255 to 0.
            for alpha in range(start, end, animationSpeed * step): # animation loop
                # alpha means transparency. 255 is opaque, 0 is invisible
                checkForQuit()
                flashSurf.fill((r, g, b, alpha))
                DISPLAYSURF.blit(origSurf, (0, 0))
                DISPLAYSURF.blit(flashSurf, (0, 0))
                drawButtons()
                pygame.display.update()
                FPSCLOCK.tick(FPS)



def getButtonClicked(x, y):
    if YELLOWRECT.collidepoint( (x, y) ):
        return YELLOW
    elif BLUERECT.collidepoint( (x, y) ):
        return BLUE
    elif REDRECT.collidepoint( (x, y) ):
        return RED
    elif GREENRECT.collidepoint( (x, y) ):
        return GREEN
    return None


if __name__ == '__main__':
    main()


