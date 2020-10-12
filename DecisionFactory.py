import random
#import np

class DecisionFactory:    
    def __init__(self, name, grid):
        self.name = name
        self.directions = [ 'wait', 'up', 'down', 'right', 'left' ]
        self.results = [ 'success', 'failure', 'portal' ]
        self.pos = (random.randint(1,8), random.randint(1,8))
        self.last_result = self.results[0]
        self.last_direction = 'wait'
        self.last_position = self.pos
        grid[self.pos[0]][self.pos[1]] = 2 
        print("AI starting at", self.pos)
        # Note: we have relativistic coordinates recorded here, since the map
        #   is relative to the player's first known and recorded position:
        # self.state.pos = (0, 0)    
        
    def get_decision(self, verbose = True):
        return self.random_direction()    
    
    def random_direction(self):
        #r = random.randint(0,4) # Includes wait state
        r = random.randint(1,4) # Does NOT include wait state
        # Update last direction to be the one just selected:
        self.last_direction = self.directions[r]        
        return self.directions[r]
    
    def put_result(self, result):        
        self.last_result = result
    
#    def test_move(self, r, grid):
#        if r == "up":
#           future_position = (self.pos[0]-1, self.pos[1])
#           if future_position == '2': #wall
#                       DecisionFactory.put_result(1)
#           elif future_position == 'x': #recorded spot
#                       DecisionFactory.put_result(1)
#           elif future_position == '3': #portal
#                       DecisionFactory.put_result(2)
#           else:
#                       DecisionFactory.put_result(0)
#        if r == "down":
#           future_position = (self.pos[0]+1, self.pos[1])
#           if future_position == '2': #wall
#                       DecisionFactory.put_result(1)
#           elif future_position == 'x': #recorded spot
#                       DecisionFactory.put_result(1)
#           elif future_position == '3': #portal
#                       DecisionFactory.put_result(2)
#           else:
#                       DecisionFactory.put_result(0)
#        if r == "left":
#           future_position = (self.pos[0], self.pos[1]-1)
#           if future_position == '2': #wall
#                       DecisionFactory.put_result(1)
#           elif future_position == 'x': #recorded spot
#                       DecisionFactory.put_result(1)
#           elif future_position == '3': #portal
#                       DecisionFactory.put_result(2)
#           else:
#                       DecisionFactory.put_result(0)
#        if r == "right":
#           future_position = (self.pos[0], self.pos[1]+1)
#           if future_position == '2': #wall
#                       DecisionFactory.put_result(1)
#           elif future_position == 'x': #recorded spot
#                       DecisionFactory.put_result(1)
#           elif future_position == '3': #portal
#                       DecisionFactory.put_result(2)
#           else:
#                       DecisionFactory.put_result(0)
#        
    def test_move(self, future_position, board):
        
        if board[future_position[0]][future_position[1]] == 1: 
        # board[player.pos[0]][player.pos[1]] == 1: #wall
            print("wall")
            self.put_result(self.results[1])
            
        elif board[future_position[0]][future_position[1]] == 3:
        #board[player.pos[0]][player.pos[1]] == 3: #portal
            print("portal")
            self.put_result(self.results[2])
            
        else:
            print("success")
            self.put_result(self.results[0])
                
    def spiral(self, grid):
        #left
        future_position = (self.pos[0], self.pos[1]-1)
        print(future_position)
        self.test_move(future_position, grid)
        print(grid)
        if self.last_result == "success":
            self.last_position = (self.pos[0], self.pos[1])
            grid[self.last_position[0]][self.last_position[1]] = 1
            self.pos = future_position
            grid[self.pos[0]][self.pos[1]] = 2
            self.spiral(grid)
        
        elif self.last_result == "portal":
            return False
        
        #up
        else:
            future_position = (self.pos[0]-1, self.pos[1])
            print(future_position)
            self.test_move(future_position, grid)
            print(grid)
            if self.last_result == "success":
                self.last_position = (self.pos[0], self.pos[1])
                grid[self.last_position[0]][self.last_position[1]] = 1
                self.pos = future_position
                grid[self.pos[0]][self.pos[1]] = 2
                self.spiral(grid)
            
            elif self.last_result == "portal":
                return False
            
            #right
            else:
                future_position = (self.pos[0], self.pos[1]+1)
                print(future_position)
                self.test_move(future_position, grid)
                print(grid)
                if self.last_result == "success":
                    self.last_position = (self.pos[0], self.pos[1])
                    grid[self.last_position[0]][self.last_position[1]] = 1
                    self.pos = future_position
                    grid[self.pos[0]][self.pos[1]] = 2
                    self.spiral(grid)
                
                elif self.last_result == "portal":
                    return False
        
                #down
                else:
                    future_position = (self.pos[0]+1, self.pos[1])
                    print(future_position)
                    self.test_move(future_position, grid)
                    print(grid)
                    if self.last_result == "success":
                        self.last_position = (self.pos[0], self.pos[1])
                        grid[self.last_position[0]][self.last_position[1]] = 1
                        self.pos = future_position
                        grid[self.pos[0]][self.pos[1]] = 2
                        self.spiral(grid)
                    
                    elif self.last_result == "portal":
                        return False
                    
                    #recurse
                    else:
                        print("RECURSE")
                        grid[self.last_position[0]][self.last_position[1]] = 0
                        self.pos = self.last_position
                        return False
                        #self.spiral(grid)
                    
                    
                    
                    