maximum = 0
def dfs(node):
  if node is None:
    return int('-inf')
  global maximum
  maximum = max(node.val, maximum)
  dfs(node.left)
  dfs(node.right)