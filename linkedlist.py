# Example of linked list implementation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating a linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
