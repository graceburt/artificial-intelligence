# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 16:33:21 2020

@author: grace
"""
import pygame
#import sys

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480

NUMBER_OF_BLOCKS_WIDE = 12
NUMBER_OF_BLOCKS_HIGH = 12
BLOCK_HEIGHT = round(SCREEN_HEIGHT/NUMBER_OF_BLOCKS_HIGH)
BLOCK_WIDTH = round(SCREEN_WIDTH/NUMBER_OF_BLOCKS_WIDE) 

def draw_map(grid, grid_blocks):
    BLACK = (255,255,255)
    BLOCK_WIDTH, BLOCK_HEIGHT = 20
    #adds a counter to an iterable and returns it in a form of enumerate object
    #i.e an interable list of objects
    for j, block in enumerate(grid_blocks):
        for i, block_info in enumerate(block):
            rect = pygame.Rect(i*BLOCK_WIDTH, j*BLOCK_WIDTH, BLOCK_WIDTH, BLOCK_HEIGHT)
            pygame.draw.rect(grid, BLACK, rect)

def draw_grid(grid):
    BLACK = (255,255,255)
    for i in range(NUMBER_OF_BLOCKS_WIDE):
        new_height = round(i * BLOCK_HEIGHT)
        new_width = round(i * BLOCK_WIDTH)
        pygame.draw.line(grid, BLACK, (0, new_height), (SCREEN_WIDTH, new_height), 2)
        pygame.draw.line(grid, BLACK, (new_width, 0), (new_width, SCREEN_HEIGHT), 2)
    
    
def color_board(tile_contents):
    WHITE = (0,0,0)
    RED = (255,0,0)
    BLUE = (0,0,255)
    GREEN = (0,255,0)
    GREY = (220,220,220)
    
    tile_color = WHITE
    
    if tile_contents == "1":
        tile_color = GREY
    if tile_contents == "0":
        tile_color = WHITE
    if tile_contents == "3":
        tile_color == BLUE
    if tile_contents == "2":
        tile_color == GREEN
    if tile_contents == "x":
        tile_color == RED
    
    return tile_color

def init_game():
    BLACK = (255,255,255)

    pygame.init()
    WIN_SIZE = [400,400]
    surface = pygame.display.set_mode(WIN_SIZE) #graphics window
    pygame.display.set_caption('AI Escape!') 
    surface.fill(BLACK)
    return surface

def read_map(textfile):
    with open(textfile, 'r') as file:
        grid = file.readlines()
    grid = [line.strip() for line in grid]
    return grid