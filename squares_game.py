## To make it easier to start, make it text based
## 0 is a white square
## 1 is black square
## have the rows and columns be constant
## Note: Once you have accomplished these things, then you can change it
## default python 2D grids are backwards
## Array[Row][Col] = Array[y][x]
## I.e. Row = y, Col = x

## Current steps: 
##    Convert text form to GUI form 
##    Add in score? 

from random import randrange

class Squares_Game:

    def __init__ (self, row, col, lvl, lives, answer_grid, user_grid):
        self.row = int(row)
        self.col = int(col)
        self.lvl = int(lvl)
        self.lives = int(lives)
        self.answer_grid = answer_grid 
        self.user_grid = user_grid 
    
    ## Function to start the game
    def start (self):
        diff = input("Difficulty? ")
        ## Easy
        if (diff == "e"):
            self.row = 3
            self.col = 3
        ## Medium
        elif (diff == "m"):
            self.row = 4
            self.col = 4
        ## Hard
        elif (diff == "h"):
            self.row = 5
            self.col = 5
        return self.level_up()

    ##Create_grid: Creates a grid based on user inputs for rows and columns
    def create_grid (self):
        self.answer_grid = []
        self.user_grid = []
        for c in range(self.row):
            self.answer_grid.append([])
            self.user_grid.append([])
            for r in range(self.col):
                self.answer_grid[-1].append(0)
                self.user_grid[-1].append(0)

    ## Randomize_grid: Changes the grid values from 0 to 1 based on level
    ## 1s represent the number you need to memorize for the game
    def randomize_grid (self):
        start_lvl = 0
        while (start_lvl != self.lvl):
            rand_y = randrange(self.row)
            rand_x = randrange(self.col)
            if ((self.answer_grid[rand_x][rand_y]) == 0):
                (self.answer_grid[rand_x][rand_y]) = 1
                start_lvl += 1
        print(self.answer_grid)
    
    ## guess_squares: This is where the user guesses which squares 1s based on the randomized grid
    def guess_squares (self):
        points = 0
        correct_coords = []
        while (points != self.lvl and self.lives > 0):
            ## User guess
            guess_y = int(input("X Coord "))
            guess_x = int(input("Y Coord "))
            if (guess_x >= self.col or guess_y >= self.row):
                print("Coordinate out of range, try again")
                continue
            guess_coord = [guess_x, guess_y]
            if (guess_coord in correct_coords):
                print("You already guessed this correctly, try again")
            ## Correct guess
            elif ((self.answer_grid[guess_x][guess_y]) == 1):
                (self.user_grid[guess_x][guess_y]) = 1
                points += 1
                correct_coords.append([guess_x, guess_y])
                print("You guessed correct, keep going")
                print("current grid ", self.user_grid)
            ## Incorrect guess
            else:
                print("Incorrect, try again")
                self.lives -= 1
        correct_coords = []
        ## If the user got everything right, they level up 
        if (points == self.lvl):
            print("Moving to next level")
            points = 0
            self.lvl += 1
            ## Winning condition
            if (self.win_game()):
                return True
            return self.level_up()
        ## If they used up all their lives they lose the game
        else:
            print("Game over")
            print("Your Grid ", self.user_grid)
            print("Answer grid ", self.answer_grid)
            return False
            
     ## Steps that allow you to move to the next level
    def level_up (self):
        self.create_grid()
        self.randomize_grid()
        self.guess_squares()
    
    ## win_game: After the halfway point in the game, the user wins mainly because it doesn't get any more difficult, the colours just get flipped
    ##          This is more efficient than just waiting until the squares change colour 
    def win_game (self):
        half_squares = int((self.row * self.col) / 2)
        print("half", half_squares)
        print("level", self.lvl)
        if (half_squares <= self.lvl):
            print("You win")
            return True
        return False

g = Squares_Game(0, 0, 1, 3, [], [])
g.start()

