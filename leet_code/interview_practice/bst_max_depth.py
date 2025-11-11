
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class solution:
    def __init__(self):
        self.root = None

    def build_tree(self):
        self.root = TreeNode(40)
        self.root.left = TreeNode(30)
        self.root.right = TreeNode(50)
        self.root.left.left = TreeNode(25)
        self.root.left.right = TreeNode(35)
        self.root.right.left = TreeNode(45)

    def max_depth(self):
        max_depth = 1
        stack = [(self.root, 1)]

        while stack:
            node, depth = stack.pop()

            max_depth = max(max_depth, depth)
            # print(node.val, depth)

            if node.right:
                stack.append((node.right, depth + 1))
            if node.left:
                stack.append((node.left, depth + 1))
        return max_depth
        


if __name__ == '__main__':
    obj = solution()
    obj.build_tree()
    print(obj.max_depth())


