'''
2. Cree una estructura de objetos que asemeje un Double Ended Queue.
    1.  Debe incluir los métodos de `push_left` y `push_right` (para agregar
        nodos al inicio y al final) y `pop_left` y `pop_right` (para quitar 
        nodos al inicio y al final).
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

class DoubleEndedQueue:
    head: Node

    def __init__(self, head):
        self.head = head
    
    def print_structure(self):
        current_node = self.head

        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next

    def push_left(self, node):
        current_node = Node(node.data)
        current_node.next = self.head
        self.head = current_node
    
    def pop_left(self):
        if self.head:
            self.head = self.head.next

    def push_right(self, node):
        current_node = self.head

        while (current_node.next is not None):
            current_node = current_node.next

        current_node.next = node

    def pop_right(self):
        if self.head is None:
            return
        
        if self.head.next is None:
            self.head = None
            return
        
        current_node = self.head
        
        while (current_node.next.next is not None):
            current_node = current_node.next
        
        current_node.next = None
            

first_node = Node("Primer Nodo")
second_node = Node("Segundo Nodo")
third_node = Node("Tercer Nodo")
fourth_node = Node("Cuarto Nodo")
fifth_node = Node("Quinto Nodo")

first_node.next = second_node
# second_node.next = third_node

structure = DoubleEndedQueue(first_node)

structure.pop_right()

structure.print_structure()