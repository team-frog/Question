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

X_PLAYER1 = 100
X_PLAYER2 = 200
Y_PLAYERS = 500
Y_BALLS_INITIAL = 400
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700

# FUNCTIONS

# How to quit our program
def quitGame():
	pygame.quit()
	sys.exit()




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

# Source in

while True:
    mousePosition = pygame.mouse.get_pos()
    surface.fill((50,0,50))
    
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
    	renderedText = textFont.render('Preguntando al jugador 1', 1, (255,255,255))
    	surface.blit(renderedText, (50, 75))
    	if (GAME_TIME.get_ticks()-timeChange) > 2000 :
    		state += 1 

    elif state == 2: # AnswerAnimation1
    	renderedText = textFont.render('Animación de respuesta 1. Dar click', 1, (255,255,255))
    	surface.blit(renderedText, (50, 75))
    	if mousePressed == True : 
    		state += 1
    		mousePressed = False
    		timeChange = GAME_TIME.get_ticks()

    elif state == 3: # QuestionPlayer2
    	renderedText = textFont.render('Preguntando al jugador 2', 1, (255,255,255))
    	surface.blit(renderedText, (50, 75))
    	if (GAME_TIME.get_ticks()-timeChange) > 2000 :
    		state += 1 

    elif state == 4: # AnswerAnimation2
    	renderedText = textFont.render('Animación de respuesta 2. Dar click', 1, (255,255,255))
    	surface.blit(renderedText, (50, 75))
    	if mousePressed == True:
    		state += 1
    		mousePressed = False
    		timeChange = GAME_TIME.get_ticks()

    elif state == 5: # Round result
    	renderedText = textFont.render('Resultado del round', 1, (255,255,255))
    	surface.blit(renderedText, (50, 75))
    	if (GAME_TIME.get_ticks()-timeChange) > 2000 :
    		state = 1
    		timeChange = GAME_TIME.get_ticks()

    clock.tick(60)
    pygame.display.update()
    