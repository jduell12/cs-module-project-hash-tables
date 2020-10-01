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
    
    wordList = list(count.items())
    wordList.sort(key=lambda t:t[1])
    
    count = len(wordList)-1
    
    while count > 0:
        #same frequency need to order alphabetically
        if wordList[count][1] == wordList[count-1][1]:
            pass
        else:
            length = wordList[count][1]
            s = ""
            for i in range(length):
                s += "#"
            #sets space for formatting    
            space = ""
            for i in range(10-len(wordList[count][0])):
                space += " "
            
            print(f"{wordList[count][0]} {space}  {s:>}")
        count -= 1
    
histo('robin.txt')