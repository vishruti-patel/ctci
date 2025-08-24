class Node:
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







