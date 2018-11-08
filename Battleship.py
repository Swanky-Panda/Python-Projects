from pprint import pprint as pp
from colorama import Fore
import random

Rows = 0
Columns = 0
turns = 0
Answer = "NaN"

print(Fore.RED + """

         VRINCH'S BATTLESHIP SIMULATOR

  (Sink the enemy battleship to win the game).

"""
      + Fore.RESET)

while (Rows > 9) or (Columns > 9) or (Rows <= 0) or (Columns <= 0):
    Rows = int(input(Fore.GREEN + "Enter the number of rows: " + Fore.RESET))
    Columns = int(input(Fore.GREEN + "Enter the number of columns: " + Fore.RESET))
    print("\n")

def create_grid(Rows, Columns):
    #Creates the 2D Data Grid
    grid = []
    for row in range(Rows):
        row = []
        for col in range(Columns):
            row.append(" ")
        grid.append(row)
    return grid

grid = create_grid(Rows,Columns)

def display_grid(grid, Columns):
    #Prints the labels for the grid
    column_names = "abcdefghijklmnopqrstuvwxyz"[:Columns]
    print("  | " + " | ".join(column_names.upper()) + " |")
    for number, row in enumerate(grid):
       print(number + 1, "| " + " | ".join(row) + " |")
    print("\n")

grid = create_grid(Rows, Columns)
display_grid(grid, Columns)

def random_row(grid):
    #Makes a random row integer
    return random.randint(1,len(grid))

def random_col(grid):
    #Makes a random column integer
    return random.randint(1,len(grid[0]))

def update_gridHit(grid, GuessRow, GuessColumn):
    grid[GuessRow-1][GuessColumn-1] = "O"

def update_gridMiss(grid, GuessRow, GuessColumn):
    grid[GuessRow-1][GuessColumn-1] = "X"

ShipRow = random_row(grid)
ShipColumn = random_col(grid)

while (turns != 5):
    GuessRow = int(input(Fore.GREEN + "What row do you guess? " + Fore.RESET))
    GuessColumn = int(input(Fore.GREEN + "What column do you guess? " + Fore.RESET))

    if (GuessRow == ShipRow) and (GuessColumn == ShipColumn):
        turns += 1
        print(Fore.CYAN + "\nYou hit the battleship! Congratulations!\n" + Fore.RESET)
        update_gridHit(grid, GuessRow, GuessColumn)
        display_grid(grid, Columns)
        break

    else:
        if (GuessRow < 1 or GuessRow > Rows) or (GuessColumn < 1 or GuessColumn > Columns):
            #Warning if the guess is out of the board
            print(Fore.RED + "\nOutside the set grid!\n" + Fore.RESET)

        elif (grid[GuessRow-1][GuessColumn-1] == "X"):
            #If "X" is there than print that it missed
            print(Fore.RED + "\nYou guessed that already!\n" + Fore.RESET)

        else:
            #Updates the grid with an "X" saying that you missed the ship
            turns += 1
            print(Fore.RED + "\nYou missed the ship!\n" + Fore.RESET)
            update_gridMiss(grid, GuessRow, GuessColumn)
            display_grid(grid, Columns)

    if (turns >= 5):
        print(Fore.RED + "Game over! Out of turns, it was at: (" + str(ShipRow) + ", " + str(ShipColumn) + ")" + Fore.RESET)