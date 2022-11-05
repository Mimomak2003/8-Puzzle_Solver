from Puzzle import Puzzle  # a* puzzle


class Node:
    # constructor making a node with data
    def __init__(self, puzzle: Puzzle):
        self.puzzle = puzzle
        self.left: Node = None
        self.right: Node = None
        self.height = 1


class Tree:
    def __init__(self, puzzle: Puzzle):
        self.root = Node(puzzle)

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

    def insert(self, node, puzzle: Puzzle):
        # if binary search tree is empty, create a new node and declare it as root
        if node is None:
            node = Node(puzzle)
            return node
        # if newValue is less than value of data in root, add it to left subtree and proceed recursively
        if puzzle < node.puzzle:
            node.left = self.insert(node.left, puzzle)
        # if newValue is greater than value of data in root, add it to right subtree and proceed recursively
        elif puzzle > node.puzzle:
            node.right = self.insert(node.right, puzzle)

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
