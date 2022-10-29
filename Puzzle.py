class Puzzle():
    def __init__(self, row0: list, row1: list, row2: list):
        self.rows = [row0, row1, row2]
        self.xposition = self.findNum('x')

    def findNum(self, num: str):
        """
        Finds the position of a given number in the puzzle's matrix.
        """
        for i in range(0, 3):
            try:
                return [i, self.rows[i].index(num)]
            except ValueError:
                pass

    def swap(self, num: str):
        """
        Swaps a given number with the 'x' mark if possible, else raises a ValueError.
        """
        positions = [
            [self.xposition[0] - 1, self.xposition[1]],
            [self.xposition[0] + 1, self.xposition[1]],
            [self.xposition[0], self.xposition[1] - 1],
            [self.xposition[0], self.xposition[1] + 1]
        ]
        num_position = self.findNum(num)

        if num_position not in positions:
            raise ValueError("The value entered is not in a place that can be swapped.")
        
        self.rows[self.xposition[0]][self.xposition[1]], self.rows[num_position[0]][num_position[1]] = \
            self.rows[num_position[0]][num_position[1]], self.rows[self.xposition[0]][self.xposition[1]]

        self.xposition = num_position

    def checkSolved(self):
        return self.rows[0] == ['x','1','2'] and self.rows[1] == ['3','4','5'] and self.rows[2] == ['6','7','8']

    def printPuzzle(self):
        x = "-------------"
        y = "| {} | {} | {} |"
        print(x)
        for i in range(0, 3):
            z = self.rows[i]
            print(y.format(z[0], z[1], z[2]))
            print(x)