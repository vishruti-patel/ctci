class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None


#Adding node to the end of the list
    def add_node(self, new_data):
       new_node = Node(new_data)
       if not self.head:
          self.head = new_node
          return
       current = self.head


       while current.next:
           current = current.next
       current.next = new_node


#printing all the node:
    def view_list(self):
        current = self.head
        while current:
            print(current.data, end = '->')
            current = current.next


    def lowest_val(self):
        if not self.head:
            print('Empty List')

        min_val = self.head.data
        current = self.head.next

        while current:
            if current.data < min_val:
                min_val = current.data
            current = current.next

        return min_val
    
if __name__ == '__main__':
    llist = Linkedlist()
    llist.add_node(10)
    llist.add_node(20)
    llist.add_node(30)
    llist.add_node(60)

    print(llist.view_list())






        
       

