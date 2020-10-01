#frequent letters from most to least 
eng_freq = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

def crack_caesar(fileName):
    cipher_freq = {}
    
    #reads the words from the file and puts into into a string
    with open(fileName) as f:
        words = f.read()
        
    #initialize number of letters in words to 0 to get letter freq
    length = 0
    
    #go through string and count the freq of each letter in the cipher text
    for c in words:
        if ord(c) < 65 or ord(c) > 90:
            continue
        #initalizes the letter into the dictionary
        if c not in cipher_freq:
            cipher_freq[c] = 0
        #increments the count for that letter
        cipher_freq[c] += 1
        length += 1
        
    for k in cipher_freq:
        cipher_freq[k] = cipher_freq[k] / length
        
    print(cipher_freq)
        
    
    
crack_caesar('ciphertext.txt')