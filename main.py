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
board[0][0] = 5
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

def test_move(player, newPos, board):
    
        if board[newPos[0]][newPos[1]] == 1: 
        # board[player.pos[0]][player.pos[1]] == 1: #wall
            print("wall")
            player.put_result(player.results[1])
            
        elif board[newPos[0]][newPos[1]] == 3:
        #board[player.pos[0]][player.pos[1]] == 3: #portal
            print("portal")
            player.put_result(player.results[2])
            
        else:
            print("success")
            player.put_result(player.results[0])
            
def move(player, r, board):
    
    print("{} goes {}").format(player.pos, r)
     
    if r == "left":
      newPos = (player.pos[0], player.pos[1]-1)
      test_move(player, newPos, board)
          
    elif r == "right":   
      newPos = (player.pos[0], player.pos[1]+1)
      test_move(player, newPos, board)
      #print(newPos)
     
    elif r == "down": 
      newPos = (player.pos[0]+1, player.pos[1])
      test_move(player, newPos, board)
      #print(newPos)
          
    elif r == "up":         
      newPos = (player.pos[0]-1, player.pos[1])
      test_move(player, newPos, board)

    if player.last_result == 'success':
        player.pos = newPos
        board[player.pos[0]][player.pos[1]] = 2
          #print(player.pos)
    elif player.last_result== 'portal':
        player.pos = newPos
        board[player.pos[0]][player.pos[1]] = 2
        return False
          #print(player.pos)
    else:
        move(player, player.get_decision(), board)

        
while run:
        
    value = move(player, player.get_decision(), board)
    print(board)
    move_total = move_total + 1
    
    if value == False:
        run = False

    pygame.display.update()
    clock.tick(3)
    draw(board)
    
           
pygame.quit()