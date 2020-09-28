# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 17:07:02 2020

@author: grace
"""
import pygame
import random

class Chick(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height):
        self.width = width
        self.height = height
        self.start = (random.randint(1,9), random.randint(1,9))
        #spaces the chick has been to
        #self.spaces_tracked = 1 #starting at init square
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        #Fetch rectangle object w/ same dimensions of chick
        #& update position of obj by setting rect.x & rect.y
        self.rect = self.image.get_rect()