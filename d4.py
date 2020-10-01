import math 

inv_sqrt ={}

def build_lookup_table():
    for i in range(1, 1000):
        inv_sqrt[i] = 1/math.sqrt(i)
        
def get_inv_sqrt(n):
    #lazily add things to lookup table 
    if n not in inv_sqrt:
        inv_sqrt[n] = 1/math.sqrt(n)
    return inv_sqrt[n]

# build_lookup_table()
# print(get_inv_sqrt(37))
# print(get_inv_sqrt(2000))

#########################################################
#indexing
#names, department
records = [
    ("Alice", "Engineering"),
    ("Bob", "Sales"),
    ("Carol", "Sales"),
    ("Dave", "Engineering"),
    ("Erin", "Engineering"),
    ("Frank", "Engineering"),
    ("Grace", "Marketing")
]

#Who are all the people in a given department?

#naive
# d = "Engineering"

# for r in records: #O(n) over number of records 
#     if r[1] == d:
#         print(r[0])

#O(1) solution - hash tables
#key --> department
#value --> list of names

department_index = {}

def add_dept_index(name, dep):
    if dep not in department_index:
        department_index[dep] = []
    
    department_index[dep].append(name)

for r in records:
    add_dept_index(r[0], r[1])

# print(department_index["Engineering"])
# add_dept_index("Jess", "Engineering")
# print(department_index["Engineering"])

#########################################################
import urllib.request
import datetime 

class CacheEntry:
    def __init__(self, data):
        self.data = data
        self.timestamp = datetime.datetime.now().timestamp()

cache = {}

CACHE_TIMEOUT_SECS = 10

def web_cache():
    while True:
        url = input("Enter a URL: ")
        
        if url == '':
            break

        cur_time = datetime.datetime.now().timestamp()
        print(cur_time)
        
        if url not in cache or cur_time - cache[url].timestamp > CACHE_TIMEOUT_SECS:
            resp = urllib.request.urlopen(url)
            data = resp.read()
            cache[url] = CacheEntry(data)
            resp.close()
            print("CACHE MISS")
        else:
            print ("CACHE HIT")
        print(data[:75])
        
# web_cache()

#########################################################