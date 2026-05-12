def hasPathSum(root, targetSum):
    """
    :type root: Optional[TreeNode]
    :type targetSum: int
    :rtype: bool
    """

    if not root:
        return False

    if root.val == targetSum and not root.left and not root.right:
        return True

    targetSum = targetSum - root.value

    if root.left:
        hasPathSum(root.left, targetSum)

    if root.right:
        hasPathSum(root.right, targetSum)

    return hasPathSum(root.left, targetSum) or hasPathSum(root.right, targetSum)


def hasPathSum2(root, targetSum):
    if not root:
        return False

    if not root.left and not root.right:  # leaf node
        return root.val == targetSum

    remaining = targetSum - root.val

    # Explicitly check for existence of left/right children
    left_path = hasPathSum(root.left, remaining) if root.left else False
    right_path = hasPathSum(root.right, remaining) if root.right else False

    return left_path or right_path
