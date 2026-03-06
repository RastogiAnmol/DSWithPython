class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def node_next(node):
    return node.next or node

def has_cycle(nodes: Node) -> bool:
    tortoise = node_next(nodes)
    hare = node_next(node_next(nodes))
    while tortoise != hare and hare.next is not None:
        tortoise = node_next(tortoise)
        hare = node_next(node_next(hare))
    return hare.next is not None

if __name__ == "__main__":
    raw_input = [int(x) for x in input().split()]
    nodes_list = []
    for i in range(len(raw_input)):
        nodes_list.append(Node(i))
    for i, entry in enumerate(raw_input):
        if entry != -1:
            nodes_list[i].next = nodes_list[entry]
    nodes = nodes_list[0]
    res = has_cycle(nodes)
    print("true" if res else "false")