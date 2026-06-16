from typing import Any

class Node:
    # Constructor to create a new node
    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.next: Node | None = None
        self.prev: Node | None = None


# Class to create a Doubly Linked List
class DoublyLinkedList :

    # Constructor for empty Doubly Linked List
    def __init__(self) -> None :
        self.head = None

    # Given a reference to the head of a list and an
    # integer, inserts a new node on the front of list
    def push(self, new_data) :

        # 1. Allocates node
        # 2. Put the data in it
        new_node = Node(new_data)

        # 3. Make next of new node as head and
        # previous as None (already None)
        new_node.next = self.head

        # 4. change prev of head node to new_node
        if self.head is not None :
            self.head.prev = new_node

        # 5. move the head to point to the new node
        self.head = new_node

    # This function prints contents of linked list
    # starting from the given node
    def printList(self, node) :

        print("\nTraversal in forward direction")
        while node is not None :
            print(" % d" % (node.data))
            last = node
            node = node.next

    def quicksort(self, start, end) :
        if (end != None) and (start != end) and (start != end.next) :
            pI = self.partition(start, end)
            self.quicksort(start, pI.prev)
            self.quicksort(pI.next, end)

    def partition(self, start, end) :
        pivot = end
        pI = start
        while start != end :
            if start.data <= pivot.data :
                start.data, pI.data = pI.data, start.data
                pI = pI.next
            start = start.next
        pI.data, pivot.data = pivot.data, pI.data
        return pI

    def last_node(self) -> Node | None :
        temp = self.head
        while temp is not None and temp.next is not None :
            temp = temp.next
        return temp


# Driver program to test above functions

# Start with empty list
llist = DoublyLinkedList()
llist.push(4)
llist.push(3)
llist.push(5)
llist.push(8)
llist.push(6)
llist.push(1)
llist.push(2)
llist.push(7)


print("Created DLL is: ")
llist.printList(llist.head)
print("\n sorted list")
end = llist.last_node()
if end is not None:
    llist.quicksort(llist.head, end)
llist.printList(llist.head)

# This code is contributed by Anmol Rastogi 4