#fibonacci numbers - get n fibonacci number 
# 0 1 1 2 3 5 8 13 21 34...
#could use recursion - could end up taking a long time
# fib(0): 0
# fib(1): 1
# fib(n): fib(n-1) + fib(n-2) 
# time complexity: O(2^n)
# def fib(n):
#     if n <= 1: return n
#     return fib(n-1) + fib(n-2)

# for i in range(100):
#     print(f"{i:3} {fib(i)}")
    
#using hash table instead
#worst case O(n)
#dict needs to be outside of function so it saves the values it's calculating 
fibNums = {}

def fib(n):
    if n <= 1:
        return n
    
    if n not in fibNums:
        fibNums[n] = fib(n-1) + fib(n-2)
        
    return fibNums[n]
    
# for i in range(100):
#     print(f"{i:3} {fib(i)}")

#########################################################################
#sort a dictionary that's out of order
d = {
    "foo": 12,
    "bar": 17,
    "qux": 2
}

#order n
dList = list(d.items())
#sorts by keys 
dList.sort()

# for i in dList:
#     print(f"{i[0]}: {i[1]}")
    

# print("----------------")
#key parameter and give a function to sort by 
# default is sorting 0

#sort by value using named function
# def sort_by(t):
#     return t[1]

# dList.sort(key=sort_by)

#annonymous function in python 
dList.sort(key=lambda t:t[1])
# for i in dList:
#     print(f"{i[0]}: {i[1]}")

#########################################################################
#encryption

#Plaintext: HELLOWORLD
#Ciphertext: DOGGEBEUGW --> using encode table 

encode_table = {
    'A': 'H',
    'B': 'Z',
    'C': 'Y',
    'D': 'W',
    'E': 'O',
    'F': 'R',
    'G': 'J',
    'H': 'D',
    'I': 'P',
    'J': 'T',
    'K': 'I',
    'L': 'G',
    'M': 'L',
    'N': 'C',
    'O': 'E',
    'P': 'X',
    'Q': 'K',
    'R': 'U',
    'S': 'N',
    'T': 'F',
    'U': 'A',
    'V': 'M',
    'W': 'B',
    'X': 'Q',
    'Y': 'V',
    'Z': 'S'
}

def encode(s):
    r = ""
    for c in s:
        r += encode_table[c]
    return r

decode_table = {}

#order n 
for k, v in encode_table.items():
    decode_table[v] = k

def decode(s):
    r = ""
    for c in s:
        r += decode_table[c]
    return r

# print("")
# print(encode('HELLOWORLD')) #should be DOGGEBEUGW
# print("")
# print(decode('DOGGEBEUGW')) #should be HELLOWORLD
# print("")

#########################################################################
#counting letters in a string

def letter_count(s):
    d = {}
    
    for c in s:
        if c not in d:
            d[c] = 1  
        else: 
            d[c] += 1
    
    # for c in s:
    #     if c not in d:
    #         d[c] = 0
    #     d[c] += 1
    
    
    return d

# print(letter_count('abbbaaaaccaddadada'))
#get ascii number for chars in list - capittal letters 
alpha = [ chr(num) for num in range(65, 91)]

# print(alpha)

#########################################################################
#how full could a hash table get before getting a collision?
import hashlib
import random 

#returns big number for particular key
def hash_function(key):
    return int(hashlib.md5(str(key).encode()).hexdigest()[-8:], 16) & 0xffffffff

def how_many_before_collision(buckets, loops):
    for i in range(loops):
        tries = 0
        tried = set()
        
        while True:
            random_key = random.random()
            index = hash_function(random_key) % buckets
            
            if index not in tried:
                tried.add(index)
                tries += 1
            else:
                break
        print(f'{buckets} buckets, {tries} hashes before collison, {tries/buckets * 100} % full')
    
# how_many_before_collision(32768, 10)

#########################################################################
#objective challenge in TK
'''
You are building a running podcast playlist generator.

Long-distance runners love listening to podcasts on their runs. Their second podcast episode often gets cut off as they are ending their run. They want to be able to listen to two entire episodes during their long runs. You are building a feature that would choose two podcast episodes that will equal the exact length of their planned run.

Write a function that takes an integer run_length (in minutes) and a list of integers podcast_episode_lengths (in minutes) and returns a boolean whether there are two numbers in podcast_episode_lengths whose sum equals run_length. Remember that the runners will listen to precisely two episodes, and they will not want to listen to the same episode twice.
'''

def pod(total, podcasts):
    #could go through all of them
    #O(n^2) - not good for large n
    # for p0 in podcasts:
    #     for p1 in podcasts:
    #         if p0 + p1 == total:
    #             return True
    # return False
    podcast_len = {}
    for p in podcasts:
        podcast_len[p] = True
        
    for p0 in podcasts:
        #is there a podcast of total - p0 minutes?
        if (total-p0) in podcast_len:
            return True
    return False
    
    