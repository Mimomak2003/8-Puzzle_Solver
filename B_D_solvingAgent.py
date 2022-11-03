from bds_puzzle import Puzzle
from collections import deque


class Node:
    def __init__(self, value: Puzzle, parent, cost, swappedNum):
        self.value = value
        self.parent = parent
        self.cost = cost
        self.swappedNum = swappedNum


class solving_agent:
    def __init__(self, initial_state: Puzzle, BFS_or_DFS: str):  # insert b > bfs and d > dfs
        self.BFS_or_DFS = BFS_or_DFS.lower()
        self.lis = deque()
        self.lis.append(Node(initial_state, None, 0, None))

    def checkVisited(self, visited, to_check):
        for i in visited:
            if i.equals(to_check):
                return True
        return False

    def empty(self, lis: deque):
        return len(lis) == 0

    def solve(self):
        # will contain the final state when the puzzle is solved
        goal: Node = None
        row0 = [0, 1, 2]
        row1 = [3, 4, 5]
        row2 = [6, 7, 8]
        goalPuzzle = Puzzle(row0, row1, row2)

        visited = []
        while not self.empty(self.lis):
            # the state we are currently exploring
            if self.BFS_or_DFS == "b":
                current = self.lis.popleft()
            elif self.BFS_or_DFS == "d":
                current = self.lis.pop()

            #current.value.printP()
            #depth = current.cost
            #print(depth)

            if self.checkVisited(visited, current.value):
                continue
            visited.append(current.value)

            if current.value.solved():
                # if we reached final state, break out of the loop and set the goal variable to that state
                goal = current
                break

            swaps = current.value.generatePossibleSwaps()  # available numbers to swap
            for i in swaps:  # add each possibility of them to the queue in addition to the cost
                p = current.value.copy()
                p.swaps(i)

                if not (self.checkVisited(visited, p)) and current.cost != 20:
                    self.lis.append(Node(p, current, current.cost + 1, i))

        # AFTER BREAKING OUT FROM THE LOOP
        if goal is None:
            # If the goal is still none, then it might be unsolvable.
            raise UnSolvablePuzzleError()
        else:
            goal_cost = goal.cost
            path = []
            while True:
                if goal.swappedNum is not None:
                    goal.swappedNum = str(goal.swappedNum)
                    path.append(goal.swappedNum)
                if goal.parent is None:
                    break
                goal = goal.parent

            return [path, goal_cost]

    def printPath(self, lis):
        path = lis[0]
        for i in range(len(path), 0, -1):
            print(path[i - 1], end="")
            if not (i == 1):
                print("  ---->  ", end="")


class UnSolvablePuzzleError(Exception):
    """
    The puzzle is unsolvable
    """
    pass


if __name__ == '__main__':
    row3 = ['1', '2', '5']
    row4 = ['3', '4', '8']
    row5 = ['6', '0', '7']
    p2 = Puzzle(row3, row4, row5)
    dps = solving_agent(p2, "d")
    solution = dps.solve()
    print(solution[1])
    dps.printPath(solution)
