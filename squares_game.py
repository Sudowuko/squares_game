## To make it easier to start, make it text based
## 0 is a white square
## 1 is black square
## have the rows and columns be constant
## Note: Once you have accomplished these things, then you can change it

## current steps
## create a grid 

class Squares_Game:

    def __init__ (self, row, col):
        self.row = row
        self.col = col
    
    ##Current step: Create a grid based on rows and columns
    def create_grid (self):
        print("the grid will have", self.row, "rows")
        print("the grid will have", self.col, "columns")
        for c in range(0, int(self.col)):
            for r in range(0,int(self.row) - 1):
                print("0", end='')
            print("0")
        
# Eventually turn this into difficulties 
# I.e. Easy, medium, and hard
r = input("Number of rows? ")
c = input("Number of columns ")
3
4
g = Squares_Game(r,c)
g.create_grid()

