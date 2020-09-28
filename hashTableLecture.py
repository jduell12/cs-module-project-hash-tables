#list to hold hashing stringbased on the has number
table = [None] * 8

#Naive hashing function - shouldn't be used
def hashf(s):
    total = 0;
    
    #encode string into bytes to be able to use unicode characters
    bytes = str(s).encode()
    
    for b in bytes: #O(n) over length of the key/string s
        #add the byte to total
        total += b
    
    return total 

def get_index(s):
    value = hashf(s);
    return value % len(table)

def put(key, value):
    index = get_index(key)
    table[index] = value

def get(key):
    index = get_index(key)
    value = table[index]
    if value:
        return value
    else:
        return f'{key} is not in the table'

put("Beej", 3490)
print(table)
put("Goats!", 9999)
print(table)

print(get("Beej"))
print(get("Goats!"))
print(get("Jess"))