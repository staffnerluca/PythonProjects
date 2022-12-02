import pygame
import random

pygame.init()
WIDTH, HEIGHT = 900, 900
window = pygame.display.set_mode((WIDTH, HEIGHT))
rightScore = 0
leftScore = 0
font = pygame.font.SysFont("Times", 30)
winnerFont = pygame.font.SysFont("Times", 90)
leftY = 400
rightY = 400
directionVector = [0, 0]
ballX = 450
ballY = 450

def drawPlayer():
    leftPlayer = pygame.Rect(20, leftY, 10, 100)
    rightPlayer = pygame.Rect(880, rightY, 10, 100)
    pygame.draw.rect(window, (255, 255, 255), leftPlayer)
    pygame.draw.rect(window, (255, 255, 255), rightPlayer)

def movePlayer(keyPressed):
    global rightY, leftY
    if keyPressed[pygame.K_UP]:
        rightY -= 10
    elif keyPressed[pygame.K_DOWN]:
        rightY += 10
    if  keyPressed[pygame.K_w]:
        leftY -=10
    elif keyPressed[pygame.K_s]:
        leftY +=10

def firstMoveBall():
    global directionVector
    plusOrMin0 = random.randint(0, 1)
    if plusOrMin0 == 1:
        directionVector[0] = 7
    elif plusOrMin0 == 0:
        directionVector[0] = -7

    plusOrMin1 = random.randint(0, 1)
    if plusOrMin1 == 1:
        directionVector[1] = random.randint(1, 8)
    elif plusOrMin1 == 0:
        directionVector[1] = random.randint(-8, -1)
        
def resetBall():
    global ballX, ballY
    ballX = 450
    ballY = 450
    firstMoveBall()

def drawBall():
    global directionVector, ballX, ballY
    ballX += directionVector[0]
    ballY += directionVector[1]
    ball = pygame.Rect(ballX, ballY, 10, 10)
    pygame.draw.rect(window, (255, 255, 255), ball)

def collision():
    global directionVector, leftBorder, rightBorder, topBorder, bottomBorder, leftScore, rightScore
    ball = pygame.Rect(ballX, ballY, 10, 10)
    leftPlayer = pygame.Rect(20, leftY, 10, 100)
    rightPlayer = pygame.Rect(880, rightY, 10, 100)
    if ball.colliderect(leftPlayer) or ball.colliderect(rightPlayer):
        directionVector[0] = directionVector[0]*(-1)
    if ballX <= 1:
        rightScore += 1
        resetBall()
    if ballX > 899:
        leftScore += 1 
        resetBall()
    if ballY < 1 or ballY > 899:
        directionVector[1] = directionVector[1] * (-1)

def drawWinner():
    if leftScore == 10:
        winner = font.render("The left player won ", 1, (255, 255, 255))
    elif rightScore == 10:
        winner = font.render("The right player won ", 1, (255, 255, 255))
    window.blit(winner, (350, 450))

if __name__ == "__main__":
    run = True
    first = True
    while run:
        pygame.time.Clock().tick(60)
        window.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keyPressed = pygame.key.get_pressed()
        movePlayer(keyPressed)
        drawPlayer()
        if first:
            firstMoveBall()
            first = False
        drawBall()
        collision()
        dScoreRight = font.render("Score: " + str(rightScore), 1, (255, 255, 255))
        dScoreLeft = font.render("Score: " + str(leftScore), 1, (255, 255, 255))
        window.blit(dScoreLeft, (30, 50))
        window.blit(dScoreRight, (770, 50))
        if leftScore == 10 or rightScore == 10:
            drawWinner()
            pygame.time.Clock().tick(5000)
            run = False
        pygame.display.update()
