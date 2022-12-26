from Puzzle import Puzzle
from collections import deque


class Node:
    def __init__(self, value: Puzzle, parent, cost: int, swappedNum: int):
        self.value = value
        self.parent = parent
        if self.parent is None: self.depth = 0
        else: self.depth = self.parent.depth + 1
        self.cost = cost
        self.swappedNum = swappedNum


class SolvingAgent:
    """
    An AI agent that solves the 8-Puzzle problem using the BFS or DFS algorithms.
    It uses a Deque data structure and chooses to use it as a stack or a queue based on the BFS_or_DFS flag.
    """
    def __init__(self, initial_state: Puzzle):
        self.lis = deque() # A Deque to be used as a queue in case of BFS and as a stack in case of DFS
        self.initial_state = initial_state
        self.lis.append(Node(initial_state, None, 0, None))

    def checkVisited(self, visited: dict[Puzzle, str], to_check: Puzzle) -> bool:
        if visited.get(str(to_check)) == 'f': return True
        return False

    def empty(self, lis: deque) -> bool:
        return len(lis) == 0

    def solve(self) -> list[list[int], int]:
        # will contain the final state when the puzzle is solved
        goal: Node = None
        next_iteration_stack = deque()
        depth_limit = 5
        iterate = True
        visited = dict()
        max_depth = 0

        while iterate:
            while not self.empty(self.lis):
                # the state we are currently exploring
                current = self.lis.pop()
                # print(len(self.lis))

                if current.cost > max_depth: max_depth = current.cost
                if self.checkVisited(visited, current.value):
                    # instead of the overhead of checking if the node exists in the Deque every time we put in it,
                    # we just check when getting a node if it was visited or not.
                    continue
                if current.depth == depth_limit:
                    next_iteration_stack.append(current)
                    continue
                visited[str(current.value)] = 'f' # Mark Puzzle state as visited

                if current.value.checkSolved():
                    # if we reached final state, break out of the loop and set the goal variable to that state
                    goal = current
                    iterate = False
                    break

                swaps = current.value.generatePossibleSwaps()  # available numbers to swap
                for i in swaps:  # add each possibility of them to the deque in addition to the cost
                    p = current.value.copy()
                    p.swap(i)

                    if not (self.checkVisited(visited, p)):
                        self.lis.append(Node(p, current, current.cost + 1, i))

            # AFTER BREAKING OUT FROM THE LOOP
            if goal is None:
                self.lis = next_iteration_stack.copy()
                next_iteration_stack = deque()
                depth_limit += 5
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
