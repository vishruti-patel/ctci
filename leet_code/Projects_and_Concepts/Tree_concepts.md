#Complete Binary Tree:
    Approach : Use DFS bound limit - use lower and higher limit
                stack = root, float("-inf"), float("inf)


#Symmetric Tree (Mirror to itself):
Approach: by BFS, queue - start traversing by adding 2 values - root.left, root.right.
            -> Then append t1.left, t2.right and t1.right, t2.left


#Binary Tree Level Order Traversal - printing all the nodes of the tree at the same level
Approach: Use BFS - use for loop - define another empty array level= []. append the node.val to level and then append the level to result[]


#Convert sorted array to Binary Search Tree:
Approach - Simulating Recursion from Stack OR Divide and Conquer.
        - We find the mid value of the array -> assign as a root so that we can get the root of the tree.
        - Divide arrray into left-subarray and right=subarray.
        - initialize empty stack. Then append 4 variables to the stack - root, left_index, right_index, is_left_subtree
        - Then run a while loop, pop the stack and unpack 4 variables from the stack element.
        - again find a mid and assign as a node.
        - check if is_left then assign as parent.left. Else assign as parent.right
        - Fianlly, append the values to the stack - stack.append((node, left, mid-1, True)), .append((root, mid+1, right, False))
        - return root.

