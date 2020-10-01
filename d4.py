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

for r in records:
    if r[1] in department_index:
        department_index[r[1]].append(r[0])
    else:
        department_index[r[1]] = [r[0]]

print(department_index["Marketing"])