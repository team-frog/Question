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
            
        
class ball:
    def __init__(self,type):
        self.type = type # player 1 or player 2
        self.x = 0 # Possition on x axis. To be defined from x,y of player
        self.y = 0 # Possition on y axis. To be defined from x,y of player