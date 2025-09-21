class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root):
        def dfs(left_root, right_root):
            if not left_root and not right_root:
                return True
            
            if not left_root or not right_root:
                return False
            
            return (left_root.val == right_root.val  and 
                    dfs(left_root.left, right_root.right) and 
                    dfs(left_root.right, right_root.left))


        return dfs(root.left, root.right)
    