#linked list for Hash tables
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_head(self, node):
        node.next = self.head
        self.head = node 
        
    def find(self, value):
        cur = self.head
        while cur is not None and cur.value != value:
            cur = cur.next
        if cur:
            return "Node(%d)" %cur.value
        else:
            return None
        
    def __str__(self):
        r = ""
        #traverse the list
        cur = self.head
        while cur is not None:
            r += " %d " % cur.value
            if cur.next is not None:
                r += '-->'
            cur = cur.next
        return r
        
ll = LinkedList()
ll.insert_at_head(Node(10))
ll.insert_at_head(Node(40))
ll.insert_at_head(Node(20))
print(ll)
print(ll.find(10))
print(ll.find(100))