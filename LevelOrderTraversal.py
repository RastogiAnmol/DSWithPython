from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # Recurse on left & right children
        left_levels = self.levelOrder(root.left)
        right_levels = self.levelOrder(root.right)

        result = [[root.val]]  # level 0 (root)

        # Merge left and right levels
        for i in range(max(len(left_levels), len(right_levels))):
            left_level = left_levels[i] if i < len(left_levels) else []
            right_level = right_levels[i] if i < len(right_levels) else []
            result.append(left_level + right_level)

        return result
sol = Solution()
# Example usage:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(6)
root.left.right.right = TreeNode(7)
root.right.right.left = TreeNode(9)
res = sol.levelOrder(root)
print(res)  # Output: [[1], [2, 3], [4, 5, 8], [6, 7, 9]]sol = Solution()