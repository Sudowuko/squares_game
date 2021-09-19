## To make it easier to start, make it text based
## 0 is a white square
## 1 is black square
## have the rows and columns be constant
## Note: Once you have accomplished these things, then you can change it

## current steps
## create a grid 

from random import randrange

class Squares_Game:

    def __init__ (self, row, col, lvl, lives, answer_grid, user_grid):
        self.row = int(row)
        self.col = int(col)
        self.lvl = int(lvl)
        self.lives = int(lives)
        self.answer_grid = answer_grid 
        self.user_grid = user_grid 
        
    
    ##Create_grid: Creates a grid based on user inputs for rows and columns
    ##Errors I need to fix: Handle invalid data entries such as no integer inputs
    def create_grid (self):
        print("the grid will have", self.row, "rows")
        print("the grid will have", self.col, "columns")
        self.answer_grid = []
        self.user_grid = []
        for c in range(self.col):
            self.answer_grid.append([])
            self.user_grid.append([])
            for r in range(self.row):
                self.answer_grid[-1].append(0)
                self.user_grid[-1].append(0)

            
    ## Randomize_grid: Changes the grid values from 0 to 1 based on level
    ## 1s represent the number you need to memorize for the game
    def randomize_grid (self):
        start_lvl = 0
        while (start_lvl != self.lvl):
            rand_x = randrange(self.row)
            rand_y = randrange(self.col)
            if ((self.answer_grid[rand_x][rand_y]) == 0):
                (self.answer_grid[rand_x][rand_y]) = 1
                start_lvl += 1
        print("random grid")
        print(self.answer_grid)
    
    ## guess_squares: This is where the user guesses which squares 1s based on the randomized grid
    ## ideally I need another blank grid 
    ## current problem: You can guess the same squares you already got correct [Fixed?]
    ##                  List index out of range
    ##                  Values ares still flipped :(
    def guess_squares (self):
        lives = 0
        points = 0
        correct_coords = []
        while (points != self.lvl and lives < 3):
            ## User guess
            guess_x = int(input("X Coord "))
            guess_y = int(input("Y Coord "))
            guess_coord = [guess_x, guess_y]
            ## Correct guess
            if ((self.answer_grid[guess_x][guess_y]) == 1 and guess_coord not in correct_coords):
                (self.user_grid[guess_x][guess_y]) = 1
                points += 1
                correct_coords.append([guess_x, guess_y])
                print("You guessed correct, keep going")
                print("current grid ", self.user_grid)
            ## Incorrect guess
            else:
                print("Incorrect, try again")
                lives += 1
        ## If the user got everything right, they level up 
        if (points == self.lvl):
            print("Moving to next level")
            self.lvl += 1
        ## If they used up all their lives they lose the game
        else:
            print("Game over")
            print("Your Grid ", self.user_grid)
            print("Answer grid ", self.answer_grid)
    
    def difficulty (self):
        diff = input("Difficulty? ")
        if (diff == "e"):
            self.row = 3
            self.col = 3
        elif (diff == "m"):
            self.row = 4
            self.col = 4
        elif (diff == "h"):
            self.row = 5
            self.col = 5
        self.level_up()

    def level_up (self):
        self.create_grid()
        self.randomize_grid()
        self.guess_squares()
        print()

# Eventually turn this into difficulties 
# I.e. Easy, medium, and hard
#r = input("Number of rows? ")
#c = input("Number of columns ")

g = Squares_Game(0, 0, 3, 3, [], [])
g.difficulty()
#g.create_grid()
#g.randomize_grid()
#g.guess_squares()

