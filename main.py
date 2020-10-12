# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 16:14:57 2020
@author: grace
"""
import pygame
import numpy as np
import DecisionFactory as df

#screen size
WIDTH, HEIGHT = 20, 20

BLACK = (255,255,255)
WHITE = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
FPS = .5

#grid size
rows = 10
cols = 10
MARGIN = 5 #this will be the space between boxes

board = np.ones((rows,cols))
board[1: -1, 1: -1] = 0

pygame.init()

WIN_SIZE = [400,400]
SCREEN = pygame.display.set_mode(WIN_SIZE) #graphics window
pygame.display.set_caption('AI Escape!') 

run = True #game runs
clock = pygame.time.Clock() #contant fps#decision factory obj

#player
player = df.DecisionFactory("dante", board)
    
#portal
board[7][4] = 3

move_total = 0

def draw(board):
    SCREEN.fill(BLACK)    
    for row in range(rows):
        for col in range(cols):
            color = WHITE
            if board[row][col] == 2:
                color = RED 
            elif board[row][col] == 3:
                color = BLUE
            elif board[row][col] == 1:
                color = GREEN
            elif board[0][0]:
                color = WHITE
            
            pygame.draw.rect(SCREEN, color, [(MARGIN + WIDTH) * col + MARGIN,
                 (MARGIN + HEIGHT) * row + MARGIN,
                 WIDTH,
                 HEIGHT])

    pygame.display.update()

draw(board)


while run:
        
    value = player.spiral(board)
    print("---------------------------------------------------")
    print(board)
    
    if value == False:
        run = False
        
    #print(board)
    #move_total = move_total + 1

    pygame.display.update()
    clock.tick(3)
    draw(board)
    
print("It took {} many moves to find portal!").format(move_total)
pygame.quit()