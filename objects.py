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
	def __init__(self, type, x, y, xPoints, yPoints):
		self.type = type # player 1 or player 2
		self.x = x # Possition on x axis
		self.y = y # Possition on y axis
		self.xPoints = xPoints
		self.yPoints = yPoints
		self.initialPos = x
		self.WIDTH = 100
		self.HEIGHT = 150
		self.points = 0
		if self.type == 1:
			self.color = (0,0,255)
		else:
			self.color = (0,255,0)
		self.SPEED = 5
	
	def getPos(self): # Para que te devuelva un tupple con las posiciones del jugador
		return (self.x, self.y)	

	def getWidth(self): # Esta función te devuelve la anchura del jugador
		return self.WIDTH
	
	def getPoints(self):
		return self.points
	
	def returnToInitialPos(self): # Esta función, la cual se va ejecutando siempre que esté en el state apropiado, hace que el jugador vuelva lentamente a la posicion de inicio
            if self.x > self.initialPos:
                self.x -= self.SPEED
            if self.x < self.initialPos:
                self.x += self.SPEED
    
	def onePointMore(self):
		self.points += 1

	def move(self,xmouse): # Para mover al jugador
		if self.x + (self.WIDTH/2) > xmouse:
			self.x -= self.SPEED
		else:
			self.x += self.SPEED

	def draw(self, surface, pygame, textFont): # Para dibujar al jugador
		pygame.draw.rect(surface,self.color,(self.x, self.y, self.WIDTH, self.HEIGHT))
		renderedText = textFont.render(str(self.points), 1, (255,255,255))
		surface.blit(renderedText, (self.xPoints, self.yPoints))



        


class ball:
	def __init__(self,type, pygame):
		self.type = type # player 1 or player 2
		self.x = 0 # Possition on x axis. To be defined from x,y of player
		self.y = 0 # Possition on y axis. To be defined from x,y of player
		self.WIDTH = 50
		self.HEIGHT = 50
		self.color = (0,255,255)
		self.flying = False
		self.gravity = 1
		self.INITIALIMPULSE = 25
		self.impulse = self.INITIALIMPULSE
		self.ANGLE_SPEED=10
		self.angle=0

		# Images
		self.ballImage = pygame.image.load("assets/images/ball.png")
		self.rect=self.ballImage.get_rect()
		self.rect.center = (self.x, self.y)
		self.imageToDraw = self.ballImage


	def move(self, playerPos, playerWIDTH, pygame): # Para mover la pelota
		if self.flying == False:
			self.x = int(playerPos[0]+(playerWIDTH)/2)
			self.y = playerPos[1] + 50
		else:
			#self.ballImage = pygame.transform.rotate(self.ballImage, 90)
			self.y -= self.impulse
			self.impulse -= self.gravity

	def draw(self, surface, pygame): # Para dibujar la pelota
		if self.flying == False:
			self.rect.center = (self.x, self.y)
			surface.blit(self.imageToDraw, self.rect)
		else:
			self.angle += self.ANGLE_SPEED
			self.angle = self.angle%360
			self.imageToDraw = pygame.transform.rotate(self.ballImage,self.angle)
			self.rect = self.imageToDraw.get_rect()
			self.rect.center = (self.x, self.y)
			surface.blit(self.imageToDraw, self.rect)
	def throw(self): # Para cambiar a true la variable flying
		self.flying = True

	def reset(self): 
		self.flying = False
		self.impulse = self.INITIALIMPULSE

	def fallen(self):
		if self.impulse > (-1)*self.INITIALIMPULSE :
			return 0
		else :
			return self.x+self.WIDTH/2

