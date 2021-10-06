## To make it easier to start, make it text based
## Array[Row][Col] = Array[y][x]
## I.e. Row = y, Col = x

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
        self.points = 0
        self.answer_grid = answer_grid 
        ## GUI GRID STUFF
        self.master = master
        self.user_grid = user_grid 
        self.buttons = buttons

        ## Create all of the main containers

        ## Layout all of the main containers

        ## Create the widgets for the top frame

        ## Layout the widgets in the top frame 

        easy_btn = tk.Button(self.master, text = "Easy", command = self.easy)
        easy_btn.grid(row = 0, column = 0, sticky = tk.EW, padx = 5, pady = 5)
        med_btn = tk.Button(self.master, text = "Med", command = self.medium)
        med_btn.grid(row = 0, column = 1, sticky = tk.EW, padx = 5, pady = 5)
        hard_btn = tk.Button(self.master, text = "Hard", command = self.hard)
        hard_btn.grid(row = 0, column = 2, sticky = tk.EW, padx = 5, pady = 5)

    ## Difficulty Functions

    def easy (self):
        self.row = 5
        self.col = 5
        self.create_grid()
        return self.randomize_grid()
    
    def medium (self):
        self.row = 6
        self.col = 6
        self.create_grid()
        return self.randomize_grid()
    
    def hard (self):
        self.row = 6
        self.col = 6
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
                coords = [c, r]
                action_with_arg = partial(self.guess_squares, coords)
                btn = tk.Button(self.master, bg = "black", command = action_with_arg)
                btn.grid(row = r + 1, column = c, padx=5, pady=5, sticky = tk.EW)
                self.buttons[c , r] = btn

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
        print("Answer: ", self.answer_grid)

    ## guess_squares: This is where the user guesses which squares 1s based on the randomized grid
    ## Current Issue: Game should now no longer require user text input, should only be done through clicking
    def guess_squares (self, user_coords):
        btn = self.buttons[user_coords[0], user_coords[1]]
        correct_coords = []
        if (self.points != self.lvl and self.lives > 0):
            ## User guess
            guess_y = user_coords[0]
            guess_x = user_coords[1]
            guess_coord = [guess_x, guess_y]
            if (guess_coord in correct_coords):
                print("You already guessed this correctly, try again")
            ## Correct guess
            elif ((self.answer_grid[guess_x][guess_y]) == 1):
                (self.user_grid[guess_x][guess_y]) = 1
                self.points += 1
                correct_coords.append([guess_x, guess_y])
                print("You guessed correct, keep going")
                print("current grid ", self.user_grid)
                btn.config(bg = "white")
            ## Incorrect guess
            else:
                print("Incorrect, try again")
                btn.config(bg = "red")
                self.lives -= 1
        correct_coords = []
        ## If the user got everything right, they level up 
        if (self.points >= self.lvl):
            print("Moving to next level")
            self.points = 0
            self.lvl += 1
            self.reset_grid()
            ## Winning condition
            if (self.win_game()):
                print("YOU WIN")
                return True
            self.reset_grid()
        ## If they used up all their lives they lose the game
        if (self.lives == 0):
            print("Game over")
            print("Level: ", self.lvl)
            print("Points: ", self.points)
            print("Your Grid ", self.user_grid)
            print("Answer grid ", self.answer_grid)
            return False
    
 
    ## Should reset and delete all the extra buttons once the user levels up 
    ## Currently not tested
    ## Maybe don't delete and recreate the buttons all over again, just reset it so that so you don't create new buttons every single time
    def reset_grid (self):
        for c in range(self.row):
            for r in range(self.col):
                coords = [c, r]
                btn = self.buttons[coords[0], coords[1]]
                btn.config(text = "BLANK")
                btn.destroy()
        self.create_grid()
        self.randomize_grid()

    ## win_game: After the halfway point in the game, the user wins mainly because it doesn't get any more difficult, the colours just get flipped
    ##          This is more efficient than just waiting until the squares change colour 
    def win_game (self):
        half_squares = int((self.row * self.col) / 2)
        if (half_squares <= self.lvl):
            print("You win")
            return True
        return False

root = tk.Tk()
root.geometry('400x400')
root.title("Memory Squares")
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=1)
root.columnconfigure(5, weight=1)
root.columnconfigure(6, weight=1)
#root.rowconfigure(0, weight = 1)
app = Squares_Game(root, [], [], {})
root.mainloop()
#g.start()



