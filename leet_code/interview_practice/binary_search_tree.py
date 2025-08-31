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


#searching the node:

def search(root, target):
    if not root or target == root.value:
        return root
    if target < root.value:
        return search(root.left, target)
    else:
        return search(root.right, target)

if __name__ == "__main__":
    root = Node(8)
    insert(root, 3)
    insert(root, 10)
    insert(root, 4)
    insert(root, 6)

    print("Inorder traversal:", end=" ")
    inorder(root)

    search_value = search(root, 2)
    if search_value:
        print("\nValue founded!")
    else:
        print("\nValue not present")