## To make it easier to start, make it text based
## Array[Row][Col] = Array[y][x]
## I.e. Row = y, Col = x

import tkinter as tk
from random import randrange
from functools import partial

class SquaresGame:

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
        self.top_frame = tk.Frame(self.master, bg='gray', width = 400, height = 90, pady = 5)
        self.mid_frame = tk.Frame(self.master, bg='gray', width = 400, height = 40, pady = 5)
        self.bot_frame = tk.Frame(self.master, bg='gray', width = 400, height = 240, pady = 5)

        ## Layout all of the main containers
        self.top_frame.grid(row = 0, sticky = tk.EW)
        self.mid_frame.grid(row = 1, sticky = tk.EW)
        self.bot_frame.grid(row = 2, sticky = tk.EW)
        
        ## Create the widgets for the top frame
        game_title = tk.Label(self.top_frame, text='Memory Squares')
        game_title.config(font=("TkDefaultFont, 20"))

        ## Layout the widgets in the top frame 
        game_title.grid(row = 0, column = 0, sticky = tk.EW)
        game_title.pack(anchor = 'center')

        ## Create the widgets for the mid frame
        easy_btn = tk.Button(self.mid_frame, text = "Easy", command = self.easy)
        med_btn = tk.Button(self.mid_frame, text = "Med", command = self.medium)
        hard_btn = tk.Button(self.mid_frame, text = "Hard", command = self.hard)

        ## Layout the widgets in the mid frame
        easy_btn.grid(row = 0, column = 0, sticky = tk.EW, padx = 5, pady = 5)
        med_btn.grid(row = 0, column = 1, sticky = tk.EW, padx = 5, pady = 5)
        hard_btn.grid(row = 0, column = 2, sticky = tk.EW, padx = 5, pady = 5)
        
    ## Difficulty Functions

    def easy(self):
        self.row = 4
        self.col = 4
        self.create_grid()
    
    def medium(self):
        self.row = 6
        self.col = 6
        self.create_grid()
    
    def hard(self):
        self.row = 7
        self.col = 7
        self.create_grid()

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
                coords = [c, r]
                action_with_arg = partial(self.guess_squares, coords)
                btn = tk.Button(self.bot_frame, bg = "black", width = 5, height = 2, command = action_with_arg)
                btn.grid(row = r + 1, column = c, padx=5, pady=5, sticky = tk.EW)
                self.buttons[c , r] = btn
        self.randomize_grid()

    ## Randomize_grid: Changes the grid values from 0 to 1 based on level
    ## 0s represent the default squares
    ## 1s represent the squares you need to memorize
    def randomize_grid (self):
        start_lvl = 0
        while (start_lvl != self.lvl):
            rand_y = randrange(self.row)
            rand_x = randrange(self.col)
            if ((self.answer_grid[rand_x][rand_y]) == 0):
                self.answer_grid[rand_x][rand_y] = 1
                btn = self.buttons[rand_y,rand_x]
                btn.config(bg = "blue")
                start_lvl += 1
        print("Answer: ", self.answer_grid)
        self.disable_all()
        self.master.after(3000, self.black_all)
    
    ## disable: Makes all the buttons unclickable 
    def disable_all(self):
        for c in range(self.row):
            for r in range(self.col):
                coords = [c, r]
                btn = self.buttons[coords[0], coords[1]]
                btn.config(state = "disabled")

    ## black_all: changes the colour of each button to back to black without mutating the values
    def black_all(self):
        for c in range(self.row):
            for r in range(self.col):
                coords = [c, r]
                btn = self.buttons[coords[0], coords[1]]
                btn.config(bg = "black", state = "normal")
        
    ## guess_squares: This is where the user guesses which squares 1s based on the randomized grid
    ## Current Issue: Game should now no longer require user text input, should only be done through clicking
    def guess_squares (self, user_coords):
        btn = self.buttons[user_coords[0], user_coords[1]]
        correct_coords = []
        if (self.points != self.lvl and self.lives > 0):
            ## User guess
            guess_y = user_coords[0]
            guess_x = user_coords[1]
            ## Correct guess
            if ((self.answer_grid[guess_x][guess_y]) == 1):
                (self.user_grid[guess_x][guess_y]) = 1
                self.points += 1
                correct_coords.append([guess_x, guess_y])
                btn.config(bg = "white")
            ## Incorrect guess
            else:
                btn.config(bg = "red")
                self.lives -= 1
        correct_coords = []
        ## If the user got everything right, they level up 
        if (self.points >= self.lvl):
            print("Moving to next level")
            self.points = 0
            self.lvl += 1
            ## Winning condition
            half_squares = int((self.row * self.col) / 2)
            if (half_squares <= self.lvl):
                print("You win")
                self.reset_grid()
                self.disable_all()
                return True
            self.reset_grid()
        ## If they used up all their lives they lose the game
        if (self.lives == 0):
            print("Game over")
            print("Level: ", self.lvl)
            print("Points: ", self.points)
            print("Your Grid ", self.user_grid)
            print("Answer grid ", self.answer_grid)
            self.disable_all()
            return False
    
    ## reset_grid: Should reset and delete all the extra buttons once the user levels up 
    def reset_grid (self):
        for c in range(self.row):
            for r in range(self.col):
                coords = [c, r]
                btn = self.buttons[coords[0], coords[1]]
                btn.config(text = "BLANK")
                btn.destroy()
        self.create_grid()

root = tk.Tk()
root.geometry('400x400')
root.title("Memory Squares")
app = SquaresGame(root, [], [], {})
root.mainloop()


