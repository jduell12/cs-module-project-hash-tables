def histo(fileName):
    count = {}
    #ignore " : ; , . - + = / \ | [ ] { } ( ) * ^ & via Ascii
    ignore = [34, 58, 59, 44, 46, 45, 43, 61, 47, 92, 124,91, 93, 123, 125,40, 41, 42, 94, 38]
    
    #opens file and reads all words
    with open(fileName) as f:
        s = f.read()
    
    #check if string has a length
    if len(s) > 0:
        #split string using whitespace
        words = s.split()
        #go through each word in the string 
        for word in words:
            #change word to lower case 
            word = word.lower()
            #go through each character in the word
            for c in word:
                if ord(c) in ignore:
                    word = word.translate({ord(c):None})
                    
            if word not in count:
                if len(word) > 0:
                    count[word] = 1
            else: 
                count[word] += 1
    
    print(count)
        
    
histo('robin.txt')