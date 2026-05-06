# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
    
   
        def helper(root, min, max):

            if not root:
                return True

            if not min < root.val < max:
                return False 
            
            left = helper(root.left, min, root.val)
            right = helper(root.right, root.val, max)
            
            return left and right
        min = float('-inf')
        max = float('inf')
        return helper(root, min, max)

    
