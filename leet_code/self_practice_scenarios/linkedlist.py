class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return f"LinkNode(val={self.val}, next = {self.next}"

class LinkedList:
    def __init__(self):
        self.head = None    
        self.tail = None     #use this for add_new_tail_way

    def create_linked_list(self, data = "Vishruti"):
        for char in data:
            if not self.head:
                self.head = Node(char)
                self.tail = self.head
            else:
                self.add_new_tail_way(char)

    def print_list(self):
        temp = self.head
        while temp:
            if temp.next:
                print(temp.val, end= '->')
            else:
                print(temp.val)

            temp = temp.next


    def add_node(self, data):
        """
            [] -> [] -> [] -> []
        """
        tail = self.head
        while tail.next:
             tail = tail.next

        new_data = Node(data)
        tail.next = new_data

    def add_new_tail_way(self, data):
        self.tail.next = Node(data)
        self.tail = self.tail.next

    def delete_node_by_index(self, index):
        """  
            delete 3rd (kth) node in the linked list 

            [] -> [] -> [] -> [] -> [] -> []    
        """

        curr, start = self.head, 0
        while curr:
            if start == index - 1:
                curr.next = curr.next.next
                return
            
            curr, start = curr.next, start+1

            





if __name__ == '__main__':
    ll = LinkedList()
    ll.create_linked_list()
    # print(ll.head)
    # ll.print_list()
    # ll.add_node("Raxit")
    ll.print_list()

    # ll.delete_node_by_index(2)
    # ll.print_list()


