from email import message
import pygame
import os
import sys
import os
import random
import math

pygame.init()
pygame.display.set_caption("Snake Game")
pygame.font.init()
random.speed()

speed = 0.30
sanke_size = 9
apple_size = sanke_size
seperation = 10
screen_height = 600
snake_width = 800
FPS = 25
key = {"UP":1 , "Down":2 , "LEFT":3 , "RIGHT":4}

screen = pygame.display.set_mode((screen_height,screen_height),pygame.HWSURFACE)

score_font = pygame.font.Font(None,38)
score_numb_font = pygame.font.Font(None,28)
game_over_font = pygame.font.Font(None,48)
play_again_font = score_numb_font
score_msg = score_font.render("Score : ",1,pygame.Color("green"))
score_msg_size = score_font.size("Score")
background_color = pygame.Color(0,0,0)
black = pygame.Color(0,0,0)

gameClock = pygame.time.Clock()

def getKey():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                return key["UP"]
            elif event.key == pygame.K_DOWN:
                return key["DOWN"]
            elif event.key == pygame.K_LEFT:
                return key["LEFT"]
            elif event.key == pygame.K_RIGHT:
                return key["RIGHT"]
            elif event.key == pygame.K_ESCAPE:
                return "exit"
            elif event.key == pygame.K_y:
                return "yes"
            elif event.key == pygame.K_n:
                return "no"
        if event.type == pygame.QUIT:
            sys.exit(0)

def endGame():
    message = game_over_font.render("Game Over",1,pygame.Color("white"))
    message_play_again = play_again_font.render("Play Again ? (Y/N",1,pygame.Color("green"))
    screen.blit(message,(320,240))
    screen.blit(message_play_again,(320+12,240+40))

    pygame.display.flip()
    pygame.display.update()

    mKey = getKey()
    while(mKey != "exit"):
        if(mKey == "yes"):
            main()
        elif(mKey == "no"):
            break
        mKey = getKey()
        gameClock.tick(FPS)
    sys.exit(0)

def drawScore(score):
    score_numb = score_numb_font.render(str(score),1,pygame.Color("red"))
    screen.blit(score_msg, ())



