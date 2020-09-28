#Naive hashing function - shouldn't be used
def hashf(s):
    total = 0;
    
    #encode string into bytes to be able to use unicode characters
    bytes = str(s).encode()
    
    for b in bytes:
        #add the byte to total
        total += b
    
    return total

print(hashf("Beej"))