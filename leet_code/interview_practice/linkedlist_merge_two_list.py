class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def merge_two_list(self, list1, list2):
        dummy = Node(0)
        cur = dummy

        while list1 and list2:
            if list1.data > list2.data:
                cur.next = list2
                list2 = list2.next 
            else:
                cur.next = list1
                list1 = list1.next

            cur = cur.next

        if list1:
            cur.next = list1
        cur.next = list2

        return dummy.next



def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

if __name__ == '__main__':
    a = Node(1)
    a.next = Node(3)
    a.next.next = Node(5)

    b = Node(2)
    b.next = Node(4)
    b.next.next= Node(6)

    l = LinkedList()

    print_list(l.merge_two_list(a,b))







