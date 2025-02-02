"""
    Node: [data, next -> (next node)]

    l = ["a", "b", "c", "d", "e", "f", "g"]

"""

# class family:
    
#     def __init__(self,relation,name):
#         self.relation = relation
#         self.name = name

# member1 = family("Mom", "Rekha")
# member2 = family("Dad", "Tarun")

# print(member1.who, member1.name)
# print(member2.name)


# class create_ll:
#     def __init__(self,data,pointer):
#         self.data = data
#         self.pointer = pointer

# obj = create_ll('12', 1)
# print(obj.data)

class Node:   
    def __init__(self,data):            #node consists of data and pointer or next
        self.data = data
        self.next = None                    #none because initially pointer is set to null

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)              #create new node from class node and passing the data

        if self.head is None:              #the head of the first node will always be null and hence if it is null then we want to point the head to new_node
            self.head = new_node            
            return
        
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next



llist = LinkedList()
print(llist.append('A'))
print(llist.append('B'))
print(llist.append)
print(print_list)






# class ListNode(object):
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
        
# def create_linkedlist(input) -> ListNode:
#     head = ListNode(input[0])
#     prev = head
#     for i in range(1, len(input)):
#         node = ListNode(input[i])
#         prev.next = node
#         prev = node        
#     return head   
    
# def print_ll(head):
#     itr = head
#     while itr.next:
#         print(itr.val)
#         itr = itr.next
#     print(itr.val)

# def add_node_at_begining(val, head) -> ListNode:
#     node = ListNode(val)
#     node.next = head
#     head = node
#     return head

# def add_node_at_end_of_ll(val, head) -> ListNode:
#     node = ListNode(val)
#     itr = head
#     while itr.next is not None:
#         itr = itr.next

#     itr.next = node
#     return head

# if __name__ == '__main__':
#     input = ["a", "b", "c", "d", "e", "f", "g"]
#     head = create_linkedlist(input)
#     head = add_node_at_begining("x", head)
#     head = add_node_at_end_of_ll("z", head)

#     print_ll(head)


# # node1 = ListNode(1)
# # node2 = ListNode(2)
# # node3 = ListNode(3)
# # node4 = ListNode(4)
# # node5 = ListNode(5)

# # root = node1
# # node1.next = node2
# # node2.next = node3
# # node3.next = node4
# # node4.next = node5


# # while root.next is not None:
# #     print(root.val)
# #     root = root.next

# # print(root.val)





