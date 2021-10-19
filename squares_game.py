import tkinter as tk
from random import randrange
from functools import partial

class SquaresGame:

    def __init__ (self, master, answer_grid, user_grid, buttons):
        ## GAME BASED STUFF
        self.row = 0
        self.col = 0
        self.lvl = 1
        self.lives = 3
        self.points = 0
        self.answer_grid = answer_grid

        ## GUI GRID STUFF
        self.master = master
        self.user_grid = user_grid 
        self.buttons = buttons

        ## Create all of the main containers, frames arranged from top to bottom
        self.frame1 = tk.Frame(self.master, bg='gray', width = 400, height = 90, pady = 5)
        self.frame2 = tk.Frame(self.master, bg='gray', width = 400, height = 40, pady = 5)
        self.frame3 = tk.Frame(self.master, bg='gray', width = 400, height = 240, pady = 5)
        self.frame4 = tk.Frame(self.master, bg='gray', width = 400, height = 40, pady = 5)
        self.frame5 = tk.Frame(self.master, bg='gray', width = 400, height = 20, pady = 5)

        ## Layout all of the main containers
        self.frame1.grid(row = 0, sticky = tk.EW)
        self.frame2.grid(row = 1, sticky = tk.EW)
        self.frame3.grid(row = 2, sticky = tk.EW)
        self.frame4.grid(row = 3, sticky = tk.EW)
        self.frame5.grid(row = 4, sticky = tk.EW)

        ## Create the widgets for frame 1
        game_title = tk.Label(self.frame1, text='Memory Squares', fg = 'white', bg = 'gray')
        game_title.config(font=("TkDefaultFont, 20"))

        ## Layout the widgets in frame 1
        game_title.grid(row = 0, column = 0, sticky = tk.EW)
        game_title.pack(anchor = 'center')

        ## Create the widgets for frame 2
        easy_diff = partial(self.set_diff, 5)
        med_diff = partial(self.set_diff, 6)
        hard_diff = partial(self.set_diff, 7)

        self.easy_btn = tk.Button(self.frame2, text = "Easy", command = easy_diff)
        self.med_btn = tk.Button(self.frame2, text = "Med", command = med_diff)
        self.hard_btn = tk.Button(self.frame2, text = "Hard", command = hard_diff)

        ## Layout the widgets in frame 2
        self.easy_btn.grid(row = 0, column = 0, sticky = tk.EW, padx = 5, pady = 5)
        self.med_btn.grid(row = 0, column = 1, sticky = tk.EW, padx = 5, pady = 5)
        self.hard_btn.grid(row = 0, column = 2, sticky = tk.EW, padx = 5, pady = 5)

        ## Create the widgets for frame 4
        self.lvl_label = tk.Label(self.frame4, text='Level: ' + str(self.lvl), fg = 'white', bg = 'gray')
        self.lives_label = tk.Label(self.frame4, text='Lives: ' + str(self.lives), fg = 'white', bg = 'gray')

        ## Layout the widgets in frame 4
        self.lvl_label.grid(row = 0, column = 0, sticky = tk.EW)
        self.lives_label.grid(row = 1, column = 0, sticky = tk.EW)

        ## Create the widgets for frame 5
        self.play_again = tk.Button(self.frame5, text = "Play Again", command = self.play)

        ## Layout the widgets in frame 5
        self.play_again.grid(row = 0, column = 0, sticky = tk.EW)
        self.play_again.pack(anchor = 'center')

    ## play_again: Resets the game if you want to play again 
    def play(self):
        self.lvl = 1
        self.lives = 3
        self.easy_btn.config(state = "normal")
        self.med_btn.config(state = "normal")
        self.hard_btn.config(state = "normal")
        for c in range(self.row):
            for r in range(self.col):
                coords = [c, r]
                btn = self.buttons[coords[0], coords[1]]
                btn.destroy()

    ## set_diff: Officially starts the game based on the set difficulty 
    def set_diff(self, num):
        self.row = num
        self.col = num
        self.easy_btn.config(state = "disabled")
        self.med_btn.config(state = "disabled")
        self.hard_btn.config(state = "disabled")
        self.create_grid()

    ## Create_grid: Creates a grid based on user inputs for rows and columns
    def create_grid(self):
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
                btn = tk.Button(self.frame3, bg = "black", width = 5, height = 2, command = action_with_arg)
                btn.grid(row = r + 1, column = c, padx=5, pady=5, sticky = tk.EW)
                btn.config(state = "normal")
                self.buttons[c , r] = btn
        self.randomize_grid()

    ## Randomize_grid: Changes the grid values from 0 to 1 based on level
    ## 0s represent the default squares
    ## 1s represent the squares you need to memorize
    def randomize_grid(self):
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
        self.play_again.config(state = "disabled")
        for c in range(self.row):
            for r in range(self.col):
                coords = [c, r]
                btn = self.buttons[coords[0], coords[1]]
                btn.config(state = "disabled")

    ## black_all: changes the colour of each button to back to black without mutating the values
    def black_all(self):
        self.play_again.config(state = "normal")
        for c in range(self.row):
            for r in range(self.col):
                coords = [c, r]
                btn = self.buttons[coords[0], coords[1]]
                btn.config(bg = "black", state = "normal")
        
    ## guess_squares: This is where the user guesses which squares 1s based on the randomized grid
    ## Current Issue: Game should now no longer require user text input, should only be done through clicking
    def guess_squares(self, user_coords):
        btn = self.buttons[user_coords[0], user_coords[1]]
        correct_coords = []
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
            self.lives_label.config(text='Lives: ' + str(self.lives))
        ## If the user got everything right, they level up 
        if (self.points >= self.lvl):
            print("Moving to next level")
            self.points = 0
            self.lvl += 1
            self.lvl_label.config(text='Level: ' + str(self.lvl))
            ## Winning condition
            half_squares = int((self.row * self.col) / 2)
            if (half_squares <= self.lvl):
                print("You win")
                self.black_all()
                self.disable_all()
                return True
            self.reset_grid()
        ## If they used up all their lives they lose the game
        if (self.lives == 0):
            print("Game over")
            self.black_all()
            self.disable_all()
            return False
    
    ## reset_grid: Should reset and delete all the extra buttons once the user levels up 
    def reset_grid(self):
        for c in range(self.row):
            for r in range(self.col):
                coords = [c, r]
                btn = self.buttons[coords[0], coords[1]]
                btn.destroy()
        self.create_grid()

root = tk.Tk()
root.geometry('400x400')
root.title("Memory Squares")
app = SquaresGame(root, [], [], {})
root.mainloop()


