"""class Node:
    def __init__(self, data):
        self.data = data
        self.next = None            #reference to the next node.


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end = " ")
            temp = temp.next
        print()

if __name__ == '__main__':
    l = LinkedList()
    l.insert_at_start('start')
    l.insert_at_start('end')

    l.print_list()
"""

#print simple linkedlist:

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class LinkedList:
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    head = node1

    node1.next = node2
    node2.next = node3


    curr = head
    while curr:
        print(curr.val, end= "->")
        curr = curr.next

    








