def isSymmetric(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: bool
    """

    if not root:
        return True

    def checker(left, right):
        if not left and not right:
            return True

        if not left or not right:
            return False

        return (
            (left.val == right.val)
            and checker(left.left, right.right)
            and checker(left.right, right.left)
        )

    return checker(root.left, root.right)
