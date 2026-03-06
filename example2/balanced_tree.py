class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(tree: Node | None) -> bool:
    # WRITE YOUR BRILLIANT CODE HERE
    def height_or_unbalanced(node):
        if not node:
            return 0

        lh = height_or_unbalanced(node.left)
        if lh == -1:
            return -1

        rh = height_or_unbalanced(node.right)
        if rh == -1:
            return -1

        if abs(lh - rh) > 1:
            return -1

        return max(lh, rh) + 1

    return height_or_unbalanced(tree) != -1

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
    inp = input().split()
    tree = build_tree(iter(inp), int)
    res = is_balanced(tree)
    print("true" if res else "false")