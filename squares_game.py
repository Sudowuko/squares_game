## To make it easier to start, make it text based
## 0 is a white square
## 1 is black square
## have the rows and columns be constant
## Note: Once you have accomplished these things, then you can change it

## current steps
## create a grid 

from random import randrange

class Squares_Game:

    def __init__ (self, row, col, lvl, grid):
        self.row = int(row)
        self.col = int(col)
        self.lvl = int(lvl)
        self.grid = grid
    
    ##Create_grid: Creates a grid based on user inputs for rows and columns
    ##Errors I need to fix: Handle invalid data entries such as no integer inputs
    def create_grid (self):
        print("the grid will have", self.row, "rows")
        print("the grid will have", self.col, "columns")
        self.grid = []
        for c in range(self.row):
            self.grid.append([])
            for r in range(self.col):
                self.grid[-1].append(0)
                #print("0", end='')
            #print("0")
        #print(self.grid)
            
    ## Randomize_grid: Changes the grid values from 0 to 1 based on level
    ## 1s represent the number you need to memorize for the game
    def randomize_grid (self):
        start_lvl = 0

        #for i in range(int(self.lvl)):
        while (start_lvl != self.lvl):
            rand_x = randrange(self.row)
            rand_y = randrange(self.col)
            if ((self.grid[rand_x][rand_y]) == 0):
                (self.grid[rand_x][rand_y]) = 1
                start_lvl += 1

        print("random grid")
        print(self.grid)
        
# Eventually turn this into difficulties 
# I.e. Easy, medium, and hard
r = input("Number of rows? ")
c = input("Number of columns ")

g = Squares_Game(r, c, 9, [])
g.create_grid()
g.randomize_grid()

