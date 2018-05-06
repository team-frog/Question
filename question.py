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
import objects

# VARIABLES

state = 0; # Waiting = 0; 
mousePressed = False # Para saber si el ratón está pulsado

# Hay que leer el fichero CSV y crear una lista de listas como esta
questions = [['Pregunta1','Correcta1','incrorrecta1a','incorrecta1b'],
             ['Pregunta1','Correcta1','incrorrecta1a','incorrecta1b']] 

contadorPreguntas = 0 # To count number of questions to finish the game
mousePosition = None

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
surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('QUESTIONS GAME: ANTONIO MUÑOZ, DANIEL ROMERO. IES CANTELY')

player1 = objects.basketPlayer(1, X_PLAYER1, Y_PLAYERS)
player2 = objects.basketPlayer(2, X_PLAYER2, Y_PLAYERS)
ball1 = objects.ball(1)
ball2 = objects.ball(2)

while True:
    mousePosition = pygame.mouse.get_pos()
    surface.fill((200,0,200))
    
    	# Handle user and system events 
    for event in GAME_EVENTS.get():
    		if event.type == pygame.KEYDOWN:
    			if event.key == pygame.K_ESCAPE:
    				quitGame()
    		if event.type == pygame.MOUSEBUTTONUP:
    			mousePressed = False
    		if event.type == GAME_GLOBALS.QUIT:
    			quitGame()


    clock.tick(60)
    pygame.display.update()
    