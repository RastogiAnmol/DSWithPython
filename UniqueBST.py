from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def generateTrees(self, n: int):
        cache: dict[tuple, list] = {}
        if n == 0:
            return []

        def clone(node, offset):
            if not node:
                return None
            return TreeNode(node.val + offset, clone(node.left, offset), clone(node.right, offset))

        def helper(start, end):
            if (start, end) in cache:
                return cache[(start, end)]
            if start > end:
                cache[(start, end)] = [None]
                return [None]
            if start == end:
                cache[(start, end)] = [TreeNode(start)]
                return [TreeNode(start)]

            all_trees = []
            for root_val in range(start, end + 1):
                left_trees = helper(start, root_val - 1)
                right_trees = helper(root_val + 1, end)

                for l in left_trees:
                    for r in right_trees:
                        root = TreeNode(root_val, l, r)
                        all_trees.append(root)
            cache[(start, end)] = all_trees
            return all_trees

        return helper(1, n)

def print_tree(node):
    if not node:
        return "None"
    return f"{node.val}({print_tree(node.left)},{print_tree(node.right)})"
        
sol = Solution()
trees = sol.generateTrees(3)
print_trees = [print_tree(tree) for tree in trees]
for t in print_trees:
    print(t)