from typing import Optional
import pprint

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

    def __repr__(self):
        return f"Node(val={self.val}, left={self.left}, right={self.right})"


class MyPractice:
    def __init__(self, name):
        self.root = None 
        self.name = name

    

    def dfs(root):
        pass


    def bfs(root):
        pass


    def build_tree(self, arr):
        """ this funciton will add node to the tree """
        # print(arr)
        self.root = Node(20)
        self.root = Node(20)
        # r = Node(10)
        # l = Node(30)
        self.root.right = Node(30)
        self.root.left = Node(10)

        # self.root.right.right = Node(35)
        # self.root.right.left = Node(32)
        print(self.root)


    def add_node(self, root :Node, val :int):
        pass

    def delete_node(self, root :Node, val:int):
        pass

    def find_a_node(self, root :Node, val: int):
        pass



if __name__ == '__main__':
    obj = MyPractice("Vishruti")
    # obj.build_tree([10,20, 30, 40, 50, 50])
    print(obj.name)
    obj2 = MyPractice("Raxit")
    print(obj2.name)



"""

Node(val=20, left=Node(val=10, left=None, right=None), right=Node(val=30, left=None, right=None))

"""    