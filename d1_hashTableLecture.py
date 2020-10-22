#list to hold hashing stringbased on the has number
#length of list is a power of 2 
table = [None] * 8

class HashEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        
    def __repr__(self):
        return f"HashEntry({self.key}, {self.value})"

#Naive hashing function - shouldn't be used
def hashf(s):
    total = 0;
    #encode string into bytes to be able to use unicode characters
    bytes = str(s).encode()
    #O(n) over length of the key/string s
    for b in bytes: 
        #add the byte to total
        total += b
    return total 

def get_index(s):
    value = hashf(s);
    return value % len(table)

def put(key, value): 
    #O(n) over the length of the key
    #O(1) over the number of items in the table 
    index = get_index(key)
    table[index] = HashEntry(key, value)

def get(key):
    index = get_index(key)
    hash_entry = table[index]
    if hash_entry:
        return hash_entry.value
    else:
        return f'{key} is not in the table'

put("Beej", 3490)
# print(table)
put("Goats!", 9999)
# print(table)

print(get("Beej")) #3490
print(get("Goats!")) #9999
print(get("Jess")) #Not in table