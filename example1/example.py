# type: ignore
class DoublyNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

def reverse_doubly_linked_list(head: DoublyNode) -> DoublyNode:
    # WRITE YOUR BRILLIANT CODE HERE
    if not head or not head.next:
        return head
    second = head.next
    reversed_list = reverse_doubly_linked_list(head.next)
    second.next = head
    head.prev = second
    head.next = None
    return reversed_list

def build_doubly_list(it, f):
    vals = [f(x) for x in it if x]
    if not vals:
        return None
    head = DoublyNode(vals[0])
    current = head
    for val in vals[1:]:
        node = DoublyNode(val, None, current)
        current.next = node
        current = node
    return head

def format_doubly_list(node):
    result = []
    while node:
        result.append(str(node.val))
        node = node.next
    return result

if __name__ == "__main__":
    head = build_doubly_list(iter(input().split()), int)
    res = reverse_doubly_linked_list(head)
    print(" ".join(format_doubly_list(res)))
