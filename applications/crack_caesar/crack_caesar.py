#frequent letters from most to least 
eng_freq = {'E': '11.53', 'T':'9.75', 'A':'8.46', 'O':'8.08', 'H':'7.71', 'N':'6.73', 'R':'6.29', 'I':'5.84', 'S':'5.56', 'D':'4.74', 'L':'3.92', 'W':'3.08', 'U':'2.59', 'G':'2.48', 'F':'2.42', 'B':'2.19', 'M':'2.18', 'Y':'2.02', 'C':'1.58', 'P':'1.08', 'K':'0.84', 'V':'0.59', 'Q':'0.17', 'J':'0.07', 'X':'0.07', 'Z':'0.03'}

invert_eng_freq = {}

for k in eng_freq:
    v = float(eng_freq[k])
    invert_eng_freq[v] = k


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
        cipher_freq[k] = f"{(cipher_freq[k] / length) * 100:.2f}"
        
    #key -> cipher text, value -> letter it should be
    cipher_decoder = {}
    
    for item in cipher_freq:
        cipher_decoder[item] = invert_eng_freq[float(cipher_freq[item])]
        
    #decodes the message 
    decoded = ""
    
    for c in words:
        if c in cipher_decoder:
            decoded += cipher_decoder[c]
        else:
            decoded += c
            
    print(decoded)
    
crack_caesar('ciphertext.txt')