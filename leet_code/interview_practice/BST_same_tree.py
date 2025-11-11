from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    # def tree(self):
    #     self.root = TreeNode(40)
    #     self.


    def isSameTree(p, q):
        queue = deque([(p,q)])

        while queue:
            node1, node2 = queue.popleft()

            if node1.val != node2.val or not node1 or not node2:
                return False
            
            queue.append((node1.left, node2.left))
            queue.append((node1.righ, node2.right))
        return True
    
if __name__ == '__main__':
    obj= Solution()
    print(obj.isSameTree(20,20))
