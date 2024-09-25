'''
1. Cree una estructura de objetos que asemeje un Stack.
    1.  Debe incluir los métodos de `push` (para agregar nodos) 
        `pop` (para quitar nodos).
    2.  Debe incluir un método para hacer `print` de toda la estructura.
    3.  No se permite el uso de tipos de datos compuestos como `lists`, 
        `dicts` o `tuples` ni módulos como `collections`.
'''

class Node:
    data: str
    next: "Node"

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    head: Node

    def __init__(self, head):
        self.head = head
    
    def print_structure(self):
        current_node = self.head

        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next

    def push(self, node):
        current_node = Node(node.data)
        current_node.next = self.head
        self.head = current_node
    
    def pop(self):
        if self.head:
            self.head = self.head.next

first_node = Node("Primer Nodo")
second_node = Node("Segundo Nodo")
third_node = Node("Tercer Nodo")
fourth_node = Node("Cuarto Nodo")
fifth_node = Node("Quinto Nodo")

first_node.next = second_node
second_node.next = third_node

structure = Stack(first_node)

structure.push(fourth_node)
structure.pop()
structure.push(fifth_node)

structure.print_structure()