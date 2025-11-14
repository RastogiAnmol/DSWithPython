from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        
        def isUnival(node):
            if not node:
                return True  # Null nodes are trivially univalue
            
            # Postorder traversal: first check children
            left_uni = isUnival(node.left)
            right_uni = isUnival(node.right)
            
            # If either subtree is not univalue, this can't be
            if not left_uni or not right_uni:
                return False
            
            # Check current node value with its children
            if node.left and node.left.val != node.val:
                return False
            if node.right and node.right.val != node.val:
                return False
            
            # It's a univalue subtree
            self.count += 1
            return True
        
        isUnival(root)
        return self.count

sol = Solution()
# Example usage:
root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(5)
root.left.left = TreeNode(5)
root.left.right = TreeNode(5)
root.right.right = TreeNode(5)
res = sol.countUnivalSubtrees(root)
print(res)  # Output: 4