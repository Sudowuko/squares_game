## To make it easier to start, make it text based
## 0 is a white square
## 1 is black square
## Array[Row][Col] = Array[y][x]
## I.e. Row = y, Col = x

## Current steps: 
##    Figure out how to put Tkinter functions directly into the class

## Using the Tkinter library to build the GUI
import tkinter as tk
from random import randrange
from functools import partial

class Squares_Game:

    def __init__ (self, master, answer_grid, user_grid, buttons):
        ## GAME BASED STUFF
        self.row = 0
        self.col = 0
        self.lvl = 1
        self.lives = 10
        self.answer_grid = answer_grid 
        ## GUI GRID STUFF
        self.master = master
        self.user_grid = user_grid 
        self.start_button = tk.Button(master, text = "Start", command=self.start)
        self.start_button.grid(row = 0, column = 0)
        self.buttons = buttons

    ## Function to start the game
    def start (self):
       # action_with_arg = partial(self.set_diff, coords)
        easy_btn = tk.Button(self.master, text = "EASY", command = self.easy)
        easy_btn.grid(row = 0, column = 0)
        med_btn = tk.Button(self.master, text = "MEDIUM", command = self.medium)
        med_btn.grid(row = 1, column = 0)
        hard_btn = tk.Button(self.master, text = "HARD", command = self.hard)
        hard_btn.grid(row = 2, column = 0)
    
    ## Difficulty Functions

    def easy (self):
        self.row = 3
        self.col = 3
        self.create_grid()
        return self.randomize_grid()
    
    def medium (self):
        self.row = 4
        self.col = 4
        self.create_grid()
        return self.randomize_grid()
    
    def hard (self):
        self.row = 5
        self.col = 5
        self.create_grid()
        return self.randomize_grid()

    ##Create_grid: Creates a grid based on user inputs for rows and columns
    ## Should create grid based on difficulty user selected
    ## Creates data values for the grid
    def create_grid (self):
        self.answer_grid = []
        self.user_grid = []
        for c in range(self.row):
            self.answer_grid.append([])
            self.user_grid.append([])
            for r in range(self.col):
                self.answer_grid[-1].append(0)
                self.user_grid[-1].append(0)
               # coord = str(c) + "X " + str(r) +"Y" 
                coords = [c, r]
                action_with_arg = partial(self.guess_squares, coords)
                btn = tk.Button(self.master, text = 'BLANK', command = action_with_arg)
                btn.grid(row = r, column = c)
                self.buttons[c , r] = btn

    ## Randomize_grid: Changes the grid values from 0 to 1 based on level
    ## 1s represent the number you need to memorize for the game
    def randomize_grid (self):
        self.create_grid()
        start_lvl = 0
        while (start_lvl != self.lvl):
            rand_y = randrange(self.row)
            rand_x = randrange(self.col)
            if ((self.answer_grid[rand_x][rand_y]) == 0):
                (self.answer_grid[rand_x][rand_y]) = 1
                start_lvl += 1
        print("Answer: ", self.answer_grid)

    ## guess_squares: This is where the user guesses which squares 1s based on the randomized grid
    ## Current Issue: Game should now no longer require user text input, should only be done through clicking
    def guess_squares (self, user_coords):
        btn = self.buttons[user_coords[0], user_coords[1]]
        points = 0
        correct_coords = []
        if (points != self.lvl and self.lives > 0):
            ## User guess
            guess_y = user_coords[0]
            guess_x = user_coords[1]
            guess_coord = [guess_x, guess_y]
            if (guess_x >= self.col or guess_y >= self.row):
                print("Coordinate out of range, try again")
            elif (guess_coord in correct_coords):
                print("You already guessed this correctly, try again")
            ## Correct guess
            elif ((self.answer_grid[guess_x][guess_y]) == 1):
                (self.user_grid[guess_x][guess_y]) = 1
                points += 1
                correct_coords.append([guess_x, guess_y])
                print("You guessed correct, keep going")
                print("current grid ", self.user_grid)
                btn.config(text = "CORRECT")
            ## Incorrect guess
            else:
                print("Incorrect, try again")
                btn.config(text = "WRONG")
                self.lives -= 1
        correct_coords = []
        ## If the user got everything right, they level up 
        if (points >= self.lvl):
            print("Moving to next level")
            points = 0
            self.lvl += 1
            self.reset_grid()
            ## Winning condition
            if (self.win_game()):
                return True
            return self.randomize_grid
        ## If they used up all their lives they lose the game
        if (self.lives == 0):
            print("Game over")
            print("Level: ", self.lvl)
            print("Your Grid ", self.user_grid)
            print("Answer grid ", self.answer_grid)
            return False
    
 
    ## Should reset and delete all the extra buttons once the user levels up 
    ## Currently not tested
    ## Maybe don't delete and recreate the buttons all over again, just reset it so that so you don't create new buttons every single time
    def reset_grid (self):
        self.create_grid()
        for c in range(self.row):
            for r in range(self.col):
               # coord = str(c) + "X " + str(r) +"Y" 
                coords = [c, r]
               # action_with_arg = partial(self.guess_squares, coords)
                btn = self.buttons[coords[0], coords[1]]
                btn.config(text = "BLANK")
                btn.forget()    

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

root = tk.Tk()
root.geometry('400x400')
root.title("Memory Squares")
app = Squares_Game(root, [], [], {})
root.mainloop()
#g.start()



