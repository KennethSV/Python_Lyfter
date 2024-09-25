class Node:
    data: str
    next: "Node"

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    head: Node

    def __init__(self, head):
        self.head = head
    
    def print_structure(self):
        current_node = self.head

        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next

first_node = Node("Hola mundo")
second_node = Node("Segundo Nodo")
third_node = Node("Tercer Nodo")

first_node.next = second_node
second_node.next = third_node

structure = LinkedList(first_node)
structure.print_structure()