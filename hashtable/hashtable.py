class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    
    def __str__(self):
        return f"HashTableEntry({self.key}, {self.value})"
        
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0
        
    def insert_at_head(self, node):
        node.next = self.head
        self.head = node 
        self.count += 1
        
    def find(self, key):
        cur = self.head
        #traverses linked list 
        while cur is not None and cur.key != key:
            cur = cur.next
        #checks if node is None or has a value
        if cur:
            return cur
        else:
            return None
        
    def delete(self, key):
        #empty list case
        if self.head is None:
            return None
        
        #deleting head of list
        if self.head.key == key:
            old_head = self.head
            self.head = old_head.next
            old_head.next = None
            self.count -= 1
            return old_head
        
        cur = self.head
        
        while cur is not None and cur.key != key:
            prev = cur 
            cur = cur.next 
            
        if cur:
            prev.next = cur.next
            cur.next = None
            self.count -= 1
            return cur
        else:
            return None
        
        
    def __str__(self):
        r = f"count: {self.count}\n"
        if self.head is None:
            r += "None\n"
        #traverse the list
        cur = self.head
        while cur is not None:
            r += f"HashEntry({cur.key}, {cur.value})\n"
            if cur.next is not None:
                r += '-->'
            cur = cur.next
        return r
    
    def iterate(self):
        nodes = []
        if self.head is None:
            return None
        #traverse the list
        cur = self.head
        while cur is not None:
            nodes.append(cur)
            cur = cur.next
        return nodes


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.items = 0

    def __str__(self):
        r = ""
        for i in range(len(self.storage)):
            r += f"{i}: {self.storage[i]}\n"
        return r

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.items / self.capacity
    


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        #found in wikipedia article
        FNV_prime = 1099511628211
        #found in wikipedia article
        offset = 14695981039346656037
        
        # hash = fnv offset basis 
        hash = offset 
        
        #for each byte of data 
        for c in key:
            #hash * fnv prime 
            hash = hash * FNV_prime
            #hash XOR byte of data 
            hash = hash ^ ord(c)
            
        return hash
        


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Uses bit manipulation and prime numbers to create hash
        """
        
        #prime number
        hash = 5381
        
        for c in key:
            #get 32-bit hash
            hash = (hash * 33) + ord(c)
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        #get index for the key
        index = self.hash_index(key)
               
        if self.storage[index]:
            if self.storage[index].find(value):
                node = self.storage[index].find(key)
                node.value = value
            else:
                headNode = HashTableEntry(key, value)
                self.storage[index].insert_at_head(headNode)
                self.items += 1
                #check node factor
                # load_factor = self.get_load_factor()
                # if load_factor > 0.7:
                #     # double table size
                #     self.resize((self.capacity * 2))
        else:
            headNode = HashTableEntry(key, value)
            self.storage[index] = LinkedList()
            self.storage[index].insert_at_head(headNode)
            self.items += 1
            
        #Day 1
        # index = self.hash_index(key)
        # self.storage[index] = HashTableEntry(key, value)


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        
        if self.storage[index]:
            #if found return the value
            if self.storage[index].find(key):
                self.items -= 1
                return self.storage[index].delete(key)
            
        return None
        
        #Day 1
        # index = self.hash_index(key)
        
        # if self.storage[index]:
        #     self.storage[index] = None
        # else:
        #     print(f'{key} is not in the hash table')


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        #search linked list at that key for the value
        if self.storage[index]:
            #if found return the value
            if self.storage[index].find(key):
                return self.storage[index].find(key).value
            
        return None
    
        #Day 1
        # index = self.hash_index(key)
        # hash_entry = self.storage[index]
        # if hash_entry:
        #     return hash_entry.value
        # else:
        #     return None
        
        


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        #creates new array
        old_table = self.storage
        
        self.storage = [None] * new_capacity

        #sets capacity to new size
        self.capacity = new_capacity
        #resets the items count
        self.items = 0
        
        for old_list in old_table:
            if old_list is None:
                continue
            else:
                cur = old_list.head
                if cur:
                    while cur:
                        self.put(cur.key, cur.value)
                        cur = cur.next
            
                


if __name__ == "__main__":
    ht = HashTable(8)
    
    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")
    print("")
    # print(f"items: {ht.items}\n\n")
    # # print(f"load: {ht.get_load_factor()}\n\n")
    # print(ht)

    # # #Test storing beyond capacity
    for i in range(1, 13):
        print(f'{i} ', ht.get("line_%d" %i))
        

    ht.delete("line_12")
    ht.delete("line_1")
    ht.delete("line_8")
    ht.delete("line_2")
    print("")
    # # print(f"items: {ht.items}\n\n")
    # print(f"load: {ht.get_load_factor()}\n\n")
    # print(ht)
    

    # Test resizing
    # old_capacity = ht.get_num_slots()
    # ht.resize(ht.capacity * 2)
    # new_capacity = ht.get_num_slots()

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    # for i in range(1, 12):
    #     print(f'{i} ', ht.get("line_%d" %i))

    print("")
