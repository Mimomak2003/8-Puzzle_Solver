from Puzzle import Puzzle
from queue import PriorityQueue

class Node():
    """
    Node class to save the data in.
    """
    def __init__(self, value: Puzzle, parent, cost_from_root, swapped_num):
        self.value = value
        self.parent = parent
        self.cost = cost_from_root
        self.sn = swapped_num # What number was swapped to reach this state?
    
    def _is_valid_operand(self, other): # to use when comparing two nodes
        return hasattr(other, "sn")

    def __lt__(self, other): # Checks if the node is less than another node.
        if not self._is_valid_operand(other):
            return NotImplemented
        return int(self.sn) < int(other.sn)

    def __gt__(self, other): # Checks if the node is greater than another node.
        if not self._is_valid_operand(other):
            return NotImplemented
        return int(self.sn) > int(other.sn)

class SolvingAgent():
    def __init__(self, initial_state: Puzzle, heuristic_type: str):
        self.pqueue = PriorityQueue()
        self.heuristic = heuristic_type # Mannhaten distance or Euclidean distance
        # Put the initial state into the priority queue with no parent or swapped number, and a cost of 0
        self.pqueue.put((self.h(initial_state), Node(initial_state, None, 0, None)))

    def solve(self):
        """
        Returns a path to the solution of the puzzle.
        """
        goal: Node = None     # will contain the final state when the puzzle is solved
        visited = []
        while not self.pqueue.empty():
            current = self.pqueue.get()[1]      # the state we are currently exploring
            if self.checkVisited(visited, current.value):
                # instead of the overhead of checking if the node exists in the PQ every time we put in it,
                # we just check when getting a node if it was visited or not.
                continue
            visited.append(current.value)

            if current.value.checkSolved():
                # if we reached final state, break out of the loop and set the goal variable to that state
                goal = current
                break

            swaps = current.value.generatePossibleSwaps() # available numbers to swap
            for i in swaps: # add each possiblity of them to the queue in addition to the heuristic + cost
                p = current.value.copy()
                p.swap(i)
                if not self.checkVisited(visited, p):
                    self.pqueue.put((current.cost + 1 + self.h(p), Node(p, current, current.cost + 1, i)))

        # AFTER BREAKING OUT FROM THE LOOP
        if goal is None: 
            # If the goal is still none, then it might be unsolvable.
            raise UnSolvablePuzzleError()
        else:
            # return the path to the goal
            path = []
            while goal.sn is not None:
                x = [str(goal.sn)]
                x.extend(path)
                path = x
                goal = goal.parent
            return [path, len(visited)]


    def h(self, puzzle):
        final_h = 0
        if self.heuristic == '1': # Eucliden ditance
            for i in range(0, 9):
                current_coordinates = puzzle.findNum(str(i))
                num_coordinates = [i // 3, i % 3]
                final_h = ((current_coordinates[0] - num_coordinates[0])**2 + \
                    (current_coordinates[1] - num_coordinates[1])**2)**(1/2)
        else: # Mannhaten distance
            for i in range(0, 9):
                current_coordinates = puzzle.findNum(str(i))
                num_coordinates = [i // 3, i % 3]
                final_h += abs(current_coordinates[0] - num_coordinates[0]) + \
                    abs(current_coordinates[1] - num_coordinates[1])
        return final_h
        

    def checkVisited(self, visited, to_check):
        for i in visited:
            if i.equals(to_check): return True
        return False


class UnSolvablePuzzleError(Exception):
    """
    The puzzle is unsolvable
    """
    pass