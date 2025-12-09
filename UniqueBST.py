from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    # This question can not be solved using recursion by considering each generateTrees(n-1) as a subproblem of generateTrees(n)
    # because the structure of the tree depends on the values assigned to each node, not just the number of nodes.
    # There is no relation between the structure of BSTs formed with n nodes and those formed with n-1 nodes.
    # You can not use the same subtree structure for different root values without adjusting the values in the subtrees. That's why
    # we need to consider the range of values (start to end) for each subtree when generating the trees.
    # For example, the left and right subtrees of a node must contain values less than and greater than the node's value, respectively.
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
            # we are using start > end to represent an empty tree and returning [None] to indicate that there is one way to have an empty tree.
            # We can not return [] here because that would indicate that there are no trees possible in this range. Also if we return [],
            # in the nested for loop below, it would lead to no iterations and thus no trees being formed for that root value.
            if start > end:
                cache[(start, end)] = [None]
                return [None]
            if start == end:
                cache[(start, end)] = [TreeNode(start)]
                return [TreeNode(start)]

            # all_trees list is declared here because we want to reset it for each (start, end) range. 
            # We only need to cache the final result and not intermediate results within the for loop.
            # If caching intermediate results was necessary then we would have put it inside the for loop.
            all_trees = []
            for root_val in range(start, end + 1):
                # Generate all left and right subtrees recursively for the current root value
                # In this recursion we are ensuring that the parameters reach the base cases eventually.
                # It will reach base case because in each recursive call the range (end - start) reduces.
                left_trees = helper(start, root_val - 1)
                right_trees = helper(root_val + 1, end)
                # Combine each left and right subtree with the current root value. We need a cartesian product here because 
                # each left subtree can be paired with each right subtree to form a unique BST.
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