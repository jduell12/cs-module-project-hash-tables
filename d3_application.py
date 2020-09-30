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

for i in dList:
    print(f"{i[0]}: {i[1]}")
    
#sort by value 
def sort_by(t):
    return t[1]

print("----------------")
#key parameter and give a function to sort by 
# default is sorting 0
dList.sort(key=sort_by)
for i in dList:
    print(f"{i[0]}: {i[1]}")