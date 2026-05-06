# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """

        current_node = root
        queue = []
        level_averages = []

        queue.append(current_node)
        while queue:
            # Get number of nodes at this level
            level_size = len(queue)
            level_sum = 0

            # Process all nodes at current level
            for i in range(level_size):

                # Process each node in this level
                current_node = queue.pop(0)  # Remove node from front of queue
                level_sum += current_node.val  # Add its value to level sum

                # Add children to queue for next level
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            level_averages.append(level_sum / float(level_size))

        return level_averages
