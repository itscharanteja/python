class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete(self, key):
        curr_node = self.head
        if curr_node is not None and curr_node.data == key:
            self.head = curr_node.next
            curr_node = None
            return
        prev_node = None
        while curr_node is not None and curr_node.data != key:
            prev_node = curr_node
            curr_node = curr_node.next
        if curr_node is None:
            return
        prev_node.next = curr_node.next
        curr_node = None

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next
# create a linked list object
my_list = LinkedList()

# insert elements at the beginning or end of the list
my_list.insert_at_beginning(1)
my_list.insert_at_end(2)
my_list.insert_at_end(3)

# print the elements of the list
my_list.print_list()  # output: 1 2 3

# delete an element from the list
my_list.delete(2)

# print the updated list
my_list.print_list()  # output: 1 3
