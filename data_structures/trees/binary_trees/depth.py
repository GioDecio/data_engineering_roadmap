class binaryTree:

    def __init__(self) -> None:
        self.root = None

    def max_depth(self, root):

        left_max = max_depth(root.left)
        right_max = max_depth(root.right)

        return max([left_max, right_max])


root = binaryTree()

root
