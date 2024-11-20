class Node:
    data: str
    next: "Node"

    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    head: Node

    def __init__(self, head):
        self.head = head
    
    def print_structure(self):
        current_node = self.head

        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next

    def queue(self, node):
        current_node = self.head

        while (current_node.next is not None):
            current_node = current_node.next

        current_node.next = node

    def dequeue(self):
        if self.head:
            self.head = self.head.next

first_node = Node("Hola mundo")
second_node = Node("Segundo Nodo")
third_node = Node("Tercer Nodo")
fourth_node = Node("Cuarto Nodo")

first_node.next = second_node
second_node.next = third_node

structure = Queue(first_node)
structure.queue(fourth_node)
structure.dequeue()
structure.print_structure()