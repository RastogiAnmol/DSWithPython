# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    cache: dict[int, List[Optional[TreeNode]]] = {}
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        possibleBST: List[Optional[TreeNode]] = []
        if n in Solution.cache:
            return Solution.cache[n]
        if n%2 == 0:
            Solution.cache[n] = possibleBST
            return possibleBST
        if n == 1:
            possibleBST.append(TreeNode(0))
            Solution.cache[n] = possibleBST
            return possibleBST
        
        for i in range(1, n, 2):
            leftTree = self.allPossibleFBT(i)
            rightTree = self.allPossibleFBT(n-i-1)
            for lT in leftTree:
                for rT in rightTree:
                    root = TreeNode(0)
                    root.left = lT
                    root.right = rT
                    possibleBST.append(root)
        Solution.cache[n] = possibleBST
        return possibleBST

sol = Solution()
res = sol.allPossibleFBT(5)
print(res)