from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root:TreeNode) -> List[int]:
        if root is None:
            return []
        lst, res = [root], []
        node = TreeNode()
        while lst:
            if root.left:
                lst.append(root.left)
                root = root.left
                continue
            if lst:
                node = lst.pop()
                res.append(node.val)
            if lst:
                node = lst.pop()
                res.append(node.val)
            if node.right:
                lst.append(node.right)
                root = node.right
        return res

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(6)
root.left.right.right = TreeNode(7)
root.right.right.left = TreeNode(9)

res = sol.inorderTraversal(root)
print(res)  # Output: [4, 2, 6, 5,