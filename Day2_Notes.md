# Day 2 - Hash Table Notes

- Collisions

  - different strings hash to the same number
  - handling collisions

        - disallow it
          - check if a number is already used and if it is return "No"
        - store in a linked list

          - aka chaining

          table = [None, None, None, None]

          | Slot Index | Chain (linked list) |
          |------------|---------------------|
          | 0 | --> None|
          | 1 | --> None|
          | 2 | --> None|
          | 3 | --> None|


        put("foo", 12) #hashes to 1
        put("bar", 30) #hashes to 2
        put("baz", 99) #hashes to 2 -- collision with "bar"
        put("qux", 10) #hashes to 0
        put("plugh", 20) #hashes to 1 -- collision
        put("xyzzy", 50) #hases to 2 -- collision

        | Slot Index | Chain (linked list) |
        | ---------- | ------------------- |
        | 0 | --> HashEntry("qux", 10) --> None |
        | 1 |--> HashEntry("plugh", 20) --> HashEntry("foo", 1) --> None |
        | 2 | --> HashEntry("xyzzy", 50) --> HashEntry("baz", 99) --> HashEntry("bar", 30) --> None |
        | 3 | --> None |

        - put in next slot that's available in a predictable manner
          - aka open addressing
          - performance isn't optimal
          - good for limited memory