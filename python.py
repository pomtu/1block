import random
from graphviz import Digraph

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, node):
        if value < node.value:
            if not node.left:
                node.left = Node(value)
            else:
                self._insert(value, node.left)
        elif value > node.value:
            if not node.right:
                node.right = Node(value)
            else:
                self._insert(value, node.right)

def draw_tree(node, dot):
    if node:
        dot.node(str(node.value))
        if node.left:
            dot.edge(str(node.value), str(node.left.value))
            draw_tree(node.left, dot)
        if node.right:
            dot.edge(str(node.value), str(node.right.value))
            draw_tree(node.right, dot)

# creation au hasard de l'arbre
tree = BinaryTree()
for i in range(10):
    tree.insert(random.randint(1, 100))

#dessin de l'abre
dot = Digraph()
draw_tree(tree.root, dot)
dot.render('tree', view=True)