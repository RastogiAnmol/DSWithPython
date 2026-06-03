class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find(tree, val):
    if tree is None:
        return False
    if tree.val == val:
        return True
    elif tree.val < val:
        return find(tree.right, val)
    else:
        return find(tree.left, val)

def insert_bst(tree, val):
    if tree is None:
        return Node(val)
    if tree.val < val:
        tree.right = insert_bst(tree.right, val)
    elif tree.val > val:
        tree.left = insert_bst(tree.left, val)
    return tree

# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    if val == "x":
        return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

def format_tree(node):
    if node is None:
        yield "x"
        return
    yield str(node.val)
    yield from format_tree(node.left)
    yield from format_tree(node.right)

if __name__ == "__main__":
    bst = build_tree(iter(input().split()), int)
    print(" ".join(format_tree(bst)))
    val = int(input())
    res = insert_bst(bst, val)
    print(" ".join(format_tree(res)))