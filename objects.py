#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  6 12:44:08 2018

@author: Antonio Muñoz Santiago

All objects of the game:
    basketPlayer: Player of the game
    Ball: Ball
"""

class basketPlayer:
	def __init__(self, type, x, y):
		self.type = type # player 1 or player 2
		self.x = x # Possition on x axis
		self.y = y # Possition on y axis
		self.WIDTH = 100
		self.HEIGHT = 150
		if self.type == 1:
			self.color = (0,0,255)
		else:
			self.color = (0,255,0)
		self.SPEED = 3

	def getPos(self):
		return (self.x, self.y)	

	def getWidth(self):
		return self.WIDTH

	def move(self,xmouse):
		if self.x + (self.WIDTH/2) > xmouse:
			self.x -= self.SPEED
		else:
			self.x += self.SPEED

	def draw(self,surface,pygame):
		pygame.draw.rect(surface,self.color,(self.x, self.y, self.WIDTH, self.HEIGHT))




        


class ball:
	def __init__(self,type):
		self.type = type # player 1 or player 2
		self.x = 0 # Possition on x axis. To be defined from x,y of player
		self.y = 0 # Possition on y axis. To be defined from x,y of player
		self.WIDTH = 50
		self.HEIGHT = 50
		self.color = (0,255,255)
		self.flying = False

	def move(self, playerPos, playerWIDTH):
		if self.flying == False:
			self.x = int(playerPos[0]+(playerWIDTH-self.WIDTH)/2)
			self.y = playerPos[1]

	def draw(self, surface, pygame):
		pygame.draw.rect(surface, self.color, (self.x, self.y, self.WIDTH,self.HEIGHT))



