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
            #  i and n-i-1 represents number of nodes in left and right subtree and not indexes
            # since we are only considering full binary trees both left and right subtree must have odd number of nodes
            # Let's say n = 7
            # i = 1, n-i-1 = 5
            # i = 3, n-i-1 = 3
            # i = 5, n-i-1 = 1
            
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
res = sol.allPossibleFBT(7)
print(res)