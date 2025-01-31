from typing import Optional


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

class Node:
    def __init__(self, data, val):
        self.data = data
        self.val = val
        self.next = None

class Traversal:
    def __init__(self, val=0):
        self.head = None
        self.val = val

    #How to Traverse through Linked list and append 
    def Traverse(self, head):
        curr = head
        res = []
        while(curr != None):
            res.append(curr.data)
            curr = curr.next
        return res
    
    def AddTraverse(self, head, val):
        curr = head
        res = val
        while(curr != None):
            res += curr.val
            curr = curr.next
        return res
    
    def removeList(self, head):
        if head is None or head.next is None:
            return None

        curr = head

        while curr.next.next != None:
            curr = curr.next
        curr.next = None
        return head

    def addList(self, head, target):
        if head is None:
            return target  # If list is empty, the new node becomes the head

        curr = head
        while curr.next is not None:
            curr = curr.next

        curr.next = target  # Append the new node
        target.next = None  # Ensure the new node is the last one

        return head


    def searchbyVal(self, head, target):
        curr = head

        while curr != None:
            if curr.val == target:
                return True
            curr = curr.next
        return False

    def searchbyData(self, head, target):
        curr = head

        while curr != None:
            if curr.data == target:
                return True
            curr = curr.next
        return False
            

# Creating linked list: 1 -> 2 -> 3
node1 = Node(1, 100) #(data, val)
node2 = Node(2, 200)
node3 = Node(3, 300)

node1.next = node2
node2.next = node3

traversal = Traversal()
  # Output: [1, 2, 3]
print(traversal.Traverse(node1))
# print(traversal.AddTraverse(node1, 10))
# node1 = traversal.removeList(node1)
# print("After removing last node:", traversal.Traverse(node1))

print("Before adding new node:", traversal.Traverse(node1))  
new_node = Node(4, 400)

# Adding new node
node1 = traversal.addList(node1, new_node)

print("After adding new node:", traversal.Traverse(node1))  
# Expected Output: [1, 2, 3, 4]

# Searching by 'val'
print(traversal.searchbyVal(node1, 300))  # Output: True
print(traversal.searchbyVal(node1, 400))  # Output: False

# Searching by 'data'
print(traversal.searchbyData(node1, 3))  # Output: True
print(traversal.searchbyData(node1, 4))  # Output: False
#Reverse Linked List
class Solution:
    def reverseList(self, head: Optional[Node]) -> Optional[Node]:
        curr = head
        prev = None

        while (curr != None):
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev

class Solution:
    def mergeTwoLists(self, list1: Optional[Node], list2: Optional[Node]) -> Optional[Node]:
        

        head = node = Node()

        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
        head.next = list1 or list2

        return node.next
class Solution:
    def hasCycle(self, head: Optional[Node]) -> bool:
        
        seen = set()

        curr = head

        while curr:
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.next
        return False

                
