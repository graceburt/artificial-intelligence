# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 16:14:57 2020

@author: grace
"""
import pygame
import numpy as np
import random
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
board[7][4] = 3

pygame.init()

WIN_SIZE = [400,400]
SCREEN = pygame.display.set_mode(WIN_SIZE) #graphics window
pygame.display.set_caption('AI Escape!') 

run = True #game runs
clock = pygame.time.Clock() #contant fps#decision factory obj

player = df.DecisionFactory("dante", board)

#player
board[player[0]][player[1]] = 2
player_position = (random.randint(1,8), random.randint(1,8))
#portal
board[7][4] = 3
    
def draw(board):
    SCREEN.fill(BLACK)    
    for row in range(rows):
        for col in range(cols):
            color = WHITE
            if board[row][col] == 2:
                color = BLUE
            elif board[row][col] == 3:
                color = RED
            elif board[row][col] == 1:
                color = GREEN
            
            pygame.draw.rect(SCREEN, color, [(MARGIN + WIDTH) * col + MARGIN,
                 (MARGIN + HEIGHT) * row + MARGIN,
                 WIDTH,
                 HEIGHT])

    pygame.display.update()

def move(r, player):
          print("{} goes {}").format(player, r)
          # print(type(AI[1]-1), "Hello")
          newPos = (0,0)
          if r == "left" and (player[1] - 1) >= 0:
        
            # grid[AI[0]][AI[1]] = 2
            newPos = (player[0], player[1]-1)
            # print(f"{newPos} - {type(newPos)}")
            return newPos
          elif r == "right" and (player[1] + 1) <= 9:
        
            # grid[AI[0]][AI[1]] = 2
            newPos = (player[0], player[1]+1)
            # print(f"{newPos} - {type(newPos)}")
            return newPos
          elif r == "down" and (player[0] + 1) <=  9:
        
            # grid[AI[0]][AI[1]] = 2
            newPos = (player[0]+1, player[1])
            # print(f"{newPos} - {type(newPos)}")
            return newPos
          elif r == "up" and (player[0] - 1) >= 0:
        
            # grid[AI[0]][AI[1]] = 2
            newPos = (player[0]-1, player[1])
            # print(f"{newPos} - {type(newPos)}")
            return newPos
          else:
            return player

move_total = 0

draw(board)

while run:
        
    df.test_move(player, player.get_decision(), board)
    if player.last_result == "failure":
        df.test_move(player.get_decision(), player, board)
    else:
       move(player, player.get_decision(), board)

   #move AI based on player.last_decision
   
    move_total = move_total + 1

            
    clock.tick(3)
    draw(board)
    
    
            
pygame.quit()
        