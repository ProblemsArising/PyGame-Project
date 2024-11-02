# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
displaySizeX = (1280)
displaySizeY = (720)
screen = pygame.display.set_mode((displaySizeX,displaySizeY))
running = True

# Title & Icon
pygame.display.set_caption('IDK')
icon = pygame.image.load('Rose.png') #Best to use 32*32
pygame.display.set_icon(icon)

# Player 1
p1IMG = pygame.image.load('Player1.png')
p1X = int(displaySizeX-96)/2
p1Y = int(displaySizeY-96)/2
p1Xchange = 0
p1Ychange = 0

def player1(x, y):
    screen.blit(p1IMG, (x, y))

# Player 2
p2IMG = pygame.image.load('Player2.png')
p2X = int(displaySizeX-96)/2
p2Y = int(displaySizeY-96)/2
p2Xchange = 0
p2Ychange = 0

def player2(x, y):
    screen.blit(p2IMG, (x, y))

# printing ground; working on currently
def ground_level(x, y):
    screen.blit?


#OPEN AND EXECUTE FILE, USEFUL FOR SAVES POSSIBLY

# with open("FILENAME.py", 'r') as f:
#     variable = f.read()
# exec(variable)


# Game Loop
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Section for KEYDOWN polling
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DELETE:
                running = False
            if event.key == pygame.K_w:
                p1Ychange = -0.3
            if event.key == pygame.K_s:
                p1Ychange = 0.3
            if event.key == pygame.K_a:
                p1Xchange = -0.3
            if event.key == pygame.K_d:
                p1Xchange = 0.3
            if event.key == pygame.K_UP:
                p2Ychange = -0.3
            if event.key == pygame.K_DOWN:
                p2Ychange = 0.3
            if event.key == pygame.K_LEFT:
                p2Xchange = -0.3
            if event.key == pygame.K_RIGHT:
                p2Xchange = 0.3
        
        # Section for KEYUP polling
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                p1Ychange = 0
            if event.key == pygame.K_s:
                p1Ychange = 0
            if event.key == pygame.K_a:
                p1Xchange = 0
            if event.key == pygame.K_d:
                p1Xchange = 0
            if event.key == pygame.K_UP:
                p2Ychange = 0
            if event.key == pygame.K_DOWN:
                p2Ychange = 0
            if event.key == pygame.K_LEFT:
                p2Xchange = 0
            if event.key == pygame.K_RIGHT:
                p2Xchange = 0

    # fill the screen with a color to wipe away anything from last frame RGB->(0,0,0)
    screen.fill((190,190,190))

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>RENDER YOUR GAME HERE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    #Update player location and apply limit --NOT TO BE CONFUSED WITH UPDATING SCREEN
    # PLAYER 1
    p1X += p1Xchange
    p1Y += p1Ychange
    
    if p1X > displaySizeX - 96:
        p1X = displaySizeX - 96
    if p1X < 0:
        p1X = int(0)
    if p1Y > displaySizeY - 96:
        p1Y = displaySizeY - 96
    if p1Y < 0:
        p1Y = int(0)
    
    player1(p1X, p1Y)

    #PLAYER 2
    p2X += p2Xchange
    p2Y += p2Ychange
    
    if p2X > displaySizeX - 96:
        p2X = displaySizeX - 96
    if p2X < 0:
        p2X = int(0)
    if p2Y > displaySizeY - 96:
        p2Y = displaySizeY - 96
    if p2Y < 0:
        p2Y = int(0)
    
    player2(p2X, p2Y)

    
    # flip() the display to put your work on screen
    pygame.display.flip()

# Executes after running=False
pygame.quit()
