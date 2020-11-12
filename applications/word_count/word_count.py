def word_count(s):
    # Your code here
    count = {}
    s_list = s.split()
    for word in s_list:
        word = word.strip('":;,.-+=/\\|[]}{()*^&')
        if word == '':
            continue
        word = word.lower()
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1
    return count

# def word_count(s):
#     count = {}
#     #ignore " : ; , . - + = / \ | [ ] { } ( ) * ^ & via Ascii
#     ignore = [34, 58, 59, 44, 46, 45, 43, 61, 47, 92, 124, 91, 93, 123, 125,40, 41, 42, 94, 38]
    
#     #check if string has a length
#     if len(s) > 0:
#         #split string using whitespace
#         words = s.split()
#         #go through each word in the string 
#         for word in words:
#             #change word to lower case 
#             word = word.lower()
#             #go through each character in the word
#             for c in word:
#                 if ord(c) in ignore:
#                     word = word.translate({ord(c):None})
                    
#             if word not in count:
#                 if len(word) > 0:
#                     count[word] = 1
#             else: 
#                 count[word] += 1
    
#     return count



if __name__ == "__main__":
    # print(word_count(""))
    print(word_count('":;,.-+=/\\|[]{}()*^&'))
    # print(word_count("Hello     hello"))
    # print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    # print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
