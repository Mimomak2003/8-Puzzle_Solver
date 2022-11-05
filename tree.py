from bds_puzzle import Puzzle  # breadth first and depth first puzzle
from Puzzle import Puzzle  # a* puzzle


class Node:
    # constructor making a node with data
    def __init__(self, puzzle: Puzzle, value):
        self.puzzle = puzzle
        self.value = value
        self.left: Node = None
        self.right: Node = None


class Tree:
    def __init__(self, puzzle: Puzzle, value):
        self.root = Node(puzzle, value)

    def add_child(self, puzzle: Puzzle, value):
        self.insert(self.root, puzzle, value)

    def insert(self, node, puzzle: Puzzle, newValue):
        # if binary search tree is empty, create a new node and declare it as root
        if node is None:
            node = Node(puzzle, newValue)
            return node
        # if newValue is less than value of data in root, add it to left subtree and proceed recursively
        if newValue < node.value:
            node.left = self.insert(node.left, puzzle, newValue)
        # if newValue is greater than value of data in root, add it to right subtree and proceed recursively
        elif newValue > node.value:
            node.right = self.insert(node.right, puzzle, newValue)
        return node

    def print_tree(self, node):
        """ method to print every node in the tree
            preorder : parent > left > right
        """
        if node is not None:
            print("parent : ", node.value)
        if node is not None:
            if node.left is not None:
                if node.left is not None:
                    print("left : ", node.left.value)
            if node.right is not None:
                if node.right is not None:
                    print("right : ", node.right.value)

            if node.left is not None:
                self.print_tree(node.left)
            if node.right is not None:
                self.print_tree(node.right)

    def PrintTree(self):
        self.print_tree(self.root)


if __name__ == "__main__":
    row3 = ['1', '0', '2']
    row4 = ['3', '4', '5']
    row5 = ['6', '7', '8']

    p = Puzzle(row3, row4, row5)
    p1 = Puzzle(row3, row4, row5)
    p2 = Puzzle(row3, row4, row5)
    p3 = Puzzle(row3, row4, row5)
    p4 = Puzzle(row3, row4, row5)
    p5 = Puzzle(row3, row4, row5)
    p6 = Puzzle(row3, row4, row5)
    p7 = Puzzle(row3, row4, row5)
    p8 = Puzzle(row3, row4, row5)
    p9 = Puzzle(row3, row4, row5)
    t = Tree(p, 20)
    t.add_child(p1, 19)
    t.add_child(p2, 21)
    t.add_child(p3, 18)
    t.add_child(p4, 22)
    t.add_child(p5, 17)
    t.add_child(p6, 23)
    t.add_child(p7, 16)
    t.add_child(p8, 24)
    t.add_child(p9, 15)
    t.PrintTree()
