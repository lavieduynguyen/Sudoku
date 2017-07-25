from random import choice, choices
from copy import copy


class SudokuGenerator():
    def __init__(self):
        self.size = 9
        self.solution = []
        self.puzzle = []


    def initiate_solution(self):
        self.solution = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(0)
            self.solution.append(row)


    def initiate_puzzle(self):
        self.puzzle = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(0)
            self.puzzle.append(row)


    def generate_solution(self):
        if not self.solution:
            self.initiate_solution()

        x = y = 0
        blocks = (range(0, 3), range(3, 6), range(6, 9))
        while x < self.size:
            domain = list(range(1, 10))

            for i in range(9):
                if self.solution[x][i] in domain:
                    domain.remove(self.solution[x][i])
                if self.solution[i][y] in domain:
                    domain.remove(self.solution[i][y])
            
            for block in blocks:
                if x in block:
                    block_x = block
                if y in block:
                    block_y = block

            for i in block_x:
                for j in block_y:
                    if self.solution[i][j] in domain:
                        domain.remove(self.solution[i][j])

            if not domain:
                y -= 1
                if y < 0:
                    y = self.size - 1
                    x -= 1
                self.solution[x][y] = 0
                continue

            self.solution[x][y] = choice(domain)

            y += 1
            if y >= self.size:
                y = 0
                x += 1


    def generate_puzzle(self, missing_sqr=25):
        if not self.solution:
            self.generate_solution()

        self.puzzle = copy(self.solution)
        domain = list(range(9))
        count = 0
        while count < missing_sqr:
            x, y = choices(domain)
            if self.puzzle[x][y] == 0:
                continue
            self.puzzle[x][y] = 0
            count += 1

