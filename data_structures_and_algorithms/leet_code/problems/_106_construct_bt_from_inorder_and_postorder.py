class TreeNode:

    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def print_tree(self):
        # Print the tree in a pre-order traversal
        print(self.value, end=" ")
        if self.left:
            self.left.print_tree()
        if self.right:
            self.right.print_tree()


def buildTree1(postorder, inorder):

    if not postorder or not inorder:
        return None

    root = TreeNode(postorder[-1])
    root_idx = inorder.index(root.value)
    root.right = buildTree1(postorder[root_idx:-1], inorder[root_idx + 1 :])
    root.left = buildTree1(postorder[:root_idx], inorder[:root_idx])

    return root


def buildTree2(postorder, inorder):
    if inorder:
        r = postorder.pop()
        root = TreeNode(r)
        i = inorder.index(r)
        root.right = buildTree2(postorder, inorder[i + 1 :])
        root.left = buildTree2(postorder, inorder[:i])

        return root


postorder = [1, 2, 9, 15, 7, 20, 3]
inorder = [1, 9, 2, 3, 15, 20, 7]

root1 = buildTree1(postorder, inorder)
root1.print_tree()

print("\n")

root2 = buildTree2(postorder, inorder)
root2.print_tree()
