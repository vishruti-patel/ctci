#traversing tree by BFS:

from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree():
    root = TreeNode(30)
    root.left = TreeNode(25)
    root.right = TreeNode(35)
    root.left.left = TreeNode(20)
    root.left.right = TreeNode(26)

    return root

def bfs(root):
    if not root:
        return []
    

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result


def dfs_preorder(root):
    if not root:
        return []
    
    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node.val)

        if node.right:
            result.append(node.right)
        if node.left:
            result.append(node.left)

    return result

if __name__ == '__main__':
    root = build_tree()
    # print(bfs(root))
    print(dfs_preorder(root))
