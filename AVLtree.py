from bds_puzzle import Puzzle  # breadth first and depth first puzzle
from Puzzle import Puzzle  # a* puzzle


class Node:
    # constructor making a node with data
    def __init__(self, puzzle: Puzzle, value: int):
        self.puzzle = puzzle
        self.value = value
        self.left: Node = None
        self.right: Node = None
        self.height = 1


class Tree:
    def __init__(self, puzzle: Puzzle, value):
        self.root = Node(puzzle, value)

    def get_height(self, node: Node):
        if node is None:
            return -1
        if node.left is None and node.right is None:
            return 0
        return 1 + max(self.get_height(node.left), self.get_height(node.right))

    def update_height(self, node: Node):
        leftHeight = self.get_height(node.left)
        rightHeight = self.get_height(node.right)
        node.height = max(leftHeight, rightHeight) + 1

    def balance_factor(self, node: Node):
        if node is not None:
            return self.get_height(node.right) - self.get_height(node.left)
        else:
            return 0

        #        N                   R
        #        |                   |
        #    L        R           N       RR
        #    |        |           |        |
        #        RL     RR     L    RL

    def rotate_left(self, node: Node):
        nodeRight = node.right  # memorize the right child
        node.right = nodeRight.left  # N right child become RL
        nodeRight.left = node        # N becomes the left child of R
        self.update_height(node)
        self.update_height(nodeRight)
        return nodeRight

        #        N                  L
        #        |                  |
        #    L        R        LL       N
        #    |        |        |        |
        # LL   LR                    LR   R

    def rotate_right(self, node: Node):
        nodeLeft = node.left  # memorize the left child L
        node.left = nodeLeft.right  # N left child become LR
        nodeLeft.right = node
        self.update_height(node)
        self.update_height(nodeLeft)
        return nodeLeft

        #     N
	    #     |
		# L       R
		# there are 4 cases for rebalancing a node
		# case 1 : bf(N) <-1 and bf(L) <= 0   then we rotateRight(N)
		# case 2 : bf(N) <-1 and bf(L) >  0   then we rotateLeft(L) then rotateRight(N)
		# case 3 : bf(N) > 1 and bf(L) >= 0   then we rotateLeft(N)
		# case 4 : bf(N) > 1 and bf(L) <  0   then we rotateRight(L) then rotateLeft(N)

    def rebalance(self, node: Node):
        balance = self.balance_factor(node)
        if (balance != 0) or (balance != 1) or (balance != -1):

            # left heavy
            if balance < -1:
                if self.balance_factor(node.left) > 0:
                    # rotate left - right
                    node.left = self.rotate_left(node.left)
                    node = self.rotate_right(node)
                else:
                    # rotate right
                    node = self.rotate_right(node)
            # right heavy
            elif balance > 1:
                if self.balance_factor(node.right) < 0:
                    # rotate right left
                    node.right = self.rotate_right(node.right)
                    node = self.rotate_left(node)
                else:
                    # rotate left
                    node = self.rotate_left(node)
        return node

    def add_child(self, puzzle: Puzzle, value):
        self.root = self.insert(self.root, puzzle, value)

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

        self.update_height(node)
        return self.rebalance(node)

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

    def search(self, value):
        return self.searchRec(self.root, value)

    # return 0 if not exist and 1 if exist
    def searchRec(self, node: Node, value):
        if node is None:
            return 0
        else:
            if node.value is None:
                return 0
            if node.value == value:
                return 1
            elif node.value > value:
                return self.searchRec(node.left, value)
            elif node.value < value:
                return self.searchRec(node.right, value)
            else:
                return 0



if __name__ == "__main__":
    row3 = ['1', '0', '2']
    row4 = ['3', '4', '5']
    row5 = ['6', '7', '8']
    row = [row3, row4, row5]

    p = Puzzle(row)
    p1 = Puzzle(row)
    p2 = Puzzle(row)
    p3 = Puzzle(row)
    p4 = Puzzle(row)
    p5 = Puzzle(row)
    p6 = Puzzle(row)
    p7 = Puzzle(row)
    p8 = Puzzle(row)
    p9 = Puzzle(row)
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

    print(t.search(15))
