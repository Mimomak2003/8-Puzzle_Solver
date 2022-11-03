class Puzzle:
    zero_position = []

    def __init__(self, rows: list):
        row0 = rows[:3]
        row1 = rows[3:6]
        row2 = rows[6:]
        row00 = []
        row11 = []
        row22 = []
        for i in row0:
            row00.append(int(i))
        for i in row1:
            row11.append(int(i))
        for i in row2:
            row22.append(int(i))
        self.rows = [row00, row11, row22]
        self.zero_position = self.findNum(0)

    def findNum(self, num: str):
        num = int(num)
        """
        Finds the position of a given number in the puzzle's matrix.
        """
        for i in range(0, 3):
            try:
                # Returns the x, y coordinates if the number was in row i.
                return [i, self.rows[i].index(num)]
            except ValueError:
                pass

    def swaps(self, num: str):
        positions = [
            [self.zero_position[0] - 1, self.zero_position[1]],
            [self.zero_position[0] + 1, self.zero_position[1]],
            [self.zero_position[0], self.zero_position[1] - 1],
            [self.zero_position[0], self.zero_position[1] + 1]
        ]
        num_position = self.findNum(num)  # Position of the number we are swapping with the zero.

        if num_position not in positions:
            # If the number is not at the right, left, up or down from the zero.
            pass
        else:  # Swap the two blocks
            self.rows[self.zero_position[0]][self.zero_position[1]], self.rows[num_position[0]][num_position[1]] = \
                self.rows[num_position[0]][num_position[1]], self.rows[self.zero_position[0]][self.zero_position[1]]

        # Update the position of the zero to its new position.
        self.zero_position = num_position

    def solved(self):
        return (self.rows[0] == [0, 1, 2]) and (self.rows[1] == [3, 4, 5]) and (self.rows[2] == [6, 7, 8])

    def printP(self):
        x = "-------------"
        print(x)
        for i in range(0, 3):
            y = 0
            print("| %d | %d | %d |" % (self.rows[i][y], self.rows[i][y + 1], self.rows[i][y + 2]))
            print(x)

    def generatePossibleSwaps(self):
        """
        Returns a list of numbers that can be swapped next.
        """
        if not self.solved():
            positions = [  # List of the four possiblities of swapping.
                [self.zero_position[0] - 1, self.zero_position[1]],
                [self.zero_position[0] + 1, self.zero_position[1]],
                [self.zero_position[0], self.zero_position[1] - 1],
                [self.zero_position[0], self.zero_position[1] + 1]
            ]
            # Returns only the ones that are possible in our case.
            num_can_swap = []
            for i in range(0, 4):
                if (positions[i][0] < 0) or (positions[i][1] < 0) or (positions[i][0] > 2) or (positions[i][1] > 2):
                    pass
                else:
                    num_can_swap.append(self.rows[positions[i][0]][positions[i][1]])
            return num_can_swap
        else:
            return None

    def copy(self):
        x = self.rows[0].copy()
        x.extend(self.rows[1])
        x.extend(self.rows[2])
        return Puzzle(x)

    def equals(self, another_puzzle):
        return self.rows == another_puzzle.rows
