
# sudoku puzzles gotten from https://dingo.sbs.arizona.edu/~sandiway/sudoku/examples.html

import os
import random
from tile import Tile

class SudokuReader:

    def __init__(self, difficulty):

        path, dirs, files = next(os.walk(os.getcwd() + "/" + difficulty))
        file_count = len(files)

        self.selection = random.randint(1, file_count)

        puzzle = open(difficulty + "/" + str(self.selection), 'r')
        rows = puzzle.readlines()

        self.tilesList = []

        for row in range(0, 9):
            self.tilesList.append([])
            for col in range(0, 9):
                sub = rows[row][2*col : 2*col + 2]
                if sub[1] == '!':
                    self.tilesList[row].append(Tile(row, col, sub[0], True))
                else:
                    self.tilesList[row].append(Tile(row, col, sub[0]))


    def getTiles(self):
        return self.tilesList
    
