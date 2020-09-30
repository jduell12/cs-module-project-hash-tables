import collections

def no_dups(s):
    dic = collections.OrderedDict()
    
    if len(s) > 1:
        #split string using whitespace
        words = s.split()
        #create a dictionary using the index and each word
        for index in range(len(words)):
            dic[index] = words[index]
            
        #order by values
        dic = sorted(dic.items(), key=lambda t:t[1])
        
        for index in range(len(dic)-1):
            if index == len(dic)-1:
                break
            
            if dic[index][1] == dic[index+1][1]:
                dic.pop(index)
        
        #order by key
        dic = sorted(dic)
        if len(dic) == 1:
            return dic[0][1]
        
        s = ""
        for k, v in dic:
            s += f'{v} '
    
    return s.strip()




if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))