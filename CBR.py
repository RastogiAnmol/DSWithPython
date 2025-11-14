from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        # Step 1: store every value's index in inorder array (O(1) lookup)
        index_map = {val: i for i, val in enumerate(inorder)}

        # Step 2: define recursive function using indices
        def build(in_left, in_right):
            if in_left > in_right:
                return None

            # Step 3: last element in postorder is current root
            root_val = postorder.pop()
            root = TreeNode(root_val)

            # Step 4: locate root in inorder
            mid = index_map[root_val]

            # 🚨 Build right subtree **before** left subtree
            root.right = build(mid + 1, in_right)
            root.left  = build(in_left, mid - 1)

            return root

        return build(0, len(inorder) - 1)

obj = Solution()
# Example usage:
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
root = obj.buildTree(inorder, postorder)
# The constructed binary tree's root is now stored in 'root' variable.
# You can add additional code to test or visualize the tree if needed.