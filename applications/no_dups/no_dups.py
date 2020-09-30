def no_dups(s):
    
    if len(s) < 1:
        return s
    
    check = {}
    
    #split string via whitespace
    words = s.split()
    
    #add the word with their index into the dict
    for index in range(len(words)):
        check[index] = words[index]
        
    #getting array of keys with values
    checkList = list(check.items())
    
    #sort by values
    checkList.sort(key=lambda t:t[1])
    print("------------------")
    print(checkList)
    print("------------------")
    
    for checkIndex in range(len(check)):
        if checkIndex+1 < len(check) and checkList[checkIndex][0] == checkList[checkIndex+1][0]:
            checkList[checkIndex+1] = (checkIndex+1, '')
    
    #sort list by index to put words back in order
    checkList.sort()
    
    return checkList
        
    # word = " "
    
    # return word.join(words).strip()
    



if __name__ == "__main__":
    # print(no_dups(""))
    # print(no_dups("hello"))
    # print(no_dups("hello hello"))
    # print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))