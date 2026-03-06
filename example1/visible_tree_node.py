from math import inf

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def visible_tree_node(root: Node) -> int:
    def dfs(root, max_sofar):
        if not root:
            return 0

        total = 0
        if root.val >= max_sofar:
            total += 1

        # max_sofar for child node is the larger of previous max and current node val
        total += dfs(root.left, max(max_sofar, root.val))
        total += dfs(root.right, max(max_sofar, root.val))

        return total

    # start max_sofar with smallest number possible so any value root has is smaller than it
    return dfs(root, -inf)

# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    if val == "x":
        return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == "__main__":
    root = build_tree(iter(input().split()), int)
    res = visible_tree_node(root)
    print(res)