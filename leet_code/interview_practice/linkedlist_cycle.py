"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.
"""


#creating nodes manually 

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class List:
    def cycle(self, head):
        slow, fast = head, head


        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False
    

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(2)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node2 


l = List()
print(l.cycle(node1))




