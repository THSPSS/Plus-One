'''
You're given strings jewels representing the types of stones that are jewels, and stones
representing the stones you have.
Each character in stones is a type of stone you have.
You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".


Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3


Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0
'''
#using library
from collections import Counter



#first attempt using sum and tuple comprehension
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum( stone in jewels for stone in stones)

    #other solution, using hashmap , dictionary
    def hashNumJewelsInStones(self, jewels: str, stones: str) -> int:
        result = 0
        hashmap = {}
        for jewel in jewels:
            hashmap[jewel] = 1

        for stone in stones:
            if stone in hashmap:
                result += 1

        return result


    #using Counter library
    def anotherNumJewelsInStones(self, J: str, S: str) -> int:
            return sum(Counter(S)[i] for i in J)