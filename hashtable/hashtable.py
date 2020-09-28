class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


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


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        keyInBytes = str(key).encode()
        
        #found in wikipedia article
        FNV_prime = 1099511628211
        #found in wikipedia article
        offset = 14695981039346656037
        
        # hash = fnv offset basis 
        hash = offset 
        
        #for each byte of data 
        for c in keyInBytes:
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
        #encode string so can use unicode characters as key
        keyInBytes = str(key).encode()
        
        #prime number
        hash = 5381
        
        for c in keyInBytes:
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
        index = self.hash_index(key)
        self.storage[index] = HashTableEntry(key, value)


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        hash_entry = self.storage[index]
        if hash_entry:
            return hash_entry.value
        else:
            return None
        


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here



if __name__ == "__main__":
    ht = HashTable(0x10000)
    
    # ht.put("line_1", "'Twas brillig, and the slithy toves")
    # ht.put("line_2", "Did gyre and gimble in the wabe:")
    # ht.put("line_3", "All mimsy were the borogoves,")
    # ht.put("line_4", "And the mome raths outgrabe.")
    # ht.put("line_5", '"Beware the Jabberwock, my son!')
    # ht.put("line_6", "The jaws that bite, the claws that catch!")
    # ht.put("line_7", "Beware the Jubjub bird, and shun")
    # ht.put("line_8", 'The frumious Bandersnatch!"')
    # ht.put("line_9", "He took his vorpal sword in hand;")
    # ht.put("line_10", "Long time the manxome foe he sought--")
    # ht.put("line_11", "So rested he by the Tumtum tree")
    # ht.put("line_12", "And stood awhile in thought.")

    # print("")

    #Test storing beyond capacity
    # for i in range(1, 13):
    #     print(ht.get("line_%d" %i))
    
    ht.put("key-0", "val-0")
    ht.put("key-1", "val-1")
    ht.put("key-2", "val-2")
    print("Test case 1 - no collisions --> insert and retrieve")
    return_value = ht.get("key-0")
    print(return_value == "val-0")
    return_value = ht.get("key-1")
    print(return_value == "val-1")
    return_value = ht.get("key-2")
    print(return_value == "val-2")
    print("")
    
    ht.put("key-0", "new-val-0")
    ht.put("key-1", "new-val-1")
    ht.put("key-2", "new-val-2")
    
    print("Test case 2 - no collisions --> overwriting")
    return_value = ht.get("key-0")
    print(return_value == "new-val-0")
    return_value = ht.get("key-1")
    print(return_value == "new-val-1")
    return_value = ht.get("key-2")
    print(return_value == "new-val-2")
    print("")
    
    ht.delete("key-2")
    ht.delete("key-1")
    ht.delete("key-0")
    
    print("Test case 3 - no collisions --> removes correctly")
    return_value = ht.get("key-0")
    print(return_value is None)
    return_value = ht.get("key-1")
    print(return_value is None)
    return_value = ht.get("key-2")
    print(return_value is None)

    # Test resizing
    # old_capacity = ht.get_num_slots()
    # ht.resize(ht.capacity * 2)
    # new_capacity = ht.get_num_slots()

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    print("")
