import pygame
from blocks import Block
import random

pygame.init()
WIDTH, HEIGHT = 900, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
playerPosition=15*7
playerLength=1
BLOCKNUMBER=225
score=0
size=0
font = pygame.font.SysFont('comicsans', 100)
run = True

def placeApple(blocks):
    blocks[random.randint(0, BLOCKNUMBER)].color = (255, 0, 0)
    return blocks

def getApple(blocks):
    global playerLength
    global score
    playerLength+=1
    score+=1
    blocks = placeApple(blocks)
    return blocks

def gameOver():
    global score
    global run
    txt = font.render(f"Game Over! Score = {score}", 1, (255, 255, 255))
    WIN.blit(txt, (10, 450))
    pygame.display.update()
    run =False
    pygame.time.delay(5000)

def drawPlayer(move, blocks):
    global playerPosition
    global size
    global playerLength
    
    if move == 1 and (playerPosition+move) % 15 == 0:
        gameOver()

    if move == -1 and (playerPosition-move) % 15 == 0 :
        gameOver()

    if blocks[playerPosition+move].color != (0, 0, 0):
        if blocks[playerPosition+move].color == (255, 0, 0):
            blocks = getApple(blocks)
        playerPosition+=move
        blocks[playerPosition].number = size
        blocks[playerPosition].color = (0, 0, 0)
     
        if size == playerLength:
            for b in blocks:
                if b.number == 0:
                    b.color = (0, 255, 0)
            for bl in blocks:
                if bl.number != -1:
                    bl.number-=1
            size-=1
        else:
            size+=1

    elif blocks[playerPosition+move].color == (0, 0, 0) and move != 0:
        gameOver()

    return blocks

def handleMovement(press):
    #1 is x and 15 is y
    if press[pygame.K_DOWN]:
        return 15
    
    elif press[pygame.K_UP]:
        return -15

    elif press[pygame.K_LEFT]:
        return -1

    elif press[pygame.K_RIGHT]:
        return 1
    
    else:
        return 0

def createField():
    blocks=[]
    x=0
    y=-60
    for i in range(BLOCKNUMBER):
        head=False
        if i % 15==0:
            y+=60
            x=0

        if i == playerPosition:
            head=True

        b=Block(60, 60, (0, 255, 0), x, y, -1)
        blocks.append(b)
        x+=60
    return blocks

def drawWindow(blocks):
    for b in blocks:
        pygame.draw.rect(WIN, b.color, pygame.Rect((b.x, b.y), (b.height, b.width)))
    pygame.display.update()

def main():
    global run
    blocks=createField() 
    move=0
    for i in range(5):
        blocks = placeApple(blocks)
    try:
        while run:
            pygame.time.Clock().tick(60)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False
                blocks = drawPlayer(move, blocks)
            keyPressed = pygame.key.get_pressed()
            move=handleMovement(keyPressed)
            drawPlayer(move, blocks)
            drawWindow(blocks)
    except IndexError:
        gameOver()
    pygame.quit()
main()
