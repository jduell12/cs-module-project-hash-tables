# Day 1 Notes

- Hash Tables
  ["Lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "eli"]
  0 1 2 3 4 5 6 7

  - time complexity of linear search O(n) over length of the list
    for item in list:
    if item == "Beej":
    print("Found it")
    break

- need a function that tells us for a given string which index to look in
  "amet" -> f() -> 4
  "ipsum" -> f() -> 1

- takes a string and deterministically return a number indicating the index

- Collision

  - when hashing returns the same number for different strings

- Table for hashing numbers

  - need to turn the value received from the hashing function into an index within the table
  - value modulo of the length of the table
    - ex. table length 8
      - hashIndex = value % 8
  - hash function doesn't care about the indexing
    - only cares about returning a number for a string

- Put
  - storing in the hash table
- Get

  - getting something from a hash table

- No matter how big the table is the put, get functions are all constant time

- XOR (inclusive or)
  ^ in python
