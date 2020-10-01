import random

# Read in all the words in one go
with open("input.txt") as f:
    #splits the input into words
    words = f.read().split()

#gets all the starting words
#Words that start with capital or "
start_words = {}

#gets all ending words 
#words end in any type of punctuation or followed by "
end_words = {}

for i in range(len(words)):
    word = words[i]
    c = word[0]
    if ord(c) == 34 or (ord(c) >= 65 and ord(c) <= 90):
        if (word, words[i+1]) in start_words:
            start_words[(word, words[i+1])] += 1
        else:
            start_words[(word, words[i+1])] = 1
            


# TODO: construct 5 random sentences
# Your code here

