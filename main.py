from Puzzle import Puzzle
import A_Star_SolvingAgent
import B_D_solvingAgent
from PuzzleGUI import PuzzleGUI
import time

def isSolvable(puzzle):
    """
    Checks if the puzzle is solvable or not.
    """
    inversion_count = 0
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if int(puzzle[j]) < int(puzzle[i]) and puzzle[j] != '0':
                inversion_count += 1
    return inversion_count % 2 == 0

def checkSolved(puzzle):
    return puzzle == "012345678"

# print("Welcome to our humble 8-puzzle intelligent solver.")
# sleep(1)
# print("Our program can solve the puzzle using BFS, DFS and A* algorithm.")
# sleep(2)
# print("It can even make coffee if you want it to. ;)")
# sleep(1)
# print("")

condition = True
working_condition = True
while condition:
    puzzle = input("Please enter the puzzle (ex. 012345678): ")
    if len(puzzle) != 9:
        print("Puzzle invalid!")
        continue
    elif checkSolved(puzzle):
        print("Puzzle already solved.")
        working_condition = False
        break

    puzzle = [i for i in puzzle]
    for i in range(0,9):
        if str(i) not in puzzle:
            print("Puzzle invalid!")
        elif not isSolvable(puzzle):
            print("Puzzle unsolvable. Please enter a puzzle that can be solved.")
        else:
            condition = False
        break


if working_condition:
    while True:
        print("1- BFS\n2- DFS\n3- A*")
        method = input("Enter the solving method (1, 2, 3): ")
        if method not in ['1', '2', '3']:
            print("Method invalid.")
        else:
            break

    if method == '3':
        while True:
            print("1- Eucliden ditance\n2- Mannhaten distance")
            heuristic = input("Enter heuristic (1, 2): ")
            if heuristic not in ['1', '2']:
                print("Heuristic invalid.")
            else:
                break
        
        puzzle1 = Puzzle(puzzle)
        agent = A_Star_SolvingAgent.SolvingAgent(puzzle1, heuristic)
    else:
        puzzle1 = Puzzle(puzzle)
        agent = B_D_solvingAgent.SolvingAgent(puzzle1, method)

    start = time.time()
    solution = agent.solve()
    end = time.time()
    timer = end - start

    path = solution[0]
    print(path)
    print(timer)
    explored = solution[1]

    # 643512780
    PuzzleGUI(puzzle, path, explored, timer)