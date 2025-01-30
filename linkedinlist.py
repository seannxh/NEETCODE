class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None  # Start with an empty list

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:  # Traverse until the last node
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node:
            elems.append(cur_node.data)  # Ensure cur_node is not None before accessing data
            cur_node = cur_node.next
        print(elems)

        
    def remove(self, idx, data):
        node = self.head
        idx = 0
        while node:
            node = node.next
        if node[idx] == self.data:
            node


# Create and test the linked list
my_list = LinkedList()
my_list.display()  # Should print []

my_list.append(1)
my_list.append(2)
my_list.append(3)

my_list.display()  # Should print [1, 2, 3]
print("Length:", my_list.length())  # Should print 3



