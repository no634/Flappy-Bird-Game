import random
import sys
import pygame
from pygame.locals import *

FPS = 11
sheight = 289
switdh = 581
gamewindow = pygame.display.set_mode (sheight, switdh)
groundy = sheight * 8
gamesprites = {}
gamesounds = {}
bird = images/bird.png
background = images/background.png
pipe = images/pipe.png

def welcomescreen():
    playerx = int(switdh/5)
    playery = int((switdh - gamesprites[‘player’].get_height())/2)
    messagex = int((switdh - gamesprites[‘message’].get_width())/2)
    messagey = int (sheight * 0.13)
    basex = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            elif (event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP)):
                return
            else:
                SCREEN.blit(gamesprites[‘background’], (0, 0)
                SCREEN.blit(gamesprites[‘player’], (playerx, playery)
                SCREEN.blit(gamesprites[‘message’], (messagex, messagey)
                SCREEN.blit(gamesprites[‘base’], (basex, groundy)
                pygame.display.update
                FPSCLOCK.tick(FPS)
def maingame():
    score = 0
    playerx = int(switdh/5)
    playery = int(switdh/2)
    basex = 0
    newpipe1 = getRandomPipe()
    newpipe2 = getRandomPipe
    upperpipes = [
        {'x':switdh + 200, 'y':newpipe1[0]['y']},
        {'x':switdh + 200 +(switdh/2), 'y': newpipe2[0]['y']}]
    lowerpipes = [
        {'x':switdh + 200, 'y':newpipe1[1]['y']}
        {'x':switdh + 200 +(switdh/2), 'y': newpipe2[1]['y']}]

    pipeVeIX = -4
    pipeVeIY = -9
    pipeMaxVeIY = 10
    pipeMinVeIY = -8
    playerAccY = 1
    playerFlapAccv = -8
    playerFlapped = False
    while True:
        for event in pygame.event.get():
            if event.type == QUIT (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_DOWN):
                if playery > 0 :
                    playerVeIY = playerFlapAccv
                    playerFlapped = True
                    GAME.SOUNDS['wing'].play()
            CrashTest = isCollide(playerx, playery, upperpipe, lowerpipe)
            if CrashTest:
                return

    PlayerMidPos = playerx + GAME_SPRITES['player'].get_width()/2
    for pipe in upperPipes:
        pipeMidPos = pipe['x']+GAME_SPRITES['pipe'][0].get_witdh() / 2
        if pipeMIdPos <= playerMidPos < pipeMidPos + 4:
            score += 1
            print('your score is:' , score)
            GAME_SOUNDS['point'].play()