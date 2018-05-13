#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  6 12:30:48 2018

@author: Antonio Muñoz Santiago

This is the main file
"""
import pygame, sys, random
import pygame.event as GAME_EVENTS
import pygame.locals as GAME_GLOBALS
import pygame.time as GAME_TIME
import csv
import objects

# VARIABLES

state = 0; # Waiting = 0; QuestionPlayer1 = 1; 
mousePressed = False # Para saber si el ratón está pulsado

# Hay que leer el fichero CSV y crear una lista de listas como esta
questionFile = open('assets/questions/prueba.csv')
questionReader = csv.reader(questionFile, delimiter=';')
questionList = list(questionReader)

contadorPreguntas = 0 # To count number of questions to finish the game
mousePosition = None
timeChange = 0 # To save the time of state changing
toAsk = random.randint(0,len(questionList)-1) # Number of the question choosen randomly
order = [1,2,3]
random.shuffle(order)
answerCorrect = None
rounds = 0


# CONSTANTS

X_PLAYER1 = 0
X_PLAYER2 = 900
Y_PLAYERS = 500
Y_BALLS_INITIAL = 400

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700

X_SCREEN = 100
Y_SCREEN = 50
WIDTH_SCREEN = 800
HEIGHT_SCREEN = 200

HEIGHT_STICK = 50
HEIGHT_TIME_STICK = 30
WIDTH_TIME_STICK = 800

WIDTH_TARGET = 100
TARGET_A = 150
TARGET_B = 450
TARGET_C = 750

WIDTH_SCORE = 100

POINT_X_DESP = 25
X_POINT1 = 0 + POINT_X_DESP
Y_POINT1 = WINDOW_HEIGHT - HEIGHT_STICK
X_POINT2 = WINDOW_WIDTH - WIDTH_SCORE + POINT_X_DESP
Y_POINT2 = WINDOW_HEIGHT - HEIGHT_STICK

MAX_TIME = 20000 # miliseconds
MAX_ROUNDS = 9


# FUNCTIONS

# How to quit our program
def quitGame():
    questionFile.close()
    pygame.quit()
    sys.exit()

def drawStage():
    pygame.draw.rect(surface,(255,0,0),(X_SCREEN, Y_SCREEN, WIDTH_SCREEN, HEIGHT_SCREEN))
    pygame.draw.rect(surface,(255,255,255),(0, WINDOW_HEIGHT-HEIGHT_STICK, WINDOW_WIDTH, HEIGHT_STICK))
    pygame.draw.rect(surface,(150,150,150), (0, WINDOW_HEIGHT-HEIGHT_STICK, WIDTH_SCORE, HEIGHT_STICK))
    pygame.draw.rect(surface,(150,150,150), (WINDOW_WIDTH-WIDTH_SCORE, WINDOW_HEIGHT-HEIGHT_STICK, WIDTH_SCORE, HEIGHT_STICK))
    pygame.draw.rect(surface,(196,107,20), (TARGET_A, 300, WIDTH_TARGET, 20))
    pygame.draw.rect(surface,(196,107,20), (TARGET_B, 300, WIDTH_TARGET, 20))
    pygame.draw.rect(surface,(196,107,20), (TARGET_C, 300, WIDTH_TARGET, 20))


def drawTimeStick(timeLeft) :
	width_real_ts = WIDTH_TIME_STICK*timeLeft/MAX_TIME
	pygame.draw.rect(surface, (255,0,0), (int((WINDOW_WIDTH-width_real_ts)/2), int(WINDOW_HEIGHT-HEIGHT_STICK+(HEIGHT_STICK-HEIGHT_TIME_STICK)/2), width_real_ts, HEIGHT_TIME_STICK))

def answer(xball) :
    toReturn = 'out'
    if xball > TARGET_A and xball < TARGET_A + WIDTH_TARGET :
        return 'A'
    elif xball > TARGET_B and xball < TARGET_B + WIDTH_TARGET :
        return 'B'
    elif xball > TARGET_C and xball < TARGET_C + WIDTH_TARGET :
        return 'C'
    return toReturn

def whoCorrect(listOrder):
    for i in range(3):
        if listOrder[i] == 1:
            return i

# PYGAME OBJECTS

pygame.init()
clock = pygame.time.Clock()
pygame.font.init()
surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('QUESTIONS GAME: ANTONIO MUÑOZ, DANIEL ROMERO. IES CANTELY')
textFont = pygame.font.SysFont("monospace", 30)
textFontPoints = pygame.font.SysFont("Becker", 65)


player1 = objects.basketPlayer(1, X_PLAYER1, Y_PLAYERS, X_POINT1, Y_POINT1)
player2 = objects.basketPlayer(2, X_PLAYER2, Y_PLAYERS, X_POINT2, Y_POINT2)
ball1 = objects.ball(1, pygame)
ball2 = objects.ball(2, pygame)

mousePosition = pygame.mouse.get_pos()

def questionPlayer(player):
    global mousePressed, state, answerPlayer, mousePosition, questionList, toAsk, answerCorrect
    if player==1:
        playerA = player1
        ballA = ball1
        playerB = player2
    else:
        playerA = player2
        ballA = ball2
        playerB = player1
    renderedText = textFont.render(questionList[toAsk][0], 1, (255,255,255))
    surface.blit(renderedText, (75, 75))
    renderedText = textFont.render('A: ' + questionList[toAsk][order[0]], 1, (255,255,255))
    surface.blit(renderedText, (75, 100))
    renderedText = textFont.render('B: ' + questionList[toAsk][order[1]], 1, (255,255,255))
    surface.blit(renderedText, (75, 125))
    renderedText = textFont.render('C: ' + questionList[toAsk][order[2]], 1, (255,255,255))
    surface.blit(renderedText, (75, 150))
    playerB.returnToInitialPos()
    playerA.move(mousePosition[0])
    ballA.move(playerA.getPos(), playerA.getWidth(), pygame)
    ballA.draw(surface, pygame)
    if mousePressed == True:
        ballA.throw()
    drawTimeStick(MAX_TIME - int(GAME_TIME.get_ticks()-timeChange))
    if (GAME_TIME.get_ticks()-timeChange) > MAX_TIME or ballA.fallen():
        state += 1
        answerCorrect = whoCorrect(order)
        toAsk = random.randint(0,len(questionList)-1)
        random.shuffle(order)
        mousePressed = False
        if (GAME_TIME.get_ticks()-timeChange) > MAX_TIME :
            answerPlayer = 'none'
        else :
            answerPlayer = answer(ballA.fallen())
        ballA.reset()
        if (answerPlayer == 'A' and answerCorrect==0) or (answerPlayer == 'B' and answerCorrect==1) or (answerPlayer == 'C' and answerCorrect==2): 
            playerA.onePointMore()
            print('muy bien!!')
        else:
            print('a ver si mejoras :C')

def answerAnimation(player):
    global mousePressed, answerPlayer, state, timeChange, answerCorrect, answerCorrect
    if player==1:
        ballA = ball1
    else:
        ballA = ball2
    if (answerPlayer == 'A' and answerCorrect==0) or (answerPlayer == 'B' and answerCorrect==1) or (answerPlayer == 'C' and answerCorrect==2):
        renderedText = textFont.render('Muy bien!!!', 1, (255,255,255))
    elif answerPlayer == 'out':
        renderedText = textFont.render('Apunta mejor!!!', 1, (255,255,255))
    elif answerPlayer == 'none':
        renderedText = textFont.render('Indeciso!!!', 1, (255,255,255))
    else:
        renderedText = textFont.render('Ceporro!!!', 1, (255,255,255))
    surface.blit(renderedText, (70, 75))
    ballA.draw(surface, pygame)
    if mousePressed == True : 
        state += 1
        mousePressed = False
        timeChange = GAME_TIME.get_ticks()
# Source in

while True:
    mousePosition = pygame.mouse.get_pos()
    surface.fill((50,0,50))
    drawStage()
    player1.draw(surface,pygame, textFontPoints)
    player2.draw(surface,pygame, textFontPoints)


    	# Handle user and system events 
    for event in GAME_EVENTS.get():
    		if event.type == pygame.KEYDOWN:
    			if event.key == pygame.K_ESCAPE:
    				quitGame()
    		if event.type == pygame.MOUSEBUTTONUP:
    			mousePressed = True
    		if event.type == GAME_GLOBALS.QUIT:
    			quitGame()

    if state == 0: # Waiting
        renderedText = textFont.render('Pulsa click para comenzar', 1, (255,255,255))
        surface.blit(renderedText, (50, 75))
        if mousePressed == True :
            state += 1
            mousePressed = False
            timeChange = GAME_TIME.get_ticks()
    elif state == 1: # QuestionPlayer1 
        questionPlayer(1)

    elif state == 2: # AnswerAnimation1
        answerAnimation(1)

    elif state == 3: # QuestionPlayer2
        questionPlayer(2)

    elif state == 4: # AnswerAnimation2
        answerAnimation(2)

    elif state == 5: # Round result
    	renderedText = textFont.render('Resultado del round. Dar click', 1, (255,255,255))
    	surface.blit(renderedText, (50, 75))
    	if mousePressed == True : 
            state = 1
            mousePressed = False
            timeChange = GAME_TIME.get_ticks()
            rounds +=1
            if rounds == MAX_ROUNDS:
				if player1.getPoints() > player2.getPoints():
					print('ha ganado player1')
				elif player2.getPoints() > player1.getPoints():
					print('ha ganedo player2')
				elif player1.getPoints() == player2.getPoints():
					print('han quedado empate')
				quitGame()

    clock.tick(60)
    pygame.display.update()
    
