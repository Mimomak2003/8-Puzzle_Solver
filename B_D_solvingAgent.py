from Puzzle import Puzzle
from collections import deque


class Node:
    def __init__(self, value: Puzzle, parent, cost, swappedNum):
        self.value = value
        self.parent = parent
        self.cost = cost
        self.swappedNum = swappedNum


class SolvingAgent:
    def __init__(self, initial_state: Puzzle, BFS_or_DFS: str):
        self.BFS_or_DFS = BFS_or_DFS
        self.lis = deque()
        self.lis.append(Node(initial_state, None, 0, None))

    def checkVisited(self, visited, to_check):
        if visited.get(str(to_check)) == 'f': return True
        return False

    def empty(self, lis: deque):
        return len(lis) == 0

    def solve(self):
        # will contain the final state when the puzzle is solved
        goal: Node = None

        visited = dict()
        max_depth = 0
        while not self.empty(self.lis):
            # the state we are currently exploring
            if self.BFS_or_DFS == "1":
                current = self.lis.popleft()
            elif self.BFS_or_DFS == "2":
                current = self.lis.pop()

            if current.cost > max_depth: max_depth = current.cost
            if self.checkVisited(visited, current.value):
                continue
            visited[str(current.value)] = 'f'

            if current.value.checkSolved():
                # if we reached final state, break out of the loop and set the goal variable to that state
                goal = current
                break

            swaps = current.value.generatePossibleSwaps()  # available numbers to swap
            for i in swaps:  # add each possibility of them to the queue in addition to the cost
                p = current.value.copy()
                p.swap(i)

                if not (self.checkVisited(visited, p)):
                    self.lis.append(Node(p, current, current.cost + 1, i))

        # AFTER BREAKING OUT FROM THE LOOP
        if goal is None:
            # If the goal is still none, then it might be unsolvable.
            raise UnSolvablePuzzleError()
        else:
            path = []
            while True:
                if goal.swappedNum is not None:
                    goal.swappedNum = str(goal.swappedNum)
                    path.append(goal.swappedNum)
                if goal.parent is None:
                    break
                goal = goal.parent

            path.reverse()
            return [path, len(visited), max_depth]

    def printPath(self):
        path = self.lis[0]
        for i in range(len(path), 0, -1):
            print(path[i - 1], end="")
            if not (i == 1):
                print("  ---->  ", end="")


class UnSolvablePuzzleError(Exception):
    """
    The puzzle is unsolvable
    """
    pass
