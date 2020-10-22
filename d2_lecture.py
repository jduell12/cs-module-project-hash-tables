#linked list for Hash tables
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0
        
    def insert_at_head(self, node):
        node.next = self.head
        self.head = node 
        self.count += 1
        
    def find(self, value):
        cur = self.head
        #traverses linked list 
        while cur is not None and cur.value != value:
            cur = cur.next
        #checks if node is None or has a value
        if cur:
            return "Node(%d)" %cur.value
        else:
            return None
        
    def delete(self, value):
        #empty list case
        if self.head is None:
            return None
        
        #deleting head of list
        if self.head.value == value:
            old_head = self.head
            self.head = old_head.next
            old_head.next = None
            self.count -= 1
            return old_head.value
        
        cur = self.head
        
        while cur is not None and cur.value != value:
            prev = cur 
            cur = cur.next 
            
        if cur:
            prev.next = cur.next
            cur.next = None
            self.count -= 1
            return cur.value
        else:
            return None
        
    def __str__(self):
        r = f"count: {self.count}\n"
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
ll.delete(40)
print(ll)