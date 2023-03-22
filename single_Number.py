from typing import List


class Solution:
    # using library
    def firstsingleNumber(self, nums: List[int]) -> int:
        for i in nums:
           if nums.count(i) == 1:
               return i

    # using bitwise
    #Use Xor / Bit Manipulation
    #Xor of any two num gives the difference of bit as 1 and same bit as 0.
    #Thus, using this we get 1 ^ 1 == 0 because the same numbers have same bits.
    #So, we will always get the single element because all the same ones will evaluate to 0
    #and 0^single_number = single_number.
    def lastsingleNumber(self, nums: List[int]) -> int:
       sol = 0

       for i in nums:
           sol ^= i

       return sol
