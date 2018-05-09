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
questions = [['Pregunta1','Correcta1','incrorrecta1a','incorrecta1b'],
             ['Pregunta1','Correcta1','incrorrecta1a','incorrecta1b']] 

contadorPreguntas = 0 # To count number of questions to finish the game
mousePosition = None
timeChange = 0 # To save the time of state changing


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

MAX_TIME = 10000 # miliseconds


# FUNCTIONS

# How to quit our program
def quitGame():
	pygame.quit()
	sys.exit()

def drawStage():
    pygame.draw.rect(surface,(255,0,0),(X_SCREEN, Y_SCREEN, WIDTH_SCREEN, HEIGHT_SCREEN))
    pygame.draw.rect(surface,(255,255,255),(0, WINDOW_HEIGHT-HEIGHT_STICK, WINDOW_WIDTH, HEIGHT_STICK))
    pygame.draw.rect(surface,(150,150,150), (0, WINDOW_HEIGHT-HEIGHT_STICK, WIDTH_SCORE, HEIGHT_STICK))
    pygame.draw.rect(surface,(150,150,150), (WINDOW_WIDTH-WIDTH_SCORE, WINDOW_HEIGHT-HEIGHT_STICK, WIDTH_SCORE, HEIGHT_STICK))
    pygame.draw.rect(surface,(255,255,255), (TARGET_A, 300, WIDTH_TARGET, 20))
    pygame.draw.rect(surface,(255,255,255), (TARGET_B, 300, WIDTH_TARGET, 20))
    pygame.draw.rect(surface,(255,255,255), (TARGET_C, 300, WIDTH_TARGET, 20))


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




# PYGAME OBJECTS

pygame.init()
clock = pygame.time.Clock()
pygame.font.init()
surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('QUESTIONS GAME: ANTONIO MUÑOZ, DANIEL ROMERO. IES CANTELY')
textFont = pygame.font.SysFont("monospace", 50)


player1 = objects.basketPlayer(1, X_PLAYER1, Y_PLAYERS)
player2 = objects.basketPlayer(2, X_PLAYER2, Y_PLAYERS)
ball1 = objects.ball(1)
ball2 = objects.ball(2)


def questionPlayer(player):
    global mousePressed, state, answerPlayer
    if player==1:
        playerA = player1
        ballA = ball1
        playerB = player2
    else:
        playerA = player2
        ballA = ball2
        playerB = player1
    renderedText = textFont.render('Preguntando al jugador ' + str(player), 1, (255,255,255))
    surface.blit(renderedText, (50, 75))
    playerB.returnToInitialPos()
    playerA.move(mousePosition[0])
    ballA.move(playerA.getPos(), playerA.getWidth())
    ballA.draw(surface, pygame)
    if mousePressed == True:
        ballA.throw()
    drawTimeStick(MAX_TIME - int(GAME_TIME.get_ticks()-timeChange))
    if (GAME_TIME.get_ticks()-timeChange) > MAX_TIME or ballA.fallen():
        state += 1
        mousePressed = False
        if (GAME_TIME.get_ticks()-timeChange) > MAX_TIME :
            answerPlayer = 'none'
        else :
            answerPlayer = answer(ballA.fallen())
        ballA.reset()


# Source in

while True:
    mousePosition = pygame.mouse.get_pos()
    surface.fill((50,0,50))
    drawStage()
    player1.draw(surface,pygame)
    player2.draw(surface,pygame)


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
        renderedText = textFont.render('Respuesta anterior: ' + answerPlayer, 1, (255,255,255))
        surface.blit(renderedText, (50, 75))
        ball1.draw(surface, pygame)
        if mousePressed == True : 
            state += 1
            mousePressed = False
            timeChange = GAME_TIME.get_ticks()

    elif state == 3: # QuestionPlayer2
        questionPlayer(2)

    elif state == 4: # AnswerAnimation2
        renderedText = textFont.render('Respuesta anterior: ' + answerPlayer, 1, (255,255,255))
        surface.blit(renderedText, (50, 75))
        ball2.draw(surface, pygame)
        if mousePressed == True:
            state += 1
            mousePressed = False
            timeChange = GAME_TIME.get_ticks()

    elif state == 5: # Round result
    	renderedText = textFont.render('Resultado del round. Dar click', 1, (255,255,255))
    	surface.blit(renderedText, (50, 75))
    	if mousePressed == True : 
            state = 1
            mousePressed = False
            timeChange = GAME_TIME.get_ticks()

    clock.tick(60)
    pygame.display.update()
    