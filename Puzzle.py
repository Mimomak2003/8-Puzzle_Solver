class Puzzle():
    def __init__(self, rows: list):
        self.rows = [rows[:3], rows[3:6], rows[6:]]
        self.zero_position = self.findNum('0')

    def findNum(self, num: str):
        """
        Finds the position of a given number in the puzzle's matrix.
        """
        for i in range(0, 3):
            try:
                # Returns the x, y coordinates if the number was in row i.
                return [i, self.rows[i].index(num)]
            except ValueError:
                pass

    def swap(self, num: str):
        """
        Swaps a given number with the '0' mark if possible, else raises a ValueError.
        """
        positions = [ # List of the four possiblities of swapping.
            [self.zero_position[0] - 1, self.zero_position[1]],
            [self.zero_position[0] + 1, self.zero_position[1]],
            [self.zero_position[0], self.zero_position[1] - 1],
            [self.zero_position[0], self.zero_position[1] + 1]
        ]
        num_position = self.findNum(num) # Position of the number we are swapping with the zero.

        if num_position not in positions:
            # If the number is not at the right, left, up or down from the zero.
            raise ValueError("The value entered is not in a place that can be swapped.")
        
        # Swap the two blocks
        self.rows[self.zero_position[0]][self.zero_position[1]], self.rows[num_position[0]][num_position[1]] = \
            self.rows[num_position[0]][num_position[1]], self.rows[self.zero_position[0]][self.zero_position[1]]

        # Update the position of the zero to its new position.
        self.zero_position = num_position

    def generatePossibleSwaps(self):
        """
        Returns a list of numbers that can be swapped next.
        """
        positions = [ # List of the four possiblities of swapping.
            [self.zero_position[0] - 1, self.zero_position[1]],
            [self.zero_position[0] + 1, self.zero_position[1]],
            [self.zero_position[0], self.zero_position[1] - 1],
            [self.zero_position[0], self.zero_position[1] + 1]
        ]
        # Returns only the ones that are possible in our case.
        return {self.rows[i[0]][i[1]] for i in positions if -1 not in i and 3 not in i}

    def checkSolved(self):
        return self.rows[0] == ['0','1','2'] and self.rows[1] == ['3','4','5'] and self.rows[2] == ['6','7','8']

    def copy(self):
        x = self.rows[0].copy()
        x.extend(self.rows[1])
        x.extend(self.rows[2])
        return Puzzle(x)

    def equals(self, another_puzzle):
        return self.rows == another_puzzle.rows

    def printPuzzle(self):
        x = "-------------"
        y = "| {} | {} | {} |"
        print(x)
        for i in range(0, 3):
            z = self.rows[i]
            print(y.format(z[0], z[1], z[2]))
            print(x)