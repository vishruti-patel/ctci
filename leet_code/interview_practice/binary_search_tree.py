"""
basic implentation of a BST
"""

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
    
    def __repr__(self):
        return f"Node(val={self.val}, left={self.left}, right={self.right})"
class solution:
    def __init__(self):
        self.root = None

    def tree(self):
        self.root = Node(30)
        self.root.left = Node(25)
        self.root.right = Node(35)
        self.root.left.left = Node(24)
        self.root.left.right = Node(26)


    #we did not pass 'root' as an argument as we are using instance variable self.root (stack = [self.root]). 
    def traverse(self):
        result = []
        stack = [self.root]

        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result
    

    def depth_of_tree(self):
        depth_max = 1
        stack = [(self.root, 1)]

        while stack:
            node, depth = stack.pop()

            depth_max = max(depth_max, depth)
            print(node.val, depth)

            if node.right:
                stack.append((node.right, depth + 1))
            if node.left:
                stack.append((node.left, depth + 1))

        return depth_max
                
    
if __name__ == '__main__':
    obj = solution()
    obj.tree()
    # print(obj.root)
    # print(obj.traverse())
    print(obj.depth_of_tree())



