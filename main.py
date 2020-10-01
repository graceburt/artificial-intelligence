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

draw(board)

#def move(player, r, board):
#          print("{} goes {}").format(player, r)
#          
#          if r == "left" and (player.pos[1] - 1) != 0:
#
#            board[player.pos[0]][player.pos[1]] = 1
#            board[player.pos[0]][player.pos[1]-1] = 2
#
#          elif r == "right" and (player.pos[1] + 1) != 9:
#
#            board[player.pos[0]][player.pos[1]] = 1
#            board[player.pos[0]][player.pos[1]+1] = 2
#
#          elif r == "down" and (player.pos[0] + 1) !=  9:
#
#            board[player.pos[0]][player.pos[1]] = 1
#            board[player.pos[0]+1][player.pos[1]] = 2
#            
#          elif r == "up" and (player.pos[0] - 1) != 0:
#        
#            board[player.pos[0]][player.pos[1]] = 1
#            board[player.pos[0]-1][player.pos[1]] = 2
#
#          else:
#            return player
def test_move(player, newPos):
        if newPos == '1':
            #return 'failure'
            player.put_result(1)
        elif newPos == '3':
            #return 'portal'
            player.put_result(2)
        else:
            #return 'success'
            player.put_result(0)
            
def move(player, r):
    
      print("{} goes {}").format(player.pos, r)
      # print(type(AI[1]-1), "Hello")
      newPos = (0,0)
     
      if r == "left":
          newPos = (player.pos[0], player.pos[1]-1)
          # print(f"{newPos} - {type(newPos)}")
          
      elif r == "right":   
          # grid[AI[0]][AI[1]] = 2
          newPos = (player.pos[0], player.pos[1]+1)
          # print(f"{newPos} - {type(newPos)}")
          
      elif r == "down": 
          # grid[AI[0]][AI[1]] = 2
          newPos = (player.pos[0]+1, player.pos[1])
          # print(f"{newPos} - {type(newPos)}")
          
      elif r == "up":         
          # grid[AI[0]][AI[1]] = 2
          newPos = (player.pos[0]-1, player.pos[1])
          # print(f"{newPos} - {type(newPos)}")
     
      test_move(player, newPos)
      
      if player.last_result == 'success':
          player.pos = newPos
      elif player.last_result== 'portal':
          player.pos = newPos
      else:
          player.last_result == 'failure'
        
while run:
        
    move(player, player.get_decision())

   #move AI based on player.last_decision
   
    move_total = move_total + 1

    pygame.display.update()
    clock.tick(3)
    draw(board)
    
           
pygame.quit()
        