import random
#import np

class DecisionFactory:    
    def __init__(self, name, grid):
        self.name = name
        self.directions = [ 'wait', 'up', 'down', 'right', 'left' ]
        self.results = [ 'success', 'failure', 'portal' ]
        self.last_position = grid[0][0]
        self.last_result = self.results[0]
        self.last_direction = 'wait'
        self.pos = (random.randint(1,8), random.randint(1,8))
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
        
#    def test_move(self, newPos, obj):
#        if newPos == 1:
#            #return 'failure'
#            self.put_result(1)
#        elif newPos == 3:
#            #return 'portal'
#            self.put_result(2)
#        else:
#            #return 'success'
#            self.put_result(0)
    
#    def test_move(self, r, grid):
#        if r == "up":
#           future_position = self.pos
#           #grid[[self.pos[0]-1][self.pos[1]]]
#           if future_position == 1: #wall
#                       self.put_result(1)
#           elif future_position == 3: #portal
#                       self.put_result(2)
#           else:
#                       self.put_result(0)
#        if r == "down":
#           future_position = self.pos
#           #grid[[self.pos[0]+1][self.pos[1]]]
#           if future_position == 1: #wall
#                       self.put_result(1)
#           elif future_position == 3: #portal
#                       self.put_result(2)
#           else:
#                       self.put_result(0)
#        if r == "left":
#           future_position = self.pos 
#           #grid[[self.pos[0]][self.pos[1]-1]]
#           if future_position == 1: #wall
#                       self.put_result(1)
#           elif future_position == 3: #portal
#                       self.put_result(2)
#           else:
#                       self.put_result(0)
#        if r == "right":
#           future_position = self.pos
#           #grid[[self.pos[0]][self.pos[1]+1]]
#           if future_position == 1: #wall
#                       self.put_result(1)
#           elif future_position == 3: #portal
#                       self.put_result(2)
#           else:
#                       self.put_result(0)
        
    def move(self, r, grid):
        future_position = grid[self[0]+1][self[1]]
        DecisionFactory.test_move("left", self, grid, future_position)
        if self.last_result == "success":
            self.last_step = grid[self[0]][self[1]]
            self.position = future_position
            DecisionFactory.move(self, grid)
        else:
            future_position = grid[self[0]-1][self[1]]
            DecisionFactory.test_move("up", self, grid)
            if self.last_result == "success":
                self.last_step = grid[self[0]][self[1]]
                self.position = future_position
                DecisionFactory.move(self, grid)
            else:
                future_position = grid[self[0]][self[1]+1]
                DecisionFactory.test_move(self, "right", grid)
                if self.last_result == "success":
                    self.last_step = grid[self[0]][self[1]]
                    self.position = future_position
                    DecisionFactory.move(self, grid)
                else:
                    future_position = grid[self[0]+1][self[1]]
                    DecisionFactory.test_move("down", self, grid)
                    if self.last_result == "success":
                        self.last_step = grid[self[0]][self[1]]
                        self.position = future_position
                        DecisionFactory.move(self, grid)
                    else:
                        self.position = self.last_position
                        #mark as 0 instead of 1
                        DecisionFactory.move(self, grid)

                       
