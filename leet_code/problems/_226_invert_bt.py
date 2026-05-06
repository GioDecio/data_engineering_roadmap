# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: Optional[TreeNode]
    """

    if not root:
        return None

    inv_left_child = self.invertTree(root.right)
    inv_right_child = self.invertTree(root.left)

    root.left = inv_left_child
    root.right = inv_right_child

    return root
