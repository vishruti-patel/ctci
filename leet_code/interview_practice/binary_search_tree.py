"""
basic implentation of a BST
"""


class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

    
def insert(root, value):
    if not root:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)

    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end = " ")
        inorder(root.right)


if __name__ == "__main__":
    root = Node(8)
    insert(root, 3)
    insert(root, 10)
    insert(root, 4)
    insert(root, 6)


    inorder(root)

