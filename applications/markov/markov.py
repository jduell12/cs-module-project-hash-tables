import random

# Read in all the words in one go
with open("input.txt") as f:
    #splits the input into words
    words = f.read().split()

#gets all the starting words
#Words that start with capital or "
start_words = []

#gets all ending words 
#words end in any type of punctuation or followed by "
end_words = []

word_freq = {}

for i in range(len(words)-1):
    word = words[i]
    #gets first letter
    c = word[0]
    if ord(c) == 34 or (ord(c) >= 65 and ord(c) <= 90):
        if word not in start_words:
            start_words.append(word)
            
    else:
        #gets end words
        end = word[len(word)-1]
        
        if ord(end) == 33 or ord(end) == 63 or ord(end) == 46 or ord(end) == 34:
            if word not in end_words:
                end_words.append(word)
        else:
            if words[i+1] != len(words)-1:
                if (word, words[i+1]) in word_freq:
                    word_freq[(word, words[i+1])] += 1
                else:
                    word_freq[(word, words[i+1])] = 1
            
#create list of dictionary
list = list(word_freq.items())

#construct 5 random sentences
for sent in range(5):
    s = ""
    #get random first word
    s += random.choice(start_words)
    
    #get number of words for the sentence 
    #on average english sentenances contain 15-20 words per wordcounter.net
    numWords = random.randint(14, 21)
    
    while numWords > 0:
        #gets random number
        randWord = random.randint(0, len(word_freq))
        word1 = list[randWord][0][0]
        word2 = list[randWord][0][1]
        s += f" {word1} {word2} "
        numWords -= 2
    
    #adds end word on sentenance
    s += random.choice(end_words)
    
    if ord(s[0]) == 34 and ord(s[len(s)-1]) != 34:
        s += chr(34)
    
    print(s)
    print("")
