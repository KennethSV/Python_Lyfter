'''
3. Cree una estructura de objetos que asemeje un Binary Tree.
    1.  Debe incluir un método para hacer `print` de toda la estructura.
    2.  No se permite el uso de tipos de datos compuestos como `lists`, 
        `dicts` o `tuples` ni módulos como `collections`.
'''

class Node:
    data: str
    next: "Node"

    def __init__(self, data):
        self.data = data
        self.next = None

class BinaryTree:
    head: Node

    def __init__(self, head):
        self.head = head
    
    def print_structure(self):
        current_node = self.head

        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
h = Node("h")
i = Node("i")
j = Node("j")


a.next = b
b.next = d
d.next = h

structure = BinaryTree(a)
structure.print_structure()

a.next = b
b.next = d
d.next = i

structure = BinaryTree(a)
structure.print_structure()

a.next = b
b.next = e
e.next = j

structure = BinaryTree(a)
structure.print_structure()

a.next = c
c.next = g

structure = BinaryTree(a)
structure.print_structure()

a.next = c
c.next = f

structure = BinaryTree(a)
structure.print_structure()